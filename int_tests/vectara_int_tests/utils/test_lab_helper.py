from vectara.factory import Factory
from vectara.managers.corpus import CreateCorpusRequest
from unittest.mock import patch
from vectara.config import ClientConfig, HomeConfigLoader, ApiKeyAuthConfig, PathConfigLoader
import os
from pathlib import Path
import yaml

import unittest
import logging


class LabHelperTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.basicConfig(format='%(asctime)s:%(name)-35s %(levelname)s:%(message)s', level=logging.INFO, datefmt='%H:%M:%S %z')
        self.logger = logging.getLogger(self.__class__.__name__)


    def test_create_lab_corpus_name(self):

        # Creates a "foo" config useful for testing without performing OAuth in a unittest environment
        foo_config = {
            "customer_id": "asdf",
            "auth": {
                "api_key": "foo"
            }
        }

        client = Factory(config=foo_config).build()
        target = client.lab_helper

        def create_request():
            return CreateCorpusRequest(name="filter-attributes", key="101-filter-attr", user_prefix=False)

        # First test using our username discovery from operating system environment
        with patch.object(target, '_discover_user', return_value="david@vectara.com") as mock_discover_user, \
             patch.object(target.corpus_manager, 'create_corpus', return_value={"stub": True}) as mock_create_corpus:
            
            target.create_lab_corpus(create_request())
            
            mock_discover_user.assert_called_once()
            mock_create_corpus.assert_called_once()
            self.assertEqual(mock_create_corpus.call_args[0][0].name, "david - filter-attributes")
            self.assertEqual(mock_create_corpus.call_args[0][0].key, "david_101-filter-attr")

        # Second test using injected username prefix
        with patch.object(target.corpus_manager, 'create_corpus', return_value={"stub": True}) as mock_create_corpus:
            target.create_lab_corpus(create_request(), username="howward.smith@vectara.com")
            
            mock_create_corpus.assert_called_once()
            self.assertEqual(mock_create_corpus.call_args[0][0].name, "howwardSmith - filter-attributes")
            self.assertEqual(mock_create_corpus.call_args[0][0].key, "howwardSmith_101-filter-attr")

        # Third test with very long username
        with patch.object(target.corpus_manager, 'create_corpus', return_value={"stub": True}) as mock_create_corpus:
            target.create_lab_corpus(create_request(), username="what.a.very.long.username.too.long.some.would.say@vectara.com")
            
            mock_create_corpus.assert_called_once()
            self.assertEqual(mock_create_corpus.call_args[0][0].name, "whatAVeryLongUsernam - filter-attributes")
            self.assertEqual(mock_create_corpus.call_args[0][0].key, "whatAVeryLongUsernam_101-filter-attr")

        # Fourth test with prefix disabled
        with patch.object(target.corpus_manager, 'create_corpus', return_value={"stub": True}) as mock_create_corpus:
            target.create_lab_corpus(create_request(), user_prefix=False)
            
            mock_create_corpus.assert_called_once()
            self.assertEqual(mock_create_corpus.call_args[0][0].name, "filter-attributes")
            self.assertEqual(mock_create_corpus.call_args[0][0].key, "101-filter-attr")


    def test_save_profile(self):
        # Use the existing resources directory from the utils sibling directory
        test_config_path = Path(__file__).parent.parent / "resources" / ".vec_auth.yaml"
        
        target = PathConfigLoader(config_path=str(test_config_path), profile="test_write")

        # First save the profile
        config = ClientConfig(customer_id="asdf", auth=ApiKeyAuthConfig(api_key="foo"))
        target._save(config, test_config_path)
        
        # Verify it exists by loading the YAML file
        with open(test_config_path, 'r') as f:
            config_data = yaml.safe_load(f)
            self.assertIn("test_write", config_data)
            self.assertEqual(config_data["test_write"]["customer_id"], "asdf")
            self.assertEqual(config_data["test_write"]["auth"]["api_key"], "foo")
        
        # Delete it
        target._delete(test_config_path)
        
        # Verify it's gone by checking the YAML file
        with open(test_config_path, 'r') as f:
            config_data = yaml.safe_load(f)
            self.assertNotIn("test_write", config_data)