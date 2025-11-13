import unittest
import os
import time

from vectara import Vectara
from vectara.core import RequestOptions
from vectara import CoreDocument, CoreDocumentPart, SearchCorporaParameters, KeyedSearchCorpus, \
    ContextConfiguration, CustomerSpecificReranker, GenerationParameters, CitationParameters, \
    QueryStreamedResponse, QueryFullResponse, MmrReranker, NoneReranker, UserFunctionReranker, \
    ChainReranker


class TestMultipleCorporaQuery(unittest.TestCase):
    client = None
    corpus_names = None
    test_documents = None

    TEST_DOCUMENT_1 = CoreDocument(
        id="my-doc-id",
        document_parts=[
            CoreDocumentPart(
                text="Robot Utility Models are trained on a diverse set of environments and objects, and then can "
                     "be deployed in novel environments with novel objects without any further data or training.",
            )
        ],
    )

    TEST_DOCUMENT_2 = CoreDocument(
        id="my-doc-id",
        document_parts=[
            CoreDocumentPart(
                text="We show that it is possible to create general Robot Utility Models with a moderate amount "
                     "of data in the order of 1,000 demonstrations (Section 2). These RUMs achieve a 90% average "
                     "success rate on zero-shot deployment in 25 novel environments (Section 3.1).",
            )
        ],
    )

    @classmethod
    def setUpClass(cls):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        cls.client = Vectara(api_key=api_key)
        cls.request_options = RequestOptions(timeout_in_seconds=100)
        cls.generation_params = GenerationParameters(
            response_language="eng",
            citations=CitationParameters(style="none"),
            enable_factual_consistency_score=False,
        )

        # Create corpora with unique names to avoid conflicts
        timestamp = int(time.time())
        cls.corpus_names = [f"test-query-corpus-1-{timestamp}", f"test-query-corpus-2-{timestamp}"]
        cls.test_documents = [cls.TEST_DOCUMENT_1, cls.TEST_DOCUMENT_2]

        for corpus_name, document in zip(cls.corpus_names, cls.test_documents):
            cls.client.corpora.create(name=corpus_name, key=corpus_name)
            # Small wait for corpus to be fully provisioned
            time.sleep(2)
            cls.client.documents.create(corpus_name, request=document)

    def setUp(self):
        # Create default search parameters
        self.search_params = self._create_search_params(
            lexical_interpolation=1,
            reranker=CustomerSpecificReranker(reranker_id="rnk_272725719")
        )

    def _create_search_params(self, lexical_interpolation=0, reranker=None):
        """Helper method to create search parameters with given interpolation and reranker."""
        return SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key=corpus_name,
                    metadata_filter="",
                    lexical_interpolation=lexical_interpolation,
                )
                for corpus_name in self.corpus_names
            ],
            context_configuration=ContextConfiguration(
                sentences_before=2,
                sentences_after=2,
            ),
            reranker=reranker,
        )

    def _assert_query_response(self, response):
        """Helper method to assert common response properties."""
        self.assertIsInstance(response, QueryFullResponse)
        self.assertIsNotNone(response.summary)
        self.assertGreater(len(response.search_results), 0)

    def test_query(self):
        response = self.client.query(
            query="Robot Utility Models",
            search=self.search_params,
            generation=self.generation_params,
            request_options=self.request_options
        )
        self._assert_query_response(response)

    def test_query_with_different_lambda(self):
        # Test with lexical_interpolation=0
        search = self._create_search_params(
            lexical_interpolation=0,
            reranker=CustomerSpecificReranker(reranker_id="rnk_272725719")
        )
        response = self.client.query(
            query="Robot Utility Models",
            search=search,
            generation=self.generation_params,
            request_options=self.request_options
        )
        self._assert_query_response(response)

        # Test with lexical_interpolation=0.1
        search = self._create_search_params(
            lexical_interpolation=0.1,
            reranker=CustomerSpecificReranker(reranker_id="rnk_272725719")
        )
        response = self.client.query(
            query="Robot Utility Models",
            search=search,
            generation=self.generation_params,
            request_options=self.request_options
        )
        self._assert_query_response(response)

    def test_query_with_mmr_reranker(self):
        search = self._create_search_params(
            lexical_interpolation=0,
            reranker=MmrReranker(diversity_bias=0.3)
        )
        response = self.client.query(
            query="Robot Utility Models",
            search=search,
            generation=self.generation_params,
            request_options=self.request_options
        )
        self._assert_query_response(response)

    def test_query_with_none_reranker(self):
        search = self._create_search_params(
            lexical_interpolation=0,
            reranker=NoneReranker()
        )
        response = self.client.query(
            query="Robot Utility Models",
            search=search,
            generation=self.generation_params,
            request_options=self.request_options
        )
        self._assert_query_response(response)

    def test_query_with_udf_reranker(self):
        search = self._create_search_params(
            lexical_interpolation=0,
            reranker=UserFunctionReranker(
                user_function="if (get('$.score') < 0.7) null else get('$.score') + 1"
            )
        )
        response = self.client.query(
            query="Robot Utility Models",
            search=search,
            generation=self.generation_params,
            request_options=self.request_options
        )
        self.assertIsInstance(response, QueryFullResponse)
        for result in response.search_results:
            self.assertGreater(result.score, 1)

    def test_query_with_chain_reranker(self):
        search = self._create_search_params(
            lexical_interpolation=0,
            reranker=ChainReranker(
                rerankers=[
                    CustomerSpecificReranker(reranker_id="rnk_272725719"),
                    UserFunctionReranker(
                        user_function="if (get('$.score') < 0.7) null else get('$.score') + 1"
                    ),
                ]
            )
        )
        response = self.client.query(
            query="Robot Utility Models",
            search=search,
            generation=self.generation_params,
            request_options=self.request_options
        )
        self.assertIsInstance(response, QueryFullResponse)
        for result in response.search_results:
            self.assertGreater(result.score, 1)

    def test_query_with_fcs_enabled(self):
        generation_params = GenerationParameters(
            response_language="eng",
            citations=CitationParameters(style="none"),
            enable_factual_consistency_score=True,
        )
        response = self.client.query(
            query="Robot Utility Models",
            search=self.search_params,
            generation=generation_params,
            request_options=self.request_options
        )
        self._assert_query_response(response)

    def test_query_stream(self):
        response = self.client.query_stream(
            query="Robot Utility Models",
            search=self.search_params,
            generation=self.generation_params,
            request_options=self.request_options
        )
        response = list(response)
        self.assertGreater(len(response), 0)
        for item in response:
            self.assertTrue(
                hasattr(item, 'type') or 
                hasattr(item, 'value') or 
                hasattr(item, 'generation_id'),
                f"Streamed response item {item} doesn't have expected attributes"
            )

    @classmethod
    def tearDownClass(cls):
        """Clean up all test resources."""
        for corpus_name in cls.corpus_names:
            try:
                cls.client.corpora.delete(corpus_name)
            except Exception:
                pass
