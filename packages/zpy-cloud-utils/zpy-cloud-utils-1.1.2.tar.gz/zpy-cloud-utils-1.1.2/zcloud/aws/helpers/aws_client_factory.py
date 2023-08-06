# Created by Noé Cruz | Zurckz 22 at 25/09/2022
# See https://www.linkedin.com/in/zurckz
from enum import Enum
from typing import Any, Optional
from botocore.client import Config
from zpy.containers.MemoryCacheSystem import MemoryCacheSystem

from zcloud.aws import AWSCredentials, AWSSession


class Custom:
    def __init__(self, name: str):
        self.value = name

    @property
    def v(self):
        return self.value


class AwsServices(Enum):
    COGNITO_IDP = 'cognito-idp'
    LAMBDA = 'lambda'
    DYNAMO = 'dynamodb'
    REKOGNITION = 'rekognition'
    SQS = 'sqs'
    S3 = 's3'

    @property
    def v(self):
        return self.value

    @staticmethod
    def new(name: str):
        return Custom(name)


class AwsClientFactory(MemoryCacheSystem):
    Services = AwsServices

    def __init__(self, credentials: Optional[AWSCredentials] = None, config: Config = None):
        super().__init__()
        self.credentials = credentials
        self.config = config
        self.session = AWSSession(credentials, config)

    def get_client(self, service: AwsServices, **kwargs) -> Any:
        service_name = f'c{service.value}'
        client = self.get_or(service_name, None)

        if client:
            return client

        client = self.new_client(service, **kwargs)
        self.set(service_name, client)
        return client

    def get_resource(self, service: AwsServices, **kwargs) -> Any:
        resource_name = f'r{service.value}'
        resource = self.get_or(resource_name, None)

        if resource:
            return resource

        client = self.new_resource(service, **kwargs)
        self.set(resource_name, client)
        return client

    def new_client(self, service: AwsServices, **kwargs):
        if kwargs and 'config' not in kwargs:
            kwargs['config'] = self.config
        return self.session.client(name=service.value, **kwargs)

    def new_resource(self, service: AwsServices, **kwargs):
        if kwargs and 'config' not in kwargs:
            kwargs['config'] = self.config
        return self.session.resource(name=service.value, **kwargs)
