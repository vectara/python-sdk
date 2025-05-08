import unittest
import logging
import os
import time

from vectara.factory import Factory
from vectara.managers.corpus import CreateCorpusRequest
from vectara.managers.document import DocOpEnum
from vectara.types import StructuredDocument
from vectara.client import Vectara


class DocumentManagerTest(unittest.TestCase):
    corpus_key = None
    client = None

    @classmethod
    def setUpClass(cls):
        """Set up test resources."""
        logging.basicConfig(format='%(asctime)s:%(name)-35s %(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%H:%M:%S %z')
        cls.logger = logging.getLogger(cls.__name__)
        cls.client = Factory().build()

        request = CreateCorpusRequest(name="int-test-document-manager", key="int-test-document-manager")
        create_response = cls.client.lab_helper.create_lab_corpus(request, user_prefix=False)
        cls.corpus_key = create_response.key

    def test_upsert(self):
        self.logger.info("Testing Doc Upload with Upsert")

        doc = StructuredDocument.model_validate({
            "id": "abc",
            "sections": [
                {"text": "Some important text"}
            ]
        })

        response = self.client.document_manager.index_doc(self.corpus_key, doc)
        self.assertEqual(DocOpEnum.CREATED, response)
        # Wait for indexing to complete
        time.sleep(10)

        response = self.client.document_manager.index_doc(self.corpus_key, doc)
        self.assertEqual(DocOpEnum.IGNORED, response)
        # Wait for indexing to complete
        time.sleep(5)

        doc = StructuredDocument.model_validate({
            "id": "abc",
            "sections": [
                {"text": "Some important text which is now changed"}
            ]
        })

        response = self.client.document_manager.index_doc(self.corpus_key, doc)
        self.assertEqual(DocOpEnum.UPDATED, response)
        # Wait for indexing to complete
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        """Clean up test resources."""
        if cls.corpus_key:
            try:
                cls.client.corpora.delete(cls.corpus_key)
            except Exception as e:
                cls.logger.error(f"Failed to delete corpus {cls.corpus_key}: {e}")


