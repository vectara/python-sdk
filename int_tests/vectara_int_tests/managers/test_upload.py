from vectara.corpora.client import CorporaClient
from vectara.managers.corpus import CreateCorpusRequest
from vectara.client import Vectara
from vectara.types import Document
from unittest.mock import MagicMock
from vectara.factory import Factory
#from vectara.utils.httpx_logging import dump_all_requests
from pathlib import Path
import time
import unittest
import logging
import json
import urllib

class UploadManagerTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.basicConfig(format='%(asctime)s:%(name)-35s %(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%H:%M:%S %z')
        self.logger = logging.getLogger(self.__class__.__name__)

    def test_upload(self):
        """
        The following test was written to bypass Fern to debug the HTTP upload without any additional abstraction.

        This is useful when we are trying to isolate an issue in Fern or the API as multipart form is hard to
        write test harnesses for.

        :return:
        """
        self.logger.info("Testing upload via manager (bypass Fern)")
        client = Factory().build()

        request = CreateCorpusRequest(name="int-test-upload", key="int-test-upload")
        create_response = client.lab_helper.create_lab_corpus(request)
        key = create_response.key

        time.sleep(30)
        path = Path("examples/01_getting_started/resources/arxiv/2409.05866v1.pdf")
        document: Document = client.upload_manager.upload(key, path, metadata={"key": "value"}, doc_id="basic_metadata")
        self.assertTrue(document.storage_usage.bytes_used > 0)
        self.assertTrue(document.storage_usage.metadata_bytes_used > 0)

    def test_delete_all_tests(self):
        self.logger.info("Deleting all tests")
        client = Factory().build()
        # TODO Refactor tests so they use username prefix like labs.
        client.lab_helper.delete_labs("int-test-", user_prefix=False)


