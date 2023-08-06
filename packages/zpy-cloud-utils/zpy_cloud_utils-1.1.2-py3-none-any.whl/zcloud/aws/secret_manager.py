# Created by Noé Cruz | Zurckz 22 at 24/09/2022
# See https://www.linkedin.com/in/zurckz
from typing import Optional, Any
from json import loads
from zcloud.aws import AWSCredentials, AWSService
from zpy.containers.MemoryCacheSystem import MemoryCacheSystem


class SecretManager(AWSService, MemoryCacheSystem):

    def __init__(self, credentials: Optional[AWSCredentials] = None, config: dict = None, use_cache=False):
        AWSService.__init__(self, "secretsmanager", credentials, config)
        self.cache = use_cache

    def __build(self, value, model):
        if value and model:
            return model(**value)
        if value:
            return value

    def from_cache(self, secret_name: str, model: Any = None, refresh=False):
        if not self.cache:
            raise ValueError("The cache is not initialized for this instance")
        if refresh is True:
            return self.get_value(secret_name, model, False)

    def get_value(self, name: str, model: Any = None, use_cache: bool = False) -> Any:
        if use_cache or self.cache:
            value = self.get_or(name, None)
            if value:
                return self.__build(value, model)

        value = self.get_client().get_secret_value(SecretId=name)
        value = loads(value['SecretString'])
        if self.cache:
            self.set(name, value)
        return self.__build(value, model)
