from vectara.corpora.client import CorporaClient
from vectara.managers.corpus import CreateCorpusRequest
from vectara.client import Vectara
from unittest.mock import MagicMock
from vectara.factory import Factory

import unittest
import logging

class CorpusManagerTest(unittest.TestCase):
    client = None
    created_corpora = None

    @classmethod
    def setUpClass(cls):
        """Set up test resources."""
        logging.basicConfig(format='%(asctime)s:%(name)-35s %(levelname)s:%(message)s', level=logging.INFO, datefmt='%H:%M:%S %z')
        cls.logger = logging.getLogger(cls.__name__)
        cls.client = Factory().build()
        cls.created_corpora = set()

    def test_find_corpora_by_name_no_match(self):
        found = self.client.corpus_manager.find_corpora_by_name("company_names")
        self.assertEqual(len(found), 0)

    def test_find_corpora_by_name_match(self):
        request = CreateCorpusRequest.model_validate(
            {
                "key": "company_names_document",
                "name": "company_names_document",
                "description": "Test corpus for finding by name"
            })
        response = self.client.corpus_manager.create_corpus(request, delete_existing=True)
        self.created_corpora.add(response.key)

        # Search for the corpus
        found = self.client.corpus_manager.find_corpora_by_name("company_names_document")
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].name, "company_names_document")

    def test_create_corpus(self):
        request = CreateCorpusRequest.model_validate(
            {
                "key": "test-sdk-corpus",
                "name": "test-sdk-corpus",
                "description": "Our first test corpus from the SDK"
            })
        response = self.client.corpus_manager.create_corpus(request, delete_existing=True)
        self.created_corpora.add(response.key)

    @classmethod
    def tearDownClass(cls):
        """Clean up test resources."""
        for corpus_key in cls.created_corpora:
            try:
                cls.client.corpora.delete(corpus_key)
            except Exception as e:
                cls.logger.error(f"Failed to delete corpus {corpus_key}: {e}")

