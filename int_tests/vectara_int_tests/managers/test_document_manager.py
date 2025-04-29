from vectara.corpora.client import CorporaClient
from vectara.managers.corpus import CreateCorpusRequest
from vectara.managers.document import DocOpEnum
from vectara.types import StructuredDocument
from vectara.client import Vectara
from unittest.mock import MagicMock
from vectara.factory import Factory
#from vectara.utils.httpx_logging import dump_all_requests
from pathlib import Path
import time
import unittest
import logging
import json
import urllib

class DocumentManagerTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.basicConfig(format='%(asctime)s:%(name)-35s %(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%H:%M:%S %z')
        self.logger = logging.getLogger(self.__class__.__name__)

    def test_upsert(self):
        self.logger.info("Testing Doc Upload with Upsert")
        client = Factory().build()

        request = CreateCorpusRequest(name="int-test-doc-upsert1", key="int-test-doc-upsert1")
        create_response = client.lab_helper.create_lab_corpus(request)
        key = create_response.key

        # Sleep for 30 seconds, let caches expire otherwise Documents service can give 404 error (Corpus not found).
        #time.sleep(30)

        doc = StructuredDocument.model_validate({
            "id": "abc",
            "sections": [
                {"text": "Some important text"}
            ]
        })

        response = client.document_manager.index_doc(key, doc)
        self.assertEqual(DocOpEnum.CREATED, response)

        response = client.document_manager.index_doc(key, doc)
        self.assertEqual(DocOpEnum.IGNORED, response)

        doc = StructuredDocument.model_validate({
            "id": "abc",
            "sections": [
                {"text": "Some important text which is now changed"}
            ]
        })

        response = client.document_manager.index_doc(key, doc)
        self.assertEqual(DocOpEnum.UPDATED, response)


