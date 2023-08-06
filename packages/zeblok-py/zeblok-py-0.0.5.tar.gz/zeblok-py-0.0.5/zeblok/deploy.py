from typing import Union
from pathlib import Path
import minio
import os
from datetime import timedelta
from .errors import FileUploadError, InvalidCredentialsError, BucketDoesNotExistsError
from zipfile import ZipFile
from .utils import api_error, Progress, get_all_file_paths, validate_base_url, validate_platform_id, \
    validate_namespace_id, validate_deployment_name, validate_username
import requests
import json

STORAGE_URL = "datalake.zbl-aws.zeblok.com:9000"
CROSS_CLOUD_SERVICE_URL = "http://cross-cloud-services-673735588.us-east-2.elb.amazonaws.com/upload"


class DeployModel:
    __slots__ = ['__CROSS_CLOUD_SERVICE_URL', '__storage_url', '__bucket_name', '__base_url', '__token', '__username']

    def __init__(self, base_url: str, token: str, bucket_name: str, username: str, storage_url: str):
        validate_base_url(base_url=base_url)
        if type(token) is not str:
            raise InvalidCredentialsError('token can only be of type String')
        elif token == '':
            raise InvalidCredentialsError('token cannot empty')
        elif token.split()[0] != 'Bearer':
            raise InvalidCredentialsError('Please pass a valid Bearer token')

        validate_username(username=username)

        self.__bucket_name = bucket_name
        self.__username = username
        self.__storage_url = storage_url
        self.__CROSS_CLOUD_SERVICE_URL = CROSS_CLOUD_SERVICE_URL
        self.__base_url = 'https://' + base_url
        self.__token = token

    @property
    def token(self):
        return self.__token

    @property
    def base_url(self):
        return self.__base_url

    @property
    def cross_cloud_service_url(self):
        return self.__CROSS_CLOUD_SERVICE_URL

    def get_datacenters(self) -> [dict]:
        response = requests.get(
            f"{self.__base_url}/api/v1/dataCenter/public/", data=json.dumps({"isActive": True}),
            headers={'Authorization': self.__token, 'Content-Type': 'application/json', 'request-from': 'Ai-MicroCloud'}
        )
        if response.status_code == 200 and response.json()['success']:
            datacenters = []
            for data in response.json()['data']:
                datacenters.append({'_id': data['_id'], 'name': data['name']})
            return datacenters
        else:
            api_error(status_code=response.status_code, message=response.text)

    def get_namespaces(self) -> [dict]:
        response = requests.get(
            f"{self.__base_url}/api/v1/namespaces/org/", data=json.dumps({"state": "ready"}),
            headers={'Authorization': self.__token, 'Content-Type': 'application/json', 'request-from': 'Ai-MicroCloud'}
        )
        if response.status_code == 200 and response.json()['success']:
            return response.json()['data']
        else:
            api_error(status_code=response.status_code, message=response.text)

    @staticmethod
    def prepare_model_zip(model_folder_path: Path) -> Path:
        print("\nPreparing model zip")
        model_zipfile_path = model_folder_path.parent.joinpath(f'{model_folder_path.name.lower()}.zip')
        with ZipFile(model_zipfile_path, 'w') as zip:
            file_paths = get_all_file_paths(directory=model_folder_path)
            for file in file_paths:
                zip.write(filename=file.as_posix(), arcname=file.relative_to(model_folder_path))
        print("Model zip prepared")
        return model_zipfile_path

    def upload_file(self, file_name: Path, secret_key: str) -> str:
        try:
            client = minio.Minio(
                endpoint=self.__storage_url, access_key=self.__username, secret_key=secret_key, secure=False
            )

            if not client.bucket_exists(self.__bucket_name):
                raise BucketDoesNotExistsError(f'{self.__bucket_name} does not exists')

            client.fput_object(
                bucket_name=self.__bucket_name, object_name=f"{file_name.name}",
                file_path=file_name.as_posix(), content_type="application/zip",
                progress=Progress(), part_size=5 * 1024 * 1024
            )

            url = client.presigned_get_object(
                bucket_name=self.__bucket_name, object_name=f"{file_name.name}",
                expires=timedelta(hours=3)
            )
        finally:
            os.remove(file_name)
        return url

    def call_cross_cloud_service(
            self, cross_cloud_service_url: str, presigned_get_url: str, image_name: str, file_name: str,
            image_id: Union[str, None], deployment_type: str, autodeploy: bool = False,
            namespace_id: Union[None, str] = None, platform_id: Union[None, str] = None,
            deployment_name: Union[None, str] = None
    ):
        if autodeploy:
            validate_platform_id(platform_id=platform_id)
            validate_namespace_id(namespace_id=namespace_id)
            validate_deployment_name(deployment_name=deployment_name)

        response = requests.post(
            cross_cloud_service_url,
            headers={'Authorization': self.__token, 'Content-Type': 'application/json',
                     'request-from': 'Ai-MicroCloud'},
            data=json.dumps({
                "imageName": image_name, "url": presigned_get_url, "filename": file_name,
                "portalUrl": f"{self.__base_url}", "imageId": image_id,
                "autoDeploy": autodeploy, "namespaceId": None if not autodeploy else namespace_id,
                "platform": None if not autodeploy else platform_id,
                "deploymentName": None if not autodeploy else deployment_name,
                "deploymentType": deployment_type
            })
        )
        if response.status_code == 200:
            if response.json()['success']:
                return
            else:
                raise FileUploadError(response.json()['job'])
        else:
            api_error(status_code=response.status_code, message=response.text)
