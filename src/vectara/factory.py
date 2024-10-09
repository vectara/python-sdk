from .config.config import JsonConfigLoader, PathConfigLoader, HomeConfigLoader, BaseConfigLoader
from .base_client import BaseVectara
from vectara.managers.corpus import CorpusManager
from vectara.managers.upload import UploadManager, UploadWrapper
from vectara.utils import LabHelper

import httpx

from .environment import VectaraEnvironment

from typing import Union, Optional, Callable
import logging
import os

class WrappedVectara(BaseVectara):
    """
    We extend the Vectara client, adding additional helper services. Due to the methodology used in the
    Vectara constructor, hard-coding dependencies and using an internal wrapper, we use lazy initialization
    for the helper classes like the CorpusManager.
    """


    def __init__(self, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.corpus_manager: Union[None, CorpusManager] = None
        self.upload_manager: Union[None, UploadManager] = None
        self.lab_helper: Union[None, LabHelper] = None


    def set_corpus_manager(self, corpus_manager: CorpusManager) -> None:
        self.corpus_manager = corpus_manager

    def set_upload_manager(self, upload_manager: UploadManager) -> None:
        self.upload_manager = upload_manager

    def set_lab_helper(self, lab_helper: LabHelper) -> None:
        self.lab_helper = lab_helper


class Factory():

    """
    Allows us to access multiple API keys from an environment or local configuration by name.

    Environment variable which indicates which profile to use, either from other environment variables, or the users
    profile. This will be overridden by explicitly indicating the profile as a parameter.

    If this is provided, it can still use environment variables for the authentication, it will just take a different
    form, using the syntax, "VECTARA_{profile.upper()}_{suffix}". So for example, if value for "VECTARA_PROFILE" is
    "test", the value for the API key will be "VECTARA_TEST_API_KEY".

    A valid configuration is given below - observe the following for a "test" profile:

    * VECTARA_PROFILE = "test"
    * VECTARA_TEST_API_KEY = "asdf"

    """
    ENV_VAR_PROFILE = "VECTARA_PROFILE"

    """
    The default environment variable containing the API key if no profile is requested. 
    """
    ENV_VAR_API_KEY = "VECTARA_API_KEY"

    """
    The default environment variable containing the OAuth2 Client ID if no profile is requested. 
    """
    ENV_VAR_OAUTH2_CLIENT_ID = "VECTARA_CLIENT_ID"

    """
    The default environment variable containing the OAuth2 Client Secret if no profile is requested. 
    """
    ENV_VAR_OAUTH2_CLIENT_SECRET = "VECTARA_CLIENT_SECRET"


    def __init__(self, config_path: Union[str, None] = None, config_json: Union[str, None] = None, profile: Union[str,  None] = None):
        """
        Initialize our factory using configuration which may either be in a file or serialized in a JSON string

        :param config_path: the file containing our configuration
        :param config_json: the JSON containing our configuration
        """

        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("initializing builder")
        self.config_path = config_path
        self.config_json = config_json
        self.profile = profile

    def _check_profile_env(self) -> Optional[str]:
        profile: Optional[str] = os.getenv(self.ENV_VAR_PROFILE)
        if profile:
            self.logger.info(f"We found the profile [{profile}] from the environment")
        return profile

        #api_key: typing.Optional[str] = os.getenv("VECTARA_API_KEY"),
        #client_id: typing.Optional[str] = os.getenv("VECTARA_CLIENT_ID"),
        #client_secret: typing.Optional[str] = os.getenv("VECTARA_CLIENT_SECRET")

    def build(self) -> WrappedVectara:
        """
        Builds our client using the configuration which .
        :return:
        """

        config_loader: BaseConfigLoader

        # 1. Load the config whether we're doing file or we've had it passed in as a String.
        if self.config_path:
            self.logger.info("Factory will load configuration from path")
            config_loader = PathConfigLoader(config_path=self.config_path, profile=self.profile)
        elif self.config_json:
            self.logger.info("Factory will load configuration from JSON")
            config_loader = JsonConfigLoader(config_json=self.config_json, profile=self.profile)
        else:
            self.logger.info("Factory will load configuration from home directory")
            config_loader = HomeConfigLoader(profile=self.profile)

        # 2. Parse and validate the client configuration
        try:
            client_config = config_loader.load()
        except Exception as e:
            # Raise a new exception without extra stack trace. We know the JSON failed to parse.
            raise TypeError(f"Unable to build factory due to configuration error: {e}")

        # 3. Load the validated configuration into our client.
        auth_config = client_config.auth
        auth_type = auth_config.get_auth_type()
        logging.info(f"We are processing authentication type [{auth_type}]")

        # Defining the host is optional and defaults to https://api.vectara.io
        # See configuration.py for a list of all supported configuration parameters.
        client: WrappedVectara
        if auth_type == "ApiKey":
            client = WrappedVectara(
                api_key=client_config.auth.api_key,
            )
        elif auth_type == "OAuth2":
            client = WrappedVectara(
                client_id=auth_config.app_client_id,
                client_secret=auth_config.app_client_secret,
            )
        else:
            raise TypeError(f"Unknown authentication type: {auth_type}")

        # Inject our convenience managers
        corpus_manager = CorpusManager(client.corpora)
        client.set_corpus_manager(corpus_manager)

        upload_wrapper = UploadWrapper(upload_client=client.upload, customer_id=client_config.customer_id)
        upload_manager = UploadManager(upload_wrapper)
        client.set_upload_manager(upload_manager)

        lab_helper = LabHelper(corpus_manager)
        client.set_lab_helper(lab_helper)


        # Return the client
        return client
