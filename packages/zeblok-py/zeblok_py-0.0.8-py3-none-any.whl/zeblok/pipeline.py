from typing import Union
from pathlib import Path
import minio
import os
from datetime import timedelta
from .errors import FileUploadError, InvalidCredentialsError, BucketDoesNotExistsError, PipelineCreationError
from zipfile import ZipFile
from .utils import api_error, Progress, get_all_file_paths, validate_url, validate_platform_id, \
    validate_namespace_id, validate_secret_key, validate_envs_args, \
    validate_model_folder
import requests
import json
import time

STORAGE_URL = "datalake.zbl-aws.zeblok.com:9000"
CROSS_CLOUD_SERVICE_URL = "http://cross-cloud-services-673735588.us-east-2.elb.amazonaws.com/upload"


class Pipeline:
    __slots__ = [
        '__base_url', '__cross_cloud_service_url', '__storage_url', '__api_access_key', '__api_access_secret',
        '__storage_username', '__storage_access_secret'
    ]

    def __init__(
            self, base_url: str, cross_cloud_service_url: str, storage_url: str, api_access_key: str,
            api_access_secret: str, storage_username: str, storage_access_secret: str
    ):

        validate_url(url_name='base_url', url=base_url)
        validate_url(url_name='cross_cloud_service_url', url=cross_cloud_service_url)
        validate_url(url_name='storage_url', url=storage_url)

        validate_secret_key(key_name='api_access_key', secret_key=api_access_key)
        validate_secret_key(key_name='api_access_secret', secret_key=api_access_secret)
        validate_secret_key(key_name='storage_username', secret_key=storage_username)
        validate_secret_key(key_name='storage_access_secret', secret_key=storage_access_secret)

        self.__base_url = 'https://' + base_url
        self.__cross_cloud_service_url = 'https://' + cross_cloud_service_url
        self.__storage_url = storage_url

        self.__api_access_key = api_access_key
        self.__api_access_secret = api_access_secret
        self.__storage_username = storage_username
        self.__storage_access_secret = storage_access_secret

    @property
    def base_url(self):
        return self.__base_url

    @property
    def cross_cloud_service_url(self):
        return self.__cross_cloud_service_url

    def get_datacenters(self) -> None:
        response = requests.get(
            f"{self.__base_url}/api/v1/dataCenter/public/", data=json.dumps({"isActive": True}),
            auth=(self.__api_access_key, self.__api_access_secret),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 200 and response.json()['success']:
            for data in response.json()['data']:
                print(f"Datacenter Name: {data['name']} | Datacenter ID: {data['_id']}")
        else:
            api_error(status_code=response.status_code, message=response.text)

    def get_namespaces(self) -> [dict]:
        response = requests.get(
            f"{self.__base_url}/api/v1/namespaces/org/", data=json.dumps({"state": "ready"}),
            auth=(self.__api_access_key, self.__api_access_secret),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 200 and response.json()['success']:
            for data in response.json()['data']:
                print(f"Namespace Name: {data['name']} | Namespace ID: {data['_id']}")
        else:
            api_error(status_code=response.status_code, message=response.text)

    def get_plans(self) -> None:
        response = requests.get(
            f"{self.base_url}/api/v1/plans/",
            auth=(self.__api_access_key, self.__api_access_secret),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 200 and response.json()['success']:
            for plan in response.json()['data']:
                print(f"Plan Name: {plan['planName']} | Id: {plan['_id']}")
                print("\tResources")
                print(f"\t\tvCPU: {plan['resources']['CPU']}")
                print(f"\t\tGPU: {plan['resources']['GPU']}")
                print(f"\t\tmemory [GB]: {plan['resources']['memory']}")
                print(f"\t\tstorage [GB]: {plan['resources']['storage']}")
                print(f"\t\tworkers: {plan['resources']['workers']}")
                print(f"\tDatacenter Name: {plan['dataCenterId']['name']} | Datacenter ID: {plan['dataCenterId']['_id']}")

        else:
            api_error(status_code=response.status_code, message=response.text)

    def __get_dockerfile(self, envs: list[str], entrypoint: list[str]) -> str:

        response = requests.get(
            f"{self.__base_url}/api/v1/system/dockerfile", auth=(self.__api_access_key, self.__api_access_secret),
            headers={'Content-Type': 'application/json'}, data=json.dumps({
                "from": {"baseImage": "miniconda3"}, "copy": {"./": "./"},
                "entrypoint": entrypoint, "env": dict([kv.split("=") for kv in envs])
            })
        )
        if response.status_code == 200:
            if response.json()['success']:
                return response.json()['data']
            else:
                api_error(status_code=response.status_code, message=response.json()['error']['message'])
        else:
            api_error(status_code=response.status_code, message=response.text)

    def __put_dockerfile(self, model_folder_path: Path, envs: list[str], entrypoint: list[str]) -> bool:
        validate_model_folder(model_folder_path=model_folder_path)
        with open(model_folder_path.joinpath('Dockerfile'), 'w') as fp:
            fp.write(self.__get_dockerfile(envs=envs, entrypoint=entrypoint))
        return True

    @staticmethod
    def __prepare_model_zip(model_folder_path: Path) -> Path:
        print("\nPreparing model zip .....")
        model_zipfile_path = model_folder_path.parent.joinpath(f'{model_folder_path.name.lower()}.zip')
        with ZipFile(model_zipfile_path, 'w') as zip:
            file_paths = get_all_file_paths(directory=model_folder_path)
            for file in file_paths:
                zip.write(filename=file.as_posix(), arcname=file.relative_to(model_folder_path))
        print("Model zip prepared")
        return model_zipfile_path

    def __upload_file(self, file_name: Path, bucket_name: str) -> str:
        try:
            client = minio.Minio(
                endpoint=self.__storage_url, access_key=self.__storage_username,
                secret_key=self.__storage_access_secret, secure=False
            )

            if not client.bucket_exists(bucket_name):
                raise BucketDoesNotExistsError(f'{bucket_name} does not exists')

            client.fput_object(
                bucket_name=bucket_name, object_name=f"{file_name.name}",
                file_path=file_name.as_posix(), content_type="application/zip",
                progress=Progress(), part_size=5 * 1024 * 1024
            )

            url = client.presigned_get_object(
                bucket_name=bucket_name, object_name=f"{file_name.name}",
                expires=timedelta(hours=3)
            )
        finally:
            os.remove(file_name)
        return url

    def __call_cross_cloud_service(
            self, cross_cloud_service_url: str, presigned_get_url: str, image_name: str, file_name: str,
            image_id: Union[str, None], plan_id: list[str], deployment_type: str, autodeploy: bool = False,
            namespace_id: Union[None, str] = None, platform_id: Union[None, list[str]] = None
    ):
        if autodeploy:
            # validate_platform_id(platform_id=platform_id)
            validate_namespace_id(namespace_id=namespace_id)

        response = requests.post(
            cross_cloud_service_url, auth=(self.__api_access_key, self.__api_access_secret),
            headers={'Content-Type': 'application/json'},
            data=json.dumps({
                "imageName": image_name,
                "url": presigned_get_url,
                "imageId": image_id,
                "filename": file_name,
                "portalUrl": f"{self.__base_url}",
                "autoDeploy": autodeploy,
                "namespaceId": None if not autodeploy else namespace_id,
                "platform": None if not autodeploy else platform_id,
                "deploymentType": deployment_type,
                "planId": plan_id
            })
        )
        if response.status_code == 200:
            if response.json()['success']:
                return
            else:
                raise FileUploadError(response.json()['job'])
        else:
            api_error(status_code=response.status_code, message=response.text)

    def __create_pipeline(
            self, pipeline_name: str, plan_id: list[str], namespace_id: str, datacenter_id: list[str], envs: list[str],
            args: list[str], docker_image_tag: str
    ):
        response = requests.post(
            f"{self.base_url}/api/v1/pipeline/", auth=(self.__api_access_key, self.__api_access_secret),
            headers={'Content-Type': 'application/json'},
            data=json.dumps({
                "pipelineName": pipeline_name,
                "planId": plan_id,
                "namespaceId": namespace_id,
                "yamlString": "from",
                "platform": datacenter_id,
                "env": envs,
                "args": args,
                "dockerImageTag": docker_image_tag
            })
        )
        print(response.request.body)
        if response.status_code == 200:
            if response.json()['success']:
                return response.json()['data']['_id']
            else:
                raise PipelineCreationError(response.json())
        else:
            api_error(status_code=response.status_code, message=response.text)

    def deploy_pipeline(
            self, model_folder_path: str, bucket_name: str, pipeline_name: str, plan_id: list[str], namespace_id: str,
            datacenter_id: list[str], envs: Union[str, None] = None, args: Union[str, None] = None,
            entrypoint: Union[str, None] = None, autodeploy: bool = False
    ):

        model_folder_path = Path(model_folder_path)

        envs = [] if envs is None else list(map(str.strip, envs.split(',')))
        if len(envs):
            validate_envs_args(name='envs', val=envs)

        args = [] if args is None else list(map(str.strip, args.split(',')))
        if len(args):
            validate_envs_args(name='args', val=args)

        entrypoint = [] if entrypoint is None else list(map(str.strip, entrypoint.split()))

        # self.__put_dockerfile(model_folder_path=model_folder_path, envs=envs, entrypoint=entrypoint)

        docker_image_tag = f"dockerhub.zeblok.io/zeblok/{pipeline_name.lower()}:{int(time.time())}"

        pipeline_id = self.__create_pipeline(
            pipeline_name=pipeline_name, plan_id=plan_id, namespace_id=namespace_id, datacenter_id=datacenter_id,
            envs=envs, args=args, docker_image_tag=docker_image_tag
        )

        print("Completed create_pipeline")

        model_zipfile_path = self.__prepare_model_zip(model_folder_path)
        print(model_zipfile_path)
        print("Completed model Zipping")

        presigned_url = self.__upload_file(file_name=model_zipfile_path, bucket_name=bucket_name)
        print("Completed zip file upload")

        self.__call_cross_cloud_service(
            cross_cloud_service_url=self.cross_cloud_service_url, presigned_get_url=presigned_url,
            image_name=docker_image_tag, file_name=model_zipfile_path.name, image_id=pipeline_id, autodeploy=autodeploy,
            namespace_id=namespace_id, platform_id=datacenter_id,
            deployment_type='pipeline', plan_id=plan_id
        )
        print("Completed cross-cloud service call")
