# Created by Noé Cruz | Zurckz 22 at 24/09/2022
# See https://www.linkedin.com/in/zurckz
from enum import Enum
from typing import Any

from zcloud.aws.secret_manager import SecretManager
from zcloud.aws.ssm import SSMParameter
from zpy.utils.parallel import TaskExecutor
from zpy.logger.utils import Loggable
import os


class SecretProvider(Enum):
    SSM = 'ssm'
    SECRET_MANAGER = 'secretsmanager'


class SecretProviderManager(Loggable):

    def __init__(self, main_provider: SecretProvider, provider_timeout: float = 2.0):
        Loggable.__init__(self)
        self.priority = main_provider
        self.ssm = SSMParameter.create()
        self.sm = SecretManager()
        self.timeout = provider_timeout

    def __retrieve_with_ssm(self, name: str):
        return TaskExecutor(task=self.ssm.get, args=(name,), logger=self.logger).run(self.timeout)

    def __retrieve_with_sm(self, name: str):
        return TaskExecutor(task=self.sm.get_value, args=(name,), logger=self.logger).run(self.timeout)

    def __retrieve(self, name: str, parallel: bool):
        if self.priority == SecretProvider.SECRET_MANAGER:
            if parallel:
                result = self.__retrieve_with_sm(name)
            else:
                result = self.sm.get_value(name)
            if not result:
                if parallel:
                    return self.__retrieve_with_ssm(name)
                return self.ssm.get(name)
            return result
        if parallel:
            result = self.__retrieve_with_ssm(name)
        else:
            result = self.ssm.get(name)
        if not result:
            if parallel:
                return self.__retrieve_with_sm(name)
            return self.sm.get_value(name)
        return result

    def get_value(self, name: str, model: Any = None):
        value = self.__retrieve(name, False)
        if value and model:
            return model(**value)
        return value

    def get(self, name: str, model: Any = None):
        """
        Retrieve parameter
        :param model:
        :param name: parameter name
        :return:
        """
        use_parallel = os.name != 'nt'
        value = self.__retrieve(name, use_parallel)
        if value and model:
            return model(**value)
        return value

    def configure(self, ssm: SSMParameter, sm: SecretManager):
        self.sm = sm
        self.ssm = ssm

    @classmethod
    def create_with_sm(cls, provider_timeout: float = 2.0) -> 'SecretProviderManager':
        """
        Create instance using Secret Manager as main provider.
        :return:
        """
        return cls(SecretProvider.SECRET_MANAGER, provider_timeout)

    @classmethod
    def create_with_ssm(cls, provider_timeout: float = 2.0) -> 'SecretProviderManager':
        """
        Create instance using Simple System Manager as main provider.
        :return:
        """
        return cls(SecretProvider.SSM, provider_timeout)
