import unittest
import os

from vectara import Vectara
from vectara.core import RequestOptions, ApiError
from vectara import CoreDocument, CoreDocumentPart, SearchCorporaParameters, KeyedSearchCorpus, \
    ContextConfiguration, CustomerSpecificReranker, GenerationParameters, CitationParameters, \
    ChatParameters


class TestChat(unittest.TestCase):
    corpus_name = None
    client = None
    TEST_DOCUMENT = CoreDocument(
        id="my-doc-id",
        document_parts=[
            CoreDocumentPart(
                text="Robot Utility Models are trained on a diverse set of environments and objects, and then can "
                     "be deployed in novel environments with novel objects without any further data or training.",
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
        cls.chat_params = ChatParameters(store=True)

        # Create corpus and add document
        cls.corpus_name = "test-chat-corpus"
        cls.client.corpora.create(name=cls.corpus_name, key=cls.corpus_name)
        cls.client.documents.create(cls.corpus_name, request=cls.TEST_DOCUMENT)

        # Create default search parameters
        cls.search_params = SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key=cls.corpus_name,
                    metadata_filter="",
                    lexical_interpolation=0.05,
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

    def test_chat(self):
        session = self.client.create_chat_session(
            search=self.search_params,
            generation=self.generation_params,
            chat_config=self.chat_params,
            request_options=self.request_options
        )

        first_response = session.chat(query="What are Robot Utility Models?")
        self.assertIsNotNone(first_response.chat_id)
        self.assertIsNotNone(first_response.answer)
        first_chat_id = first_response.chat_id

        second_response = session.chat(query="How do they handle novel environments?")
        self.assertIsNotNone(second_response.chat_id)
        self.assertIsNotNone(second_response.answer)
        
        # Verify chat continuity
        self.assertEqual(first_chat_id, second_response.chat_id, "Chat ID should remain the same across turns")
        

    def test_chat_with_default_params(self):
        session = self.client.create_chat_session(
            search=SearchCorporaParameters(
                corpora=[
                    KeyedSearchCorpus(
                        corpus_key=self.corpus_name,
                        metadata_filter="",
                        lexical_interpolation=1,
                    )
                ]
            )
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

    @classmethod
    def tearDownClass(cls):
        """Clean up all test resources."""
        try:
            cls.client.corpora.delete(cls.corpus_name)
        except Exception:
            pass
