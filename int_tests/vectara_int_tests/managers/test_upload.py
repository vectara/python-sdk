from vectara.corpora.client import CorporaClient
from vectara.managers.corpus import CreateCorpusRequest
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

class UploadManagerTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.basicConfig(format='%(asctime)s:%(name)-35s %(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%H:%M:%S %z')
        self.logger = logging.getLogger(self.__class__.__name__)

    def test_upload_fern(self):
        self.logger.info("Testing Fern Upload (no metadata)")
        client = Factory().build()

        request = CreateCorpusRequest(name="int-test-upload-fern", key="int-test-upload-fern")
        create_response = client.lab_helper.create_lab_corpus(request)
        key = create_response.key

        time.sleep(10)
        path = Path("examples/01_getting_started/resources/arxiv/2409.05865v1.pdf")
        with open(path, "rb") as f:
            content = f.read()
            doc = client.upload.file(key, file=("override-doc-id", content, "application/pdf"))

    def test_upload_fern_metadata(self):
        self.logger.info("Testing Fern Upload (metadata)")
        client = Factory().build()

        request = CreateCorpusRequest(name="int-test-upload-fern-metadata", key="int-test-upload-fern-metadata")
        create_response = client.lab_helper.create_lab_corpus(request)
        key = create_response.key

        time.sleep(10)
        path = Path("examples/01_getting_started/resources/arxiv/2409.05865v1.pdf")
        with open(path, "rb") as f:
            content = f.read()
            doc = client.upload.file(key, file=(path.name, content, "application/pdf"), metadata={"test_fern": "ok"})

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
        path = Path("examples/01_getting_started/resources/arxiv/2409.05865v1.pdf")
        response = client.upload_manager.upload(key, path)
        if response.status_code > 200:
            self.logger.error(f"Unexpected response code [{response.status_code}]: {response.content}")

        self.assertTrue(200 <= response.status_code < 300)

        #dump_all_requests(response)

    def test_delete_all_tests(self):
        self.logger.info("Deleting all tests")
        client = Factory().build()
        # TODO Refactor tests so they use username prefix like labs.
        client.lab_helper.delete_labs("int-test-", user_prefix=False)


