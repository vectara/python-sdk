import logging
from abc import ABC
from dataclasses import dataclass
from dacite import from_dict, Config, UnexpectedDataError, UnionMatchError
from typing import Optional, Union, Any, List, Dict
import json
import yaml
from os import path, sep
from pathlib import Path

"""
Collection of dataclasses related to the configuration of the application.

"""
logger = logging.getLogger(__name__)


@dataclass
class BaseAuthConfig:

    def getAuthType(self) -> str:
        raise NotImplementedError("You must implement this method to return the String type of the auth")


@dataclass
class ApiKeyAuthConfig(BaseAuthConfig):
    api_key: str

    def getAuthType(self) -> str:
        return "ApiKey"


@dataclass
class OAuth2AuthConfig(BaseAuthConfig):
    auth_url: Optional[str]
    app_client_id: str
    app_client_secret: str

    def getAuthType(self) -> str:
        return "OAuth2"

    def validate(self):
        pass


@dataclass
class ClientConfig:
    """
    Wrapper for all configuration needed to work with Vectara.
    """

    customer_id: str
    auth: Union[ApiKeyAuthConfig, OAuth2AuthConfig]

    def validate(self) -> List[str]:
        errors = []

        if not self.customer_id:
            errors.append(f"In [{self.__class__.__name__}] You must define the field [customer_id]")

        return errors


def _tryCreateAuth(data_class, input):
    try:
        from_dict(data_class=data_class, data=input, config=Config(strict=True))
        return True, None
    except Exception as e:
        return False, str(e)


def loadConfig(config: str) -> ClientConfig:
    """
    Loads our configuration from JSON onto our data classes.

    :param config: the input configuration in JSON format.
    :return: the parsed client configuration1
    :raises TypeError: if the configuration cannot be parsed correctly
    """
    logger.info(f"Loading config from {config}")

    try:
        config_dict = json.loads(config)



        return from_dict(ClientConfig, config_dict, config=Config(strict=True))
    except UnionMatchError as e:
        raise TypeError(e)
    except UnexpectedDataError as e:
        raise TypeError(e)

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

    def _convert_dict_config(self, config_dict: Dict[str, Any]) -> ClientConfig:
        """
        Helper method for all subclasses of BaseConfigLoader to parse a dict into our config domain classes.

        :param config_dict: the input configuration as a dict
        :return: the parsed client configuration
        :raises TypeError: if the configuration cannot be parsed correctly
        """

        # First we're going to manually try each Authentication Type for better logging.
        # This is because the dicate library just gives the user a generic error
        # without any logging.
        auth = config_dict["auth"]
        if (auth):
            oauth2_success, oauth2_error_msg = _tryCreateAuth(OAuth2AuthConfig, auth)
            api_key_success, api_key_error_msg = _tryCreateAuth(ApiKeyAuthConfig, auth)

            if not oauth2_success and not api_key_success:
                logger.error(f"Invalid Authentication Configuration:\n{json.dumps(auth, indent=4)}")
                logger.error(f"Unable to cast auth to OAuth2 configuration block: {oauth2_error_msg}")
                logger.error(f"Unable to cast auth to API Key configuration block: {api_key_error_msg}")

                raise TypeError(
                    f"Could not use polymorphism to cast auth to either OAuth2 or API Key config, see errors above in log.")

        self.logger.info("Parsing config")
        try:
            client_config = from_dict(data_class=ClientConfig, data=config_dict, config=Config(strict=True))
            client_config.validate()
            return client_config
        except UnexpectedDataError as e:
            raise TypeError(f"Unable to build configuration: {e}") from None

    def _load_yaml_config(self, final_config_path):
        with open(final_config_path, 'r') as yaml_stream:
            creds = yaml.safe_load(yaml_stream)

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
        return self._convert_dict_config(config_dict)


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
        return self._convert_dict_config(config_dict)

class HomeConfigLoader(BaseConfigLoader):
    """
    Loads our configuration from the users home directory
    """

    def __init__(self, profile: Union[str, None] = BaseConfigLoader.DEFAULT_CONFIG_NAME):
        super().__init__(profile=profile)

    def load(self):
        home = str(Path.home())
        self.logger.info(f"Loading configuration from users home directory [{home}]")

        looking_for = home + sep + BaseConfigLoader.CONFIG_FILE_NAME
        if not path.exists(looking_for) or not path.isfile(looking_for):
            raise TypeError(f"Unable to find configuration file [{BaseConfigLoader.CONFIG_FILE_NAME}]"
                            f" within home directory [{home}]")
        config_dict = self._load_yaml_config(looking_for)
        return self._convert_dict_config(config_dict)


