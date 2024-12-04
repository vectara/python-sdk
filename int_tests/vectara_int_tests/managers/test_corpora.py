import time
import unittest

from vectara import FilterAttribute, CorpusCustomDimension, CoreDocument, CoreDocumentPart, SearchCorporaParameters, \
    ContextConfiguration, CustomerSpecificReranker, GenerationParameters, ModelParameters, \
    CitationParameters, SearchCorpusParameters
from vectara.core import RequestOptions
from vectara.factory import Factory


class TestCorporaManager(unittest.TestCase):
    def setUp(self):
        self.client = Factory().build()
        self.addCleanup(self.cleanup)

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
        response = self.client.corpora.create(
            key="test-create-corpus",
            name="test-create-corpus",
            description="test description",
            queries_are_answers=True,
            documents_are_questions=True,
            encoder_name="boomerang-2023-q3",
            filter_attributes=[filter_attributes],
            # custom_dimensions=[custom_dimensions]
        )
        time.sleep(30)
        self.assertEqual(response.key, "test-create-corpus")
        self.assertEqual(response.name, "test-create-corpus")
        self.assertEqual(response.description, "test description")
        self.assertEqual(response.queries_are_answers, True)
        self.assertEqual(response.documents_are_questions, True)
        self.assertEqual(response.encoder_name, "boomerang-2023-q3")
        self.assertEqual(response.filter_attributes, [filter_attributes])
        # self.assertEqual(response.custom_dimensions, [custom_dimensions])

    def test_list_corpora(self):
        self.client.corpora.create(key="corpus-1")
        self.client.corpora.create(key="corpus-2")
        time.sleep(30)

        response = self.client.corpora.list()
        self.assertEqual(len(list(response)), 2)

        for corpora in response:
            self.assertIn(corpora.key, ["corpus-1", "corpus-2"])

    def test_delete_corpora(self):
        self.client.corpora.create(key="test-delete-corpus")
        self.client.corpora.delete(corpus_key="test-delete-corpus")
        time.sleep(30)
        corpora = self.client.corpora.list()

        self.assertEqual(len(list(corpora)), 0)

    def test_update_corpora(self):
        response = self.client.corpora.create(key="test-update-corpus")
        time.sleep(30)
        self.assertEqual(response.key, "test-update-corpus")
        self.assertEqual(response.name, "test-update-corpus")

        response = self.client.corpora.update("test-update-corpus",
                                              name="updated-name", description="updated-description")

        time.sleep(30)

        self.assertEqual(response.description, "updated-description")
        self.assertEqual(response.name, "updated-name")

    def test_get_metadata_of_corpora(self):
        self.client.corpora.create(key="test-get-metadata",
                                   description="test-description", name="Test")
        time.sleep(30)
        corpora = self.client.corpora.get("test-get-metadata")

        self.assertEqual(corpora.key, "test-get-metadata")
        self.assertEqual(corpora.name, "Test")
        self.assertEqual(corpora.description, "test-description")

    def test_corpus_reset(self):
        self.client.corpora.create(key="test-reset-corpus")
        time.sleep(30)
        document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="I'm a nice document part.",
                )
            ],
        )
        self.client.documents.create("test-reset-corpus", request=document)
        documents = self.client.documents.list("test-reset-corpus")
        self.assertEqual(len(list(documents)), 1)

        self.client.corpora.reset("test-reset-corpus")

        documents = self.client.documents.list("test-reset-corpus")
        self.assertEqual(len(list(documents)), 0)

    def test_replace_filter_attributes(self):
        self.client.corpora.create(key="test-reset-filters")
        time.sleep(30)
        filter_attributes = FilterAttribute(
            name="Title",
            level="document",
            description="The title of the document.",
            indexed=True,
            type="text"
        )
        res = self.client.corpora.replace_filter_attributes("test-reset-filters", filter_attributes=[filter_attributes])

        self.assertIsNotNone(res.job_id)

    def test_search(self):
        self.client.corpora.create(name="test-search", key="test-search")
        time.sleep(30)
        document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="Robot Utility Models are trained on a diverse set of environments and objects, and then can "
                         "be deployed in novel environments with novel objects without any further data or training.",
                )
            ],
        )
        self.client.documents.create("test-search", request=document)

        response = self.client.corpora.search(corpus_key="test-search", query="Robot Utility Models")
        self.assertIsNone(response.summary)
        self.assertGreater(len(response.search_results), 0)

    def test_query(self):
        self.client.corpora.create(name="test-search", key="test-search")
        time.sleep(60)
        document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="Robot Utility Models are trained on a diverse set of environments and objects, and then can "
                         "be deployed in novel environments with novel objects without any further data or training.",
                )
            ],
        )
        self.client.documents.create("test-search", request=document)
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

        response = self.client.corpora.query(corpus_key="test-search", search=search_params,
                                             query="Robot Utility Models", generation=generation_params,
                                             request_options=request_options)
        self.assertIsNotNone(response.summary)
        self.assertGreater(len(response.search_results), 0)

    def cleanup(self):
        for corpora in self.client.corpora.list():
            self.client.corpora.delete(corpora.key)

    def tearDown(self):
        for corpora in self.client.corpora.list():
            self.client.corpora.delete(corpora.key)
