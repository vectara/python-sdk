import logging
from abc import ABC
from typing import Optional, Union, Any, List, Dict
from pydantic import BaseModel, Discriminator, Tag
from typing_extensions import Annotated
import json
import yaml
from os import path, sep
from pathlib import Path

"""
Collection of dataclasses related to the configuration of the application.

"""
logger = logging.getLogger(__name__)


class BaseAuthConfig(BaseModel):

    def get_auth_type(self) -> str:
        raise NotImplementedError("You must implement this method to return the String type of the auth")


class ApiKeyAuthConfig(BaseAuthConfig):
    api_key: str

    def get_auth_type(self) -> str:
        return "ApiKey"


class OAuth2AuthConfig(BaseAuthConfig):
    app_client_id: str
    app_client_secret: str

    def get_auth_type(self) -> str:
        return "OAuth2"


def get_discriminator_value(v: Any) -> str:
    has_api_key = False
    has_oauth2 = False

    if isinstance(v, dict):
        if 'api_key' in v:
            has_api_key = True
        if 'app_client_id' in v and 'app_client_secret' in v:
            has_oauth2 = True
    else:
        if hasattr(v, 'api_key'):
            has_api_key = True
        if hasattr(v, 'app_client_id') and hasattr(v, 'app_client_secret'):
            has_oauth2 = True

    if has_api_key and has_oauth2:
        raise Exception("Invalid configuration, specify an api_key or OAuth2 values, but not both")
    elif has_api_key:
        return 'ApiKey'
    elif has_oauth2:
        return 'OAuth2'
    else:
        raise Exception("Invalid configuration, specify api_key or OAuth2 values (app_client_id and app_client_secret)")



class ClientConfig(BaseModel):
    """
    Wrapper for all configuration needed to work with Vectara.
    """

    customer_id: str

    auth: Annotated[
        Union[
            Annotated[ApiKeyAuthConfig, Tag('ApiKey')],
            Annotated[OAuth2AuthConfig, Tag('OAuth2')],
        ],
        Discriminator(get_discriminator_value),
    ]

def loadConfig(config: str) -> ClientConfig:
    """
    Loads our configuration from JSON onto our data classes.

    :param config: the input configuration in JSON format.
    :return: the parsed client configuration1
    :raises TypeError: if the configuration cannot be parsed correctly
    """
    logger.info(f"Loading config from {config}")
    return ClientConfig.model_validate_json(config)

class BaseConfigLoader(ABC):
    CONFIG_FILE_NAME = ".vec_auth.yaml"

    DEFAULT_CONFIG_NAME = "default"

    def __init__(self, profile: Union[str, None] = DEFAULT_CONFIG_NAME):
        self.logger = logging.getLogger(self.__class__.__name__)
        if not profile:
            self.profile = self.DEFAULT_CONFIG_NAME
        else:
            self.profile = profile

    def load(self):
        """
        :return: The client configuration in our domain class ClientConfig
        :raises TypeError: Should be implemented in subclasses.
        """
        raise Exception("Define in sublcass")

    def _load_yaml_full(self, final_config_path):
        with open(final_config_path, 'r') as yaml_stream:
            return yaml.safe_load(yaml_stream)



    def _load_yaml_config(self, final_config_path):
        creds = self._load_yaml_full(final_config_path)

        if self.profile:
            self.logger.info(f"Loading specified profile [{self.profile}]")
            profile_to_load = self.profile
        else:
            self.logger.info(f"Loading default configuration [{BaseConfigLoader.DEFAULT_CONFIG_NAME}]")
            profile_to_load = BaseConfigLoader.DEFAULT_CONFIG_NAME


        if profile_to_load in creds:
            return creds[profile_to_load]
        else:
            raise TypeError(f"Specified profile [{profile_to_load}] not found in [{final_config_path}]")

    def _save(self, client_config: ClientConfig, final_config_path: str):
        creds = self._load_yaml_full(final_config_path)
        creds[self.profile] = client_config.model_dump()

        with open(final_config_path, 'w') as yaml_stream:
            yaml.safe_dump(creds, yaml_stream)

    def _delete(self, final_config_path: str):
        creds = self._load_yaml_full(final_config_path)
        del creds[self.profile]

        with open(final_config_path, 'w') as yaml_stream:
            yaml.safe_dump(creds, yaml_stream)


class JsonConfigLoader(BaseConfigLoader):
    """
    Loads our configuration from JSON
    """

    def __init__(self, config_json: str, profile: Union[str, None] = BaseConfigLoader.DEFAULT_CONFIG_NAME):
        super().__init__(profile=profile)
        self.config_json = config_json

    def load(self):
        self.logger.info("Loading configuration from JSON string")
        config_dict = json.loads(self.config_json)
        return ClientConfig.model_validate(config_dict)


class PathConfigLoader(BaseConfigLoader):
    """
    Loads our configuration from the specified folder/file
    """

    def __init__(self, config_path : str, profile: Union[str, None] = BaseConfigLoader.DEFAULT_CONFIG_NAME):
        super().__init__(profile=profile)

        self.config_path = config_path

    def load(self):
        self.logger.info(f"Loading configuration from path {self.config_path}")

        if path.exists(self.config_path) and path.isdir(self.config_path):
            self.logger.info(f"Configuration param is a path, looking for {BaseConfigLoader.CONFIG_FILE_NAME}")
            looking_for = self.config_path / BaseConfigLoader.CONFIG_FILE_NAME
            if not path.exists(looking_for) or not path.isfile(looking_for):
                raise TypeError(f"Unable to find configuration file [{BaseConfigLoader.CONFIG_FILE_NAME}]"
                                f" within specified directory [{self.config_path}]")
        elif path.exists(self.config_path) and path.isfile(self.config_path):
            self.logger.info(f"Configuration param is a file")
            looking_for = self.config_path
        else:
            raise TypeError(f"Path [{self.config_path}] does not exist.")

        config_dict = self._load_yaml_config(looking_for)
        return ClientConfig.model_validate(config_dict)



class HomeConfigLoader(BaseConfigLoader):
    """
    Loads our configuration from the users home directory
    """

    def __init__(self, profile: Union[str, None] = BaseConfigLoader.DEFAULT_CONFIG_NAME):
        super().__init__(profile=profile)

    def _build_config_path(self) -> str:
        home = str(Path.home())
        self.logger.info(f"Loading configuration from users home directory [{home}]")

        looking_for = home + sep + BaseConfigLoader.CONFIG_FILE_NAME
        if not path.exists(looking_for) or not path.isfile(looking_for):
            raise TypeError(f"Unable to find configuration file [{BaseConfigLoader.CONFIG_FILE_NAME}]"
                            f" within home directory [{home}]")
        return looking_for

    def load(self):
        config_dict = self._load_yaml_config(self._build_config_path())
        return ClientConfig.model_validate(config_dict)

    def has_profile(self) -> bool:
        try:
            existing = self.load()
            if existing:
                return True
            else:
                return False
        except TypeError as e:
            self.logger.info("No existing profile found")
            return False

    def save(self, to_save: ClientConfig):
        config_path = self._build_config_path()
        self._save(to_save, config_path)

    def delete(self):
        config_path = self._build_config_path()
        self._delete(config_path)
