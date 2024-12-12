from unittest import TestCase

from vectara import CoreDocument, CoreDocumentPart
from vectara.factory import Factory


class TestDocument(TestCase):

    def setUp(self):
        self.addCleanup(self.cleanup)
        self.client = Factory().build()
        response = self.client.corpora.create(name="test-document-manager", key="test-document-manager")
        self.key = response.key

    def test_add_document(self):
        document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="test-doc-part-1",
                )
            ],
        )
        response = self.client.documents.create(self.key, request=document)

        self.assertEqual(response.id, "my-doc-id")

    def test_delete_document(self):
        document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="test-doc-part-1",
                )
            ],
        )
        self.client.documents.create(self.key, request=document)

        response = self.client.documents.delete(self.key, "my-doc-id")

        self.assertIsNone(response)

    def test_get_document(self):
        document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="test-doc-part-1",
                )
            ],
        )
        self.client.documents.create(self.key, request=document)

        response = self.client.documents.get_corpus_document(self.key, "my-doc-id")

        self.assertEqual(response.id, "my-doc-id")

    def test_list_documents(self):
        doc_ids = []
        for index in range(2):
            document = CoreDocument(
                id=f"my-doc-id-{index}",
                document_parts=[
                    CoreDocumentPart(
                        text="test-doc-part-1",
                    )
                ],
            )
            response = self.client.documents.create(self.key, request=document)
            doc_ids.append(response.id)

        response = self.client.documents.list(self.key)
        for doc in response:
            self.assertIn(doc.id, doc_ids)

    def cleanup(self):
        response = self.client.corpora.list()
        for corpora in response:
            self.client.corpora.delete(corpora.key)

    def tearDown(self):
        response = self.client.corpora.list()
        for corpora in response:
            self.client.corpora.delete(corpora.key)
