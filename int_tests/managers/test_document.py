import unittest
import os
import time

from vectara import Vectara, CoreDocument, CoreDocumentPart


class TestDocument(unittest.TestCase):
    client = None
    corpus_key = None
    created_corpora = None
    created_documents = None

    @classmethod
    def setUpClass(cls):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        
        cls.client = Vectara(api_key=api_key)
        cls.created_corpora = set()
        cls.created_documents = set()

        # Create test corpus
        response = cls.client.corpora.create(name="test-document-manager", key="test-document-manager")
        cls.corpus_key = response.key
        cls.created_corpora.add(cls.corpus_key)

    def _create_document(self, doc_id: str, text: str = "test-doc-part-1") -> str:
        """Helper method to create a document with given parameters."""
        document = CoreDocument(
            id=doc_id,
            document_parts=[
                CoreDocumentPart(
                    text=text,
                )
            ],
        )
        response = self.client.documents.create(self.corpus_key, request=document)
        self.created_documents.add((self.corpus_key, doc_id))
        return response.id

    def test_add_document(self):
        doc_id = self._create_document("my-doc-id")
        self.assertEqual(doc_id, "my-doc-id")

    def test_delete_document(self):
        doc_id = self._create_document("test-delete-my-doc")
        response = self.client.documents.delete(self.corpus_key, doc_id)
        self.assertIsNone(response)
        self.created_documents.remove((self.corpus_key, doc_id))

    def test_get_document(self):
        doc_id = self._create_document("test-get-my-doc")
        response = self.client.documents.get(self.corpus_key, doc_id)
        self.assertEqual(response.id, doc_id)

    def test_list_documents(self):
        # Create test documents
        doc_ids = []
        for index in range(2):
            doc_id = self._create_document(f"my-doc-id-{index}")
            doc_ids.append(doc_id)

        # Wait for documents to be indexed
        time.sleep(10) 

        # Get all documents and verify our created documents are in the list
        found_ids = set()
        for page in self.client.documents.list(self.corpus_key).iter_pages():
            for doc in page:
                if doc.id in doc_ids:
                    found_ids.add(doc.id)
            if found_ids == set(doc_ids):
                break

        self.assertEqual(found_ids, set(doc_ids))

    def test_update_metadata(self):
        doc_id = self._create_document("test-update-metadata")
        metadata = {
            "title": "Test Document",
            "author": "Test Author",
            "category": "Test Category"
        }
        response = self.client.documents.update_metadata(
            corpus_key=self.corpus_key,
            document_id=doc_id,
            metadata=metadata
        )
        self.assertEqual(response.id, doc_id)
        self.assertEqual(response.metadata, metadata)

    def test_summarize(self):
        doc_id = self._create_document(
            "test-summarize",
            text="""Robot Utility Models are trained on a diverse set of environments and objects, and then can
                 be deployed in novel environments with novel objects without any further data or training."""
        )
        response = self.client.documents.summarize(
            corpus_key=self.corpus_key,
            document_id=doc_id,
            llm_name="gpt-3.5-turbo"
        )
        self.assertIsNotNone(response.summary)
        self.assertGreater(len(response.summary), 0)

    @classmethod
    def tearDownClass(cls):
        """Clean up all test resources."""
        # Clean up documents
        for corpus_key, doc_id in cls.created_documents:
            try:
                cls.client.documents.delete(corpus_key, doc_id)
            except Exception:
                pass

        # Clean up corpora
        for corpus_key in cls.created_corpora:
            try:
                cls.client.corpora.delete(corpus_key)
            except Exception:
                pass
