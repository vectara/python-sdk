
from vectara.factory import Factory
from vectara.corpora.client import CorporaClient
from vectara.managers.corpus import CreateCorpusRequest
from vectara.client import Vectara
from vectara.utils import LabHelper
from unittest.mock import MagicMock
from vectara.config import ClientConfig, HomeConfigLoader, ApiKeyAuthConfig

import unittest
import logging
import json

import time

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

        client = Factory(config_json=json.dumps(foo_config)).build()
        target = client.lab_helper

        def create_request():
            return CreateCorpusRequest(name="filter-attributes", key="101-filter-attr")

        modified_request = CreateCorpusRequest(name="david - filter-attributes", key="david_101-filter-attr")

        # First test using our username discovery from operating system environment
        create_corpus_mock = MagicMock(return_value={"stub": True})
        target.corpus_manager.create_corpus = create_corpus_mock
        target.discover_user = MagicMock(return_value="david@vectara.com")
        target.create_lab_corpus(create_request())
        target.discover_user.assert_called_once_with()
        create_corpus_mock.assert_called_once_with(modified_request, delete_existing=True)

        # Second test using injected username prefix
        create_corpus_mock = MagicMock(return_value={"stub": True})
        target.corpus_manager.create_corpus = create_corpus_mock
        target.create_lab_corpus(create_request(), username="howward.smith@vectara.com")

        modified_request = CreateCorpusRequest(name="howwardSmith - filter-attributes", key="howwardSmith_101-filter-attr")
        create_corpus_mock.assert_called_once_with(modified_request, delete_existing=True)

        # Third test with very long username!!
        create_corpus_mock = MagicMock(return_value={"stub": True})
        target.corpus_manager.create_corpus = create_corpus_mock
        target.create_lab_corpus(create_request(), username="what.a.very.long.username.too.long.some.would.say@vectara.com")

        modified_request = CreateCorpusRequest(name="whatAVeryLongUsernam - filter-attributes", key="whatAVeryLongUsernam_101-filter-attr")
        create_corpus_mock.assert_called_once_with(modified_request, delete_existing=True)

        # Fourth test with prefix disabled
        create_corpus_mock = MagicMock(return_value={"stub": True})
        target.corpus_manager.create_corpus = create_corpus_mock
        target.create_lab_corpus(create_request(), user_prefix=False)
        create_corpus_mock.assert_called_once_with(create_request(), delete_existing=True)


        #target.create_lab_corpus(create_request(), username="howward.smith@vectara.com", dry_run=True)

    def test_create_lab_corpus(self):
        client = Factory().build()
        target = client.lab_helper

        def create_request():
            return CreateCorpusRequest(name="filter-attributes", key="101-filter-attr")

        target.create_lab_corpus(create_request())


    def test_save_profile(self):
        target = HomeConfigLoader(profile="test_write")

        target.delete()

        self.assertFalse(target.has_profile())
        config = ClientConfig(customer_id="asdf", auth=ApiKeyAuthConfig(api_key="foo"))
        target.save(config)
        self.assertTrue(target.has_profile())