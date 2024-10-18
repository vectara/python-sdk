import os

from vectara.factory import Factory
from vectara.config import HomeConfigLoader, EnvConfigLoader, ApiKeyAuthConfig, OAuth2AuthConfig
from pathlib import Path

import unittest
import logging

class FactoryConfigTest(unittest.TestCase):
    """
    This test depends on our YAML default config being defined.

    We use this to test various methods of injection.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.basicConfig(format='%(asctime)s:%(name)-35s %(levelname)s:%(message)s', level=logging.INFO,
                            datefmt='%H:%M:%S %z')
        self.logger = logging.getLogger(self.__class__.__name__)

    def _test_factory_auth(self, target: Factory, expected_method: str):
        client = target.build()
        self.assertEqual(expected_method, target.load_method)

        if not client.corpus_manager:
            raise Exception("Corpus manager should be defined")

        results = client.corpus_manager.find_corpora_with_filter("", 1)
        if results and len(results) > 0:
            self.logger.info(f"Found corpus [{results[0].key}]")


    def test_default_load(self):
        factory = Factory()
        self._test_factory_auth(factory, "path_home")

    def test_explicit_path(self):
        factory = Factory(config_path=str(Path.home().resolve()))
        self._test_factory_auth(factory, "path_explicit")

    def test_env(self):
        client_config = HomeConfigLoader().load()
        os.environ[EnvConfigLoader.ENV_CUSTOMER_ID] = client_config.customer_id
        if isinstance(client_config.auth, ApiKeyAuthConfig):
            os.environ[EnvConfigLoader.ENV_API_KEY] = client_config.auth.api_key
        elif isinstance(client_config.auth, OAuth2AuthConfig):
            os.environ[EnvConfigLoader.ENV_OAUTH2_CLIENT_ID] = client_config.auth.app_client_id
            os.environ[EnvConfigLoader.ENV_OAUTH2_CLIENT_SECRET] = client_config.auth.app_client_secret

        try:
            factory = Factory()
            self._test_factory_auth(factory, "env")
        finally:
            if isinstance(client_config.auth, ApiKeyAuthConfig):
                del os.environ[EnvConfigLoader.ENV_API_KEY]
            elif isinstance(client_config.auth, OAuth2AuthConfig):
                del os.environ[EnvConfigLoader.ENV_OAUTH2_CLIENT_ID]
                del os.environ[EnvConfigLoader.ENV_OAUTH2_CLIENT_SECRET]

    def test_explicit_typed(self):
        client_config = HomeConfigLoader().load()
        factory = Factory(config=client_config)
        self._test_factory_auth(factory, "explicit_typed")

    def test_explicit_dict(self):
        client_config = HomeConfigLoader().load().model_dump()
        factory = Factory(config=client_config)
        self._test_factory_auth(factory, "explicit_dict")


if __name__ == '__main__':
    unittest.main()
