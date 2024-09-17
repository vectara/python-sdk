from vectara.corpora.client import CorporaClient
from vectara.managers.corpus import CreateCorpusRequest
from vectara.client import Vectara
from unittest.mock import MagicMock
from vectara.factory import Factory

import time
import unittest
import logging

class CorpusManagerTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.basicConfig(format='%(asctime)s:%(name)-35s %(levelname)s:%(message)s', level=logging.INFO, datefmt='%H:%M:%S %z')
        self.logger = logging.getLogger(self.__class__.__name__)


    def test_find_corpora_by_name_no_match(self):
        client = Factory().build()

        found = client.corpus_manager.find_corpora_by_name("company_names")
        self.assertEqual(len(found), 0)

    def test_find_corpora_by_name_match(self):
        client = Factory().build()

        found = client.corpus_manager.find_corpora_by_name("company_names_document")
        self.assertEqual(len(found), 1)

    def test_create_corpus(self):
        client = Factory().build()

        request = CreateCorpusRequest.model_validate(
            {
                "key": "test-sdk-corpus",
                "name": "test-sdk-corpus",
                "description": "Our first test corpus from the SDK"
            })
        client.corpus_manager.create_corpus(request, delete_existing=True)

