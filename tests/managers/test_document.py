# type: ignore
from unittest.mock import Mock, patch

from vectara import VectaraEnvironment
from vectara.documents.client import DocumentsClient
from vectara.managers.document import DocumentManager
from vectara.core.client_wrapper import SyncClientWrapper
from vectara.utils.hash import calculate_sha256
from vectara.types import Document
from httpx import Client

import unittest


class MockSyncClientWrapper(SyncClientWrapper):

    def __init__(self):
        super().__init__(environment=VectaraEnvironment.PRODUCTION, httpx_client=Client())


class DocumentManagerTest(unittest.TestCase):

    @patch("vectara.documents.client.DocumentsClient.list")
    def test_check_exists(self, mock_list: patch):
        doc_client_dep = DocumentsClient(client_wrapper=MockSyncClientWrapper())
        target = DocumentManager(doc_client_dep)

        mock_list.return_value = iter([])

        result = target.check_exists("corpus_key", "ABC")
        self.assertFalse(result)  # add assertion here

        mock_list.return_value = iter([Document.model_validate({"id": "ABC"})])
        result = target.check_exists("corpus_key", "ABC")
        self.assertEqual(result.id, "ABC")  # add assertion here


    @patch("vectara.documents.client.DocumentsClient.list")
    def test_check_same(self, mock_list: patch):

        doc_client_dep = DocumentsClient(client_wrapper=MockSyncClientWrapper())
        target = DocumentManager(doc_client_dep)
        example_content = "some content".encode()

        # Test a document without a SHA1 Hash
        mock_list.return_value = iter([Document.model_validate({"metadata": {}})])
        exists, result = target.check_same("corpus_key", "ABC", example_content)
        self.assertFalse(result)  # add assertion here

        # Test a document with a different hash
        mock_list.return_value = iter([Document.model_validate({"metadata": {"sha256": "abcd"}})])
        exists, result = target.check_same("corpus_key", "ABC", example_content)
        self.assertFalse(result)

        # Test same document with same hash recorded matches
        created_hash = calculate_sha256(example_content)
        mock_list.return_value = iter([Document.model_validate({"metadata": {"sha256": created_hash}})])
        exists, result = target.check_same("corpus_key", "ABC", example_content)
        self.assertTrue(result, "We were expecting documents to be same but were not")

        # Test invalid metadata
        mock_list.return_value = iter([Document.model_validate({"metadata": {"sha256": created_hash, "animal": "dog"}})])
        exists, result = target.check_same("corpus_key", "ABC", example_content, metadata={"animal": "cat"})
        self.assertFalse(result, "We were expecting documents to be different, animal = dog vs cat")

        mock_list.return_value = iter([Document.model_validate({"metadata": {"sha256": created_hash, "animal": "cat"}})])
        exists, result = target.check_same("corpus_key", "ABC", example_content, metadata={"animal": "cat"})
        self.assertTrue(result, "We were expecting documents to be same, animal = cat")


if __name__ == '__main__':
    unittest.mock
