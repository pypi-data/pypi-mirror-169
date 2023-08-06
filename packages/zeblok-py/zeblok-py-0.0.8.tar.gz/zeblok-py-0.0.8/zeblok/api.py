from typing import Union
from .deploy import DeployModel
from pathlib import Path
import os
import time
from .errors import InvalidModelFolder, FileUploadError, ModelDeploymentError
from .utils import api_error, get_all_file_paths, validate_model_pipeline, validate_username, validate_platform_id, \
    validate_namespace_id, validate_deployment_name, validate_model_folder
import requests
import json


class ModelAPI(DeployModel):
    def __init__(self, base_url: str, token: str, bucket_name: str, username: str, storage_url: str):
        super(ModelAPI, self).__init__(
            base_url=base_url, token=token, bucket_name=bucket_name, username=username, storage_url=storage_url
        )

    def get_model_pipelines(self) -> [dict]:
        response = requests.get(
            f"{self.base_url}/api/v1/aimodel/", data=json.dumps({"state": "ready"}),
            headers={'Authorization': self.token, 'Content-Type': 'application/json'}
        )
        if response.status_code == 200 and response.json()['success']:
            image_names = []
            for data in response.json()['data']:
                image_names.append({'_id': data['_id'], 'imageName': data['imageName']})
            return image_names
        else:
            api_error(status_code=response.status_code, message=response.text)

    @staticmethod
    def __validate_folder_format(model_folder_path: Path) -> None:
        validate_model_folder(model_folder_path=model_folder_path)
        for filepath in get_all_file_paths(directory=model_folder_path):
            if filepath.name == 'Dockerfile' and filepath.parent.name == model_folder_path.name:
                return
        raise InvalidModelFolder(f"Invalid BentoML folder format: {model_folder_path}")

    def __register_image_name(self, image_name: str):
        response = requests.post(
            f"{self.base_url}/api/v1/aimodel/", data=json.dumps({"imageName": image_name, "type": "bentoml"}),
            headers={'Authorization': self.token, 'Content-Type': 'application/json'}
        )
        print(response.request.body)
        if response.status_code == 201:
            if response.json()['success']:
                return response.json()['data']['_id']
            else:
                raise FileUploadError(response.json()['message'])
        else:
            api_error(status_code=response.status_code, message=response.text)

    def upload_model(
            self, model_folder_path: str, username: str, storage_secret_key: str,
            autodeploy: bool = False, namespace_id: Union[None, str] = None, platform_id: Union[None, str] = None,
            deployment_name: Union[None, str] = None,
    ) -> str:
        validate_username(username=username)
        folder_path = Path(model_folder_path)
        self.__validate_folder_format(model_folder_path=folder_path)
        model_zipfile_path = self.prepare_model_zip(model_folder_path=folder_path)
        presigned_url = self.upload_file(file_name=model_zipfile_path, secret_key=storage_secret_key)
        image_name = f"zeblok/{model_zipfile_path.stem}:{int(time.time())}".lower()
        image_id = self.__register_image_name(image_name=image_name)
        self.call_cross_cloud_service(
            cross_cloud_service_url=self.cross_cloud_service_url, presigned_get_url=presigned_url,
            image_name=image_name, file_name=model_zipfile_path.name, image_id=image_id, autodeploy=autodeploy,
            namespace_id=namespace_id, deployment_name=deployment_name, platform_id=platform_id,
            deployment_type='aimodel'
        )
        print(
            f"\nSuccessfully uploaded the Model folder | Filename: {model_zipfile_path.name}, Image Name: {image_name}"
        )
        return image_name

    def deploy_model(self, deployment_name: str, namespace_id: str, platform_id: str, model_pipeline: str):
        validate_deployment_name(deployment_name=deployment_name)
        validate_namespace_id(namespace_id=namespace_id)
        validate_platform_id(platform_id=platform_id)
        validate_model_pipeline(model_pipeline=model_pipeline)

        if model_pipeline not in [img_nm['imageName'] for img_nm in self.get_model_pipelines()]:
            raise ValueError(f'Image Name: {model_pipeline} not found in the database')

        response = requests.post(
            f"{self.base_url}/api/v1/k8deployments/",
            headers={'Authorization': self.token, 'Content-Type': 'application/json'},
            data=json.dumps({
                "imageName": model_pipeline, "nodePreference": "NO PREFERENCE", "kioskId": None,
                "platform": platform_id,
                "namespaceId": namespace_id, "deploymentName": deployment_name
            })
        )

        if response.status_code == 201:
            if response.json()['success']:
                print(
                    f"\n{response.json()['message']}"
                )
                return response.json()['success']
            else:
                raise ModelDeploymentError(response.json()['message'])
        else:
            api_error(status_code=response.status_code, message=response.text)
