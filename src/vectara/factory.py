from vectara.config.config import (PathConfigLoader, HomeConfigLoader, ClientConfig, EnvConfigLoader, ApiKeyAuthConfig,
                                   OAuth2AuthConfig)
from .client import Vectara
from vectara.managers.corpus import CorpusManager
from vectara.managers.upload import UploadManager, UploadWrapper
from vectara.utils import LabHelper

from typing import Union, Optional, Callable, Dict, Any
import logging
import os

class Factory():

    """
    Allows us to access multiple API keys from an environment or local configuration by name.

    This loader uses the following precedence (priority given to first satisfied):

    1. Explicit Configuration via param "config" as ClientConfig which matches
    2. Explicit Configuration via param "config" as Dict which matches pydantic ClientConfig
    3. TODO Explicit Configuration via YAML given by path (Need to fix this)
    3. TODO Environment Variables for Profile (See below)
    4. TODO General Environment Variables
    5. Profile for param "profile" within YAML file ".vec_auth.yaml" in users home directory.
    6. Default profile called "default" within YAML file ".vec_auth.yaml" in users home directory.



    Environment variable which indicates which profile to use, either from other environment variables, or the users
    profile. This will be overridden by explicitly indicating the profile as a parameter.

    If this is provided, it can still use environment variables for the authentication, it will just take a different
    form, using the syntax, "VECTARA_{profile.upper()}_{suffix}". So for example, if value for "VECTARA_PROFILE" is
    "test", the value for the API key will be "VECTARA_TEST_API_KEY".

    A valid configuration is given below - observe the following for a "test" profile:

    * VECTARA_PROFILE = "test"
    * VECTARA_TEST_API_KEY = "asdf"

    """

    def __init__(self, config_path: Union[str, None] = None, config: Optional[Union[ClientConfig, Dict[str, Any]]] = None, profile: Union[str,  None] = None):
        """
        Initialize our factory using configuration which may either be in a file or serialized in a JSON string

        :param config_path: the file containing our configuration
        :param config_json: the JSON containing our configuration
        """

        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("initializing builder")
        self.config_path = config_path
        self.config = config
        self.profile = profile
        self.load_method: Optional[str] = None

    def build(self) -> Vectara:
        """
        Builds our client using the configuration which .
        :return:
        """

        client_config: Optional[ClientConfig] = None

        # 1. Load the config whether we're doing file or we've had it passed in as a String.
        if self.config:
            if isinstance(self.config, ClientConfig):
                self.logger.info("Using explicit configuration from pydantic typed config")
                client_config = self.config
                self.load_method = "explicit_typed"
            elif isinstance(self.config, Dict):
                self.logger.info("Using explicit configuration from dict config")
                client_config = ClientConfig.model_validate(self.config)
                self.load_method = "explicit_dict"
            else:
                raise Exception(f"Unexpected type for config [{type(self.config)}]")

        if not client_config:
            client_config = EnvConfigLoader().load()
            if client_config:
                self.logger.info("Using configuration from env variables")
                self.load_method = "env"

        if not client_config:
            if self.config_path:
                self.logger.info("Factory will load configuration from path")
                client_config = PathConfigLoader(config_path=self.config_path, profile=self.profile).load()
                self.load_method = "path_explicit"
            else:
                self.logger.info("Factory will load configuration from home directory")
                client_config = HomeConfigLoader(profile=self.profile).load()
                self.load_method = "path_home"

        if not client_config:
            raise Exception("No client configuration specified by any method (explicit, env or home location)")

        auth_config = client_config.auth
        logging.info(f"We are processing authentication type [{auth_config.get_auth_type()}]")

        # Bind our configuration onto our client class.
        client: Vectara
        if isinstance(auth_config, ApiKeyAuthConfig):
            client = Vectara(
                api_key=auth_config.api_key,
            )
        elif isinstance(auth_config, OAuth2AuthConfig):
            client = Vectara(
                client_id=auth_config.app_client_id,
                client_secret=auth_config.app_client_secret,
            )
        else:
            raise TypeError(f"Unknown authentication type: {type(auth_config)}")

        # Inject our convenience managers
        # TODO Move this into Vectara client
        corpus_manager = CorpusManager(client.corpora)
        client.set_corpus_manager(corpus_manager)

        upload_wrapper = UploadWrapper(upload_client=client.upload, customer_id=client_config.customer_id)
        upload_manager = UploadManager(upload_wrapper)
        client.set_upload_manager(upload_manager)

        lab_helper = LabHelper(corpus_manager)
        client.set_lab_helper(lab_helper)


        # Return the client
        return client
