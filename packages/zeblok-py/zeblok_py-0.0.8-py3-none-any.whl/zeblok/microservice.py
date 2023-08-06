from .deploy import DeployModel
from pathlib import Path
from .errors import InvalidModelFolder, FileUploadError, InvalidCredentialsError, ModelDeploymentError
from .utils import api_error, get_all_file_paths
import requests
import time
import json
from .utils import validate_model_folder


class ModelMicroService(DeployModel):
    def __init__(self, base_url: str, token: str, bucket_name: str, username: str, storage_url: str):
        super(ModelMicroService, self).__init__(
            base_url=base_url, token=token, bucket_name=bucket_name, username=username, storage_url=storage_url
        )

    def __put_dockerfile(self, model_folder_path: Path) -> bool:
        validate_model_folder(model_folder_path=model_folder_path)
        with open(model_folder_path.joinpath('Dockerfile'), 'w') as fp:
            fp.write(self.__get_dockerfile(self.base_url, self.token))
        return True

    @staticmethod
    def __get_dockerfile(base_url: str, token: str) -> str:
        response = requests.get(
            f"{base_url}/api/v1/system/dockerfile",
            headers={'Authorization': token, 'Content-Type': 'application/json', 'request-from': 'Ai-MicroCloud'}
        )
        if response.status_code == 200:
            if response.json()['success']:
                return response.json()['data']
            else:
                api_error(status_code=response.status_code, message=response.json()['error']['message'])
        else:
            api_error(status_code=response.status_code, message=response.text)

    def get_plans(self) -> None:
        response = requests.get(
            f"{self.base_url}/api/v1/plans/",
            headers={'Authorization': self.token, 'Content-Type': 'application/json', 'request-from': 'Ai-MicroCloud'}
        )
        if response.status_code == 200 and response.json()['success']:
            for plan in response.json()['data']:
                print(f"Plan Name: {plan['planName']}")
                print(f"Id: {plan['_id']}")
                print(f"Datacenters:")
                print(f"\tName: {plan['dataCenterId']['name']}")
                print(f"\tId: {plan['dataCenterId']['_id']}")
        else:
            api_error(status_code=response.status_code, message=response.text)

    def __create_microservice(
            self, microservice_name: str, microservice_description: str, image_name: str, plan_id: str
    ) -> str:
        response = requests.post(
            f"{self.base_url}/api/v1/microservices/",
            data=json.dumps({
                "name": microservice_name,
                "description": microservice_description,
                "imageTag": [{"displayName": image_name, "dockerImage": image_name}],
                "defaultPlan": plan_id,
                "plans": [plan_id],
                "parameters": {
                    "ports": "4200"
                },
                "s3ImageLink": "https://zeblokcomputationalpublicimages.s3.ap-south-1.amazonaws.com/logo_6238a5205888964d61cdd42a.jpg",
                "isPublic": "true"
            }),
            headers={'Authorization': self.token, 'Content-Type': 'application/json', 'request-from': 'Ai-MicroCloud'}
        )
        # print(response.request.body)
        if response.status_code == 201:
            if response.json()['success']:
                print([{"displayName": image_name, "dockerImage": image_name}])
                return response.json()['data']['_id']
            else:
                raise ModelDeploymentError(response.json()['message'])
        else:
            api_error(status_code=response.status_code, message=response.text)

    def upload_model(
            self, model_folder_path: str, storage_secret_key: str, microservice_name: str,
            microservice_description: str, plan_id: str
    ) -> str:
        folder_path = Path(model_folder_path)
        # self.__put_dockerfile(Path(folder_path))
        model_zipfile_path = self.prepare_model_zip(model_folder_path=folder_path)
        presigned_url = self.upload_file(file_name=model_zipfile_path, secret_key=storage_secret_key)
        version = int(time.time())
        image_name = f"zeblok/{model_zipfile_path.stem}:{version}".lower()
        self.call_cross_cloud_service(
            cross_cloud_service_url=self.cross_cloud_service_url, presigned_get_url=presigned_url,
            image_name=image_name, file_name=model_zipfile_path.name, image_id=None, autodeploy=False,
            namespace_id='', deployment_name='', platform_id='', deployment_type='microservices'
        )
        return self.__create_microservice(
            microservice_name=f"{microservice_name}: {version}", microservice_description=microservice_description,
            image_name=image_name, plan_id=plan_id
        )

    def deploy_microservice(
            self, image_name: str, microservice_id: str, plan_id: str, service_name: str,
            namespace_id: str, datacenter_id: str, envs: list[str]
    ):

        response = requests.post(
            f"{self.base_url}/api/v1/spawnedservices/",
            data=json.dumps({
                "microserviceId": microservice_id, "dataCenterId": datacenter_id,
                "planId": plan_id,
                "namespaceId": namespace_id,
                "parameters": {
                    "ports": [5000],
                    "envs": envs,
                    "args": None,
                    "command": None
                },
                "name": service_name,
                "imageTag": {"displayName": image_name, "dockerImage": image_name}
            }),
            headers={'Authorization': self.token, 'Content-Type': 'application/json', 'request-from': 'Ai-MicroCloud'}
        )

        if response.status_code == 201:
            if response.json()['success']:
                return response.json()['message']
            else:
                raise ModelDeploymentError(response.json()['message'])
        else:
            api_error(status_code=response.status_code, message=response.text)
