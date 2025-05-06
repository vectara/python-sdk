import os
from pathlib import Path
import yaml
import tempfile
import shutil

from vectara.factory import Factory
from vectara.config import HomeConfigLoader, ApiKeyAuthConfig, OAuth2AuthConfig, PathConfigLoader, EnvConfigLoader

import unittest
import logging


class FactoryConfigTest(unittest.TestCase):
    """
    This test depends on our YAML default config being defined.

    We use this to test various methods of injection.
    """
    test_config_path = None
    temp_home = None
    test_env_vars = {
        EnvConfigLoader.ENV_CUSTOMER_ID: "test_customer",
        EnvConfigLoader.ENV_API_KEY: "test_api_key",
        EnvConfigLoader.ENV_OAUTH2_CLIENT_ID: "test_client_id",
        EnvConfigLoader.ENV_OAUTH2_CLIENT_SECRET: "test_client_secret"
    }

    VECTARA_API_KEY = os.environ["VECTARA_API_KEY"]

    @classmethod
    def setUpClass(cls):
        """Set up test resources."""
        logging.basicConfig(format='%(asctime)s:%(name)-35s %(levelname)s:%(message)s', level=logging.INFO,
                            datefmt='%H:%M:%S %z')
        cls.logger = logging.getLogger(cls.__name__)
        
        # Create a temporary home directory for testing
        cls.temp_home = tempfile.mkdtemp()
        
        # Create .vec_auth.yaml in the temporary home directory
        home_config_path = Path(cls.temp_home) / ".vec_auth.yaml"
        test_config = {
            "default": {
                "customer_id": "test_customer",
                "auth": {
                    "api_key": "test_api_key",
                    "type": "api_key"
                }
            }
        }
        with open(home_config_path, 'w') as f:
            yaml.dump(test_config, f)
        
        # Set up test config path for explicit path tests
        cls.test_config_path = Path(__file__).parent.parent / "resources" / ".vec_auth.yaml"

    @classmethod
    def tearDownClass(cls):
        """Clean up test resources."""

        os.environ["VECTARA_API_KEY"] = cls.VECTARA_API_KEY

        try:
            if cls.temp_home and os.path.exists(cls.temp_home):
                # Remove the .vec_auth.yaml file first
                home_config_path = Path(cls.temp_home) / ".vec_auth.yaml"
                if home_config_path.exists():
                    home_config_path.unlink()
                
                # Then remove the temporary directory
                shutil.rmtree(cls.temp_home)
                cls.logger.info(f"Cleaned up temporary home directory: {cls.temp_home}")
        except Exception as e:
            cls.logger.error(f"Error cleaning up temporary home directory: {e}")

    def setUp(self):
        """Clean up test environment variables before each test."""
        # Remove test environment variables
        for key in self.test_env_vars:
            if key in os.environ:
                del os.environ[key]

        # Set HOME to our temporary directory
        self.original_home = os.environ.get('HOME')
        os.environ['HOME'] = self.temp_home

    def tearDown(self):
        """Restore original HOME environment variable."""
        if hasattr(self, 'original_home'):
            if self.original_home:
                os.environ['HOME'] = self.original_home
            else:
                del os.environ['HOME']

    def _test_factory_auth(self, target: Factory, expected_method: str):
        client = target.build()
        self.assertEqual(expected_method, target.load_method)

    def test_default_load(self):
        # With no config_path and no environment variables, it should use "path_home"
        factory = Factory()
        self._test_factory_auth(factory, "path_home")

    def test_env_load(self):
        # With environment variables set, it should use "env"
        os.environ[EnvConfigLoader.ENV_CUSTOMER_ID] = self.test_env_vars[EnvConfigLoader.ENV_CUSTOMER_ID]
        os.environ[EnvConfigLoader.ENV_API_KEY] =   self.test_env_vars[EnvConfigLoader.ENV_API_KEY]
        
        factory = Factory()
        self._test_factory_auth(factory, "env")

    def test_explicit_path(self):
        # With config_path specified, it should use "path_explicit"
        factory = Factory(config_path=str(self.test_config_path))
        self._test_factory_auth(factory, "path_explicit")

    def test_explicit_typed(self):
        # With explicit typed config, it should use "explicit_typed"
        client_config = PathConfigLoader(config_path=str(self.test_config_path)).load()
        factory = Factory(config=client_config)
        self._test_factory_auth(factory, "explicit_typed")

    def test_explicit_dict(self):
        # With explicit dict config, it should use "explicit_dict"
        client_config = PathConfigLoader(config_path=str(self.test_config_path)).load().model_dump()
        factory = Factory(config=client_config)
        self._test_factory_auth(factory, "explicit_dict")

