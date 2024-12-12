import time
import unittest

from vectara.core import RequestOptions, ApiError
from vectara.factory import Factory

from vectara import CoreDocument, CoreDocumentPart, SearchCorporaParameters, KeyedSearchCorpus, \
    ContextConfiguration, CustomerSpecificReranker, GenerationParameters, CitationParameters, \
    ChatParameters


class TestChat(unittest.TestCase):

    def setUp(self):
        self.addCleanup(self.cleanup)
        self.client = Factory().build()
        self.client.corpora.create(name="test-chat", key="test-chat")
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
        self.client.documents.create("test-chat", request=test_search_1_document)

        self.search_params = SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key="test-chat",
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
            enable_factual_consistency_score=True,
        )
        self.chat_params = ChatParameters(store=True)
        self.request_options = RequestOptions(timeout_in_seconds=100)

    def test_chat(self):
        session = self.client.create_chat_session(
            search=self.search_params,
            generation=self.generation_params,
            chat_config=self.chat_params,
            request_options=self.request_options
        )

        response = session.chat(query="Robot Utility Models")
        self.assertIsNotNone(response.chat_id)
        self.assertIsNotNone(response.answer)

        response = session.chat(query="Utility Models")
        self.assertIsNotNone(response.chat_id)
        self.assertIsNotNone(response.answer)

    def test_chat_with_default_params(self):
        session = self.client.create_chat_session(
            search=SearchCorporaParameters(corpora=[
                KeyedSearchCorpus(
                    corpus_key="test-chat",
                    metadata_filter="",
                    lexical_interpolation=1,
                )
            ])
        )

        response = session.chat(query="Robot Utility Models")
        self.assertIsNotNone(response.chat_id)
        self.assertIsNotNone(response.answer)

    def test_exception_in_chat(self):
        session = self.client.create_chat_session(
            search=SearchCorporaParameters()
        )
        with self.assertRaises(ApiError) as context:
            session.chat(query="Robot Utility Models")

        exception = context.exception
        self.assertEqual(exception.status_code, 400)
        self.assertEqual(
            exception.body.field_errors,
            {"body.search.corpora": "[] should have at least 1 items."},
        )

    def test_chat_stream(self):
        session = self.client.create_chat_session(
            search=self.search_params,
            generation=self.generation_params,
            chat_config=self.chat_params,
            request_options=self.request_options
        )
        response_chunks = []
        for data in session.chat_stream(query="Robot Utility Models"):
            response_chunks.append(data)

        self.assertGreater(len(response_chunks), 0)

    def cleanup(self):
        for corpora in self.client.corpora.list():
            self.client.corpora.delete(corpora.key)

    def tearDown(self):
        for corpora in self.client.corpora.list():
            self.client.corpora.delete(corpora.key)
