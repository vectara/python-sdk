import unittest
import os
import time
from typing import Optional, List

from vectara import Vectara, FilterAttribute, CorpusCustomDimension, CoreDocument, CoreDocumentPart, \
    ContextConfiguration, CustomerSpecificReranker, GenerationParameters, \
    CitationParameters, SearchCorpusParameters
from vectara.core import RequestOptions


class TestCorporaManager(unittest.TestCase):
    client = None
    created_corpora = None

    @classmethod
    def setUpClass(cls):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        
        cls.client = Vectara(api_key=api_key)
        cls.created_corpora = set()

    def _create_corpus(self, key: str, name: Optional[str] = None, description: Optional[str] = None, 
                      filter_attributes: Optional[List[FilterAttribute]] = None) -> str:
        """Helper method to create a corpus with given parameters."""
        if name is None:
            name = key
        response = self.client.corpora.create(
            key=key,
            name=name,
            description=description,
            filter_attributes=filter_attributes
        )
        self.created_corpora.add(key)
        return key

    def _wait_for_corpus(self, corpus_key: str, timeout: int = 60):
        """Helper method to wait for corpus operations to complete."""
        import time
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                corpus = self.client.corpora.get(corpus_key)
                if corpus:
                    return
            except Exception:
                pass
            time.sleep(5)
        raise TimeoutError(f"Corpus {corpus_key} not ready after {timeout} seconds")

    def test_create_corpora(self):
        filter_attributes = FilterAttribute(
            name="Title",
            level="document",
            description="The title of the document.",
            indexed=True,
            type="text"
        )
        custom_dimensions = CorpusCustomDimension(
            name="importance",
            description="Product importance.",
            indexing_default=0,
            querying_default=0
        )
        
        corpus_key = self._create_corpus(
            key="test-create-corpus",
            description="test description",
            filter_attributes=[filter_attributes]
        )
        
        corpus = self.client.corpora.get(corpus_key)
        self.assertEqual(corpus.key, "test-create-corpus")
        self.assertEqual(corpus.name, "test-create-corpus")
        self.assertEqual(corpus.description, "test description")
        self.assertEqual(corpus.filter_attributes, [filter_attributes])

    def test_list_corpora(self):
        # Create test corpora
        corpus_keys = []
        for i in range(2):
            corpus_key = self._create_corpus(key=f"corpus-{i}")
            corpus_keys.append(corpus_key)

        # Verify corpora are in the list
        found_keys = set()
        for page in self.client.corpora.list().iter_pages():
            for corpus in page:
                if corpus.key in corpus_keys:
                    found_keys.add(corpus.key)
            if found_keys == set(corpus_keys):
                break

        self.assertEqual(found_keys, set(corpus_keys))

    def test_delete_corpora(self):
        corpus_key = self._create_corpus(key="test-delete-corpus")
        
        self.client.corpora.delete(corpus_key=corpus_key)
        self.created_corpora.remove(corpus_key)
        
        # Verify corpus is deleted
        found = False
        for page in self.client.corpora.list().iter_pages():
            for corpus in page:
                if corpus.key == corpus_key:
                    found = True
                    break
            if found:
                break
        self.assertFalse(found)

    def test_update_corpora(self):
        corpus_key = self._create_corpus(key="test-update-corpus")
        
        response = self.client.corpora.update(
            corpus_key,
            name="updated-name",
            description="updated-description"
        )
        
        self.assertEqual(response.description, "updated-description")
        self.assertEqual(response.name, "updated-name")

    def test_get_metadata_of_corpora(self):
        corpus_key = self._create_corpus(
            key="test-get-metadata",
            description="test-description",
            name="Test"
        )
        
        corpus = self.client.corpora.get(corpus_key)
        self.assertEqual(corpus.key, "test-get-metadata")
        self.assertEqual(corpus.name, "Test")
        self.assertEqual(corpus.description, "test-description")

    def test_corpus_reset(self):
        corpus_key = self._create_corpus(key="test-reset-corpus")
        
        # Add document
        document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="I'm a nice document part.",
                )
            ],
        )
        self.client.documents.create(corpus_key, request=document)
        time.sleep(30)
        # Verify document was added
        documents = list(self.client.documents.list(corpus_key))
        self.assertEqual(len(documents), 1)

        # Reset corpus
        self.client.corpora.reset(corpus_key)
        
        # Verify document was removed
        documents = list(self.client.documents.list(corpus_key))
        self.assertEqual(len(documents), 0)

    def test_replace_filter_attributes(self):
        corpus_key = self._create_corpus(key="test-reset-filters")
        
        filter_attributes = FilterAttribute(
            name="Title",
            level="document",
            description="The title of the document.",
            indexed=True,
            type="text"
        )
        res = self.client.corpora.replace_filter_attributes(
            corpus_key,
            filter_attributes=[filter_attributes]
        )
        self.assertIsNotNone(res.job_id)

    def test_search(self):
        corpus_key = self._create_corpus(name="test-search", key="test-search")
        
        document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="Robot Utility Models are trained on a diverse set of environments and objects, and then can "
                         "be deployed in novel environments with novel objects without any further data or training.",
                )
            ],
        )
        self.client.documents.create(corpus_key, request=document)
        
        response = self.client.corpora.search(corpus_key=corpus_key, query="Robot Utility Models")
        self.assertIsNone(response.summary)
        self.assertGreater(len(response.search_results), 0)

    def test_query(self):
        corpus_key = self._create_corpus(name="test-query", key="test-query")
        
        document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="Robot Utility Models are trained on a diverse set of environments and objects, and then can "
                         "be deployed in novel environments with novel objects without any further data or training.",
                )
            ],
        )
        self.client.documents.create(corpus_key, request=document)
        
        search_params = SearchCorpusParameters(
            context_configuration=ContextConfiguration(
                sentences_before=2,
                sentences_after=2,
            ),
            reranker=CustomerSpecificReranker(
                reranker_id="rnk_272725719"
            ),
        )
        generation_params = GenerationParameters(
            response_language="eng",
            citations=CitationParameters(
                style="none",
            ),
            enable_factual_consistency_score=True,
        )
        request_options = RequestOptions(timeout_in_seconds=100)

        response = self.client.corpora.query(
            corpus_key=corpus_key,
            search=search_params,
            query="Robot Utility Models",
            generation=generation_params,
            request_options=request_options
        )
        self.assertIsNotNone(response.summary)
        self.assertGreater(len(response.search_results), 0)

    @classmethod
    def tearDownClass(cls):
        """Clean up all test resources."""
        for corpus_key in cls.created_corpora:
            try:
                cls.client.corpora.delete(corpus_key)
            except Exception:
                pass
