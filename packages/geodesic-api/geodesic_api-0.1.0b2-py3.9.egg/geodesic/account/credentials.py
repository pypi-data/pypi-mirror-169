import base64
from geodesic.bases import APIObject
import json
from geodesic import raise_on_error
from geodesic.service import ServiceClient

from typing import Any
# Credentials client
credentials_client = ServiceClient("krampus", 1, "credentials")

SERVICE_ACCOUNT_KEY = 'SERVICE_ACCOUNT_KEY'
AWS_KEY_PAIR = 'AWS_KEY_PAIR'
AZURE_ACCESS_KEY = 'AZURE_ACCESS_KEY'
JWT = 'JWT'
OAUTH2_CLIENT_CREDENTIALS = 'OAUTH2_CLIENT_CREDENTIALS'
OAUTH2_REFRESH_TOKEN = 'OAUTH2_REFRESH_TOKEN'
BASIC_AUTH = 'BASIC_AUTH'

valid_types = [
    SERVICE_ACCOUNT_KEY,
    AWS_KEY_PAIR,
    AZURE_ACCESS_KEY,
    JWT,
    OAUTH2_CLIENT_CREDENTIALS,
    OAUTH2_REFRESH_TOKEN,
    BASIC_AUTH
]


def get_credential(name: str = None):
    """
    Gets the name/type of requested credential, or None if it doesn't exist

    Args:
        name: Name of the credential to access
    """
    res = raise_on_error(credentials_client.get(name))
    c = res.json()['credential']
    if c is None:
        return None
    return Credential(**c)


def get_credentials():
    """
    Returns all of your user's credentials
    """
    res = raise_on_error(credentials_client.get(''))
    return [Credential(**p) for p in res.json()['credentials']]


class Credential(APIObject):
    """
    Credentials to access secure resources such as a cloud storage bucket. Credentials have
    a name, type and data. Credentials can be created or deleted but not accessed again
    except by internal services. This is for security reasons. Credentials are stored using
    symmetric PGP encryption at rest.
    """
    _limit_setitem = [
        "name",
        "type",
        "data"
    ]

    def __init__(self, **credential):
        self._name = None
        self._type = None
        self.__data = bytes()
        self._client = credentials_client
        for k, v in credential.items():
            setattr(self, k, v)

    def create(self):
        """
        Creates a new Credentials. Encodes the data to be sent.
        """

        data = self.__data
        if isinstance(data, bytes):
            enc_data = base64.b64encode(data).decode()
        elif isinstance(data, dict):
            enc_data = base64.b64encode(json.dumps(data).encode()).decode()
        elif isinstance(data, str):
            enc_data = base64.b64encode(data.encode()).decode()

        raise_on_error(self._client.post("", name=self.name, type=self.type, data=enc_data))

    def delete(self):
        raise_on_error(self._client.delete(self.name))

    @property
    def name(self):
        return self['name']

    @name.setter
    def name(self, v: str):
        if not isinstance(v, str):
            raise ValueError("name must be a string")
        self._set_item('name', v)

    @property
    def type(self):
        return self['type']

    @type.setter
    def type(self, v: str):
        if v not in valid_types:
            raise ValueError(f"type must be one of {valid_types}")
        self._set_item('type', v)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, v: str):
        self.__data = v

    def __setattr__(self, name: str, value: Any) -> None:
        if name == 'data':
            self.__data = value
        return super().__setattr__(name, value)
