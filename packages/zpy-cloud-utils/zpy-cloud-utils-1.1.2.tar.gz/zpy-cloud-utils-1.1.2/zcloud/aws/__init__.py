from abc import ABC, abstractmethod
from enum import Enum

__author__ = "Noé Cruz | contactozurckz@gmail.com"
__copyright__ = "Copyright 2021, Small APi Project"
__credits__ = ["Noé Cruz", "Zurck'z"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Noé Cruz"
__email__ = "contactozurckz@gmail.com"
__status__ = "Dev"

from typing import Any, Optional

from boto3 import Session, client

AWS_DEFAULT_REGION = "us-east-1"
AWS_DNS = "https://s3.amazonaws.com/"


class AWSCredentials:
    def __init__(self, ak: str = None, sk: str = None, st: str = None, region: str = AWS_DEFAULT_REGION,
                 profile_name: str = None) -> None:
        self.access_key = ak
        self.secret_key = sk
        self.session_token = st
        self.profile_name = profile_name
        self.region = region


class AWSSession:
    def __init__(self, credentials: Optional[AWSCredentials] = None, config: dict = None):
        self.config = config
        self.credentials = credentials
        self.__session = None
        self.__initialize()

    def __initialize(self):
        if self.credentials:
            self.__session = Session(
                aws_access_key_id=self.credentials.access_key,
                aws_secret_access_key=self.credentials.secret_key,
                region_name=self.credentials.region,
                profile_name=self.credentials.profile_name
            )
            return
        self.__session = Session()

    def client(self, name: str, **kwargs):
        return self.__session.client(name, **kwargs)

    def resource(self, name: str, **kwargs):
        return self.__session.resource(name, **kwargs)


class AWSService(ABC):

    def __init__(self, name: str, credentials: Optional[AWSCredentials] = None, config: dict = None):
        self.name = name
        self.config = config
        self.credentials = credentials
        self.__client = None
        self.__session = None
        self.__initialize()

    def __initialize_client(self):
        if self.__session:
            self.client = self.__session.client(self.name, self.credentials.region)
            return
        self.__client = client(self.name, config=self.config)

    def __initialize(self):
        if self.credentials:
            self.__session = Session(
                aws_access_key_id=self.credentials.access_key,
                aws_secret_access_key=self.credentials.secret_key,
                region_name=self.credentials.region,
                profile_name=self.credentials.profile_name
            )
        self.__initialize_client()

    def get_session(self) -> Session:
        return self.__session

    def configure_session(self, session: Session) -> None:
        self.__session = session
        self.__initialize_client()

    def get_client(self) -> Any:
        return self.__client

    def configure_client(self, new_client: Any) -> Any:
        self.__client = new_client


class CredentialsMode(Enum):
    PROFILE = 1
    CREDENTIALS = 2
