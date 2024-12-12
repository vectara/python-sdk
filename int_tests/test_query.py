import time
import unittest

from vectara.core import RequestOptions
from vectara.factory import Factory
from vectara import CoreDocument, CoreDocumentPart, SearchCorporaParameters, KeyedSearchCorpus, \
    ContextConfiguration, CustomerSpecificReranker, GenerationParameters, CitationParameters, \
    QueryStreamedResponse, QueryFullResponse, MmrReranker, NoneReranker, UserFunctionReranker, \
    ChainReranker


class TestMultipleCorporaQuery(unittest.TestCase):
    def setUp(self):
        self.addCleanup(self.cleanup)
        self.client = Factory().build()
        self.client.corpora.create(name="test-search-1", key="test-search-1")
        self.client.corpora.create(name="test-search-2", key="test-search-2")
        time.sleep(30)
        test_search_1_document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="Robot Utility Models are trained on a diverse set of environments and objects, and then can "
                         "be deployed in novel environments with novel objects without any further data or training.",
                )
            ],
        )

        test_search_2_document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="We show that it is possible to create general Robot Utility Models with a moderate amount "
                         "of data in the order of 1,000 demonstrations (Section 2). These RUMs achieve a 90% average "
                         "success rate on zero-shot deployment in 25 novel environments (Section 3.1).",
                )
            ],
        )
        self.client.documents.create("test-search-1", request=test_search_1_document)
        self.client.documents.create("test-search-2", request=test_search_2_document)

        self.search_params = SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key="test-search-1",
                    metadata_filter="",
                    lexical_interpolation=1,
                ),
                KeyedSearchCorpus(
                    corpus_key="test-search-2",
                    metadata_filter="",
                    lexical_interpolation=1,
                )
            ],
            context_configuration=ContextConfiguration(
                sentences_before=2,
                sentences_after=2,
            ),
            reranker=CustomerSpecificReranker(
                reranker_id="rnk_272725719"
            ),
        )
        self.generation_params = GenerationParameters(
            response_language="eng",
            citations=CitationParameters(
                style="none",
            ),
            enable_factual_consistency_score=False,
        )

        self.request_options = RequestOptions(timeout_in_seconds=100)

    def test_query(self):
        response = self.client.query(query="Robot Utility Models", search=self.search_params,
                                     generation=self.generation_params,
                                     request_options=self.request_options)
        self.assertIsInstance(response, QueryFullResponse)
        self.assertIsNotNone(response.summary)
        self.assertGreater(len(response.search_results), 0)

    def test_query_with_different_lambda(self):
        search = SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key="test-search-1",
                    metadata_filter="",
                    lexical_interpolation=0,
                ),
                KeyedSearchCorpus(
                    corpus_key="test-search-2",
                    metadata_filter="",
                    lexical_interpolation=0,
                )
            ],
            context_configuration=ContextConfiguration(
                sentences_before=2,
                sentences_after=2,
            ),
            reranker=CustomerSpecificReranker(
                reranker_id="rnk_272725719"
            ),
        )

        response = self.client.query(query="Robot Utility Models", search=search,
                                     generation=self.generation_params,
                                     request_options=self.request_options)
        self.assertIsInstance(response, QueryFullResponse)
        self.assertIsNotNone(response.summary)
        self.assertGreater(len(response.search_results), 0)

        search = SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key="test-search-1",
                    metadata_filter="",
                    lexical_interpolation=0.1,
                ),
                KeyedSearchCorpus(
                    corpus_key="test-search-2",
                    metadata_filter="",
                    lexical_interpolation=0.1,
                )
            ],
            context_configuration=ContextConfiguration(
                sentences_before=2,
                sentences_after=2,
            ),
            reranker=CustomerSpecificReranker(
                reranker_id="rnk_272725719"
            ),
        )

        response = self.client.query(query="Robot Utility Models", search=search,
                                     generation=self.generation_params,
                                     request_options=self.request_options)
        self.assertIsInstance(response, QueryFullResponse)
        self.assertIsNotNone(response.summary)
        self.assertGreater(len(response.search_results), 0)

    def test_query_with_mmr_reranker(self):
        search = SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key="test-search-1",
                    metadata_filter="",
                    lexical_interpolation=0,
                ),
                KeyedSearchCorpus(
                    corpus_key="test-search-2",
                    metadata_filter="",
                    lexical_interpolation=0,
                )
            ],
            context_configuration=ContextConfiguration(
                sentences_before=2,
                sentences_after=2,
            ),
            reranker=MmrReranker(
                diversity_bias=0.3
            ),
        )

        response = self.client.query(query="Robot Utility Models", search=search,
                                     generation=self.generation_params,
                                     request_options=self.request_options)
        self.assertIsInstance(response, QueryFullResponse)
        self.assertIsNotNone(response.summary)
        self.assertGreater(len(response.search_results), 0)

    def test_query_with_none_reranker(self):
        search = SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key="test-search-1",
                    metadata_filter="",
                    lexical_interpolation=0,
                ),
                KeyedSearchCorpus(
                    corpus_key="test-search-2",
                    metadata_filter="",
                    lexical_interpolation=0,
                )
            ],
            context_configuration=ContextConfiguration(
                sentences_before=2,
                sentences_after=2,
            ),
            reranker=NoneReranker(),
        )

        response = self.client.query(query="Robot Utility Models", search=search,
                                     generation=self.generation_params,
                                     request_options=self.request_options)
        self.assertIsInstance(response, QueryFullResponse)
        self.assertIsNotNone(response.summary)
        self.assertGreater(len(response.search_results), 0)

    def test_query_with_udf_reranker(self):
        search = SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key="test-search-1",
                    metadata_filter="",
                    lexical_interpolation=0,
                ),
                KeyedSearchCorpus(
                    corpus_key="test-search-2",
                    metadata_filter="",
                    lexical_interpolation=0,
                )
            ],
            context_configuration=ContextConfiguration(
                sentences_before=2,
                sentences_after=2,
            ),
            reranker=UserFunctionReranker(
                user_function="if (get('$.score') < 0.7) null else get('$.score') + 1"
            ),
        )

        response = self.client.query(query="Robot Utility Models", search=search,
                                     generation=self.generation_params,
                                     request_options=self.request_options)
        self.assertIsInstance(response, QueryFullResponse)
        for result in response.search_results:
            self.assertGreater(result.score, 1)

    def test_query_with_chain_reranker(self):
        search = SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key="test-search-1",
                    metadata_filter="",
                    lexical_interpolation=0,
                ),
                KeyedSearchCorpus(
                    corpus_key="test-search-2",
                    metadata_filter="",
                    lexical_interpolation=0,
                )
            ],
            context_configuration=ContextConfiguration(
                sentences_before=2,
                sentences_after=2,
            ),
            reranker=ChainReranker(
                rerankers=[
                    CustomerSpecificReranker(
                        reranker_id="rnk_272725719"
                    ),
                    UserFunctionReranker(
                        user_function="if (get('$.score') < 0.7) null else get('$.score') + 1"),
                ]
            )
        )

        response = self.client.query(query="Robot Utility Models", search=search,
                                     generation=self.generation_params,
                                     request_options=self.request_options)
        self.assertIsInstance(response, QueryFullResponse)
        for result in response.search_results:
            self.assertGreater(result.score, 1)

    def test_query_with_fcs_enabled(self):
        generation_params = GenerationParameters(
            response_language="eng",
            citations=CitationParameters(
                style="none",
            ),
            enable_factual_consistency_score=True,
        )
        response = self.client.query(query="Robot Utility Models", search=self.search_params,
                                     generation=generation_params,
                                     request_options=self.request_options)
        self.assertIsInstance(response, QueryFullResponse)
        self.assertIsNotNone(response.summary)
        self.assertGreater(len(response.search_results), 0)

    def test_query_stream(self):
        response = self.client.query_stream(query="Robot Utility Models", search=self.search_params,
                                            generation=self.generation_params,
                                            request_options=self.request_options)

        response = list(response)

        self.assertGreater(len(response), 0)
        for item in response:
            self.assertIsInstance(item, QueryStreamedResponse)

    def cleanup(self):
        for corpora in self.client.corpora.list():
            self.client.corpora.delete(corpora.key)

    def tearDown(self):
        for corpora in self.client.corpora.list():
            self.client.corpora.delete(corpora.key)
