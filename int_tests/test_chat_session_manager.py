import unittest
from datetime import timedelta
import time

from vectara import SearchCorporaParameters, KeyedSearchCorpus, ContextConfiguration, CustomerSpecificReranker, \
    GenerationParameters, ModelParameters, CitationParameters, ChatParameters
from vectara.client import ChatSessionManager
from vectara.core import RequestOptions


class TestChatSessionManagerIntegration(unittest.TestCase):
    def setUp(self):
        self.session_manager = ChatSessionManager(session_expiry_time=timedelta(seconds=5),
                                                  cleanup_interval_in_seconds=6)
        self.search_params = SearchCorporaParameters(
                corpora=[
                    KeyedSearchCorpus(
                        corpus_key="test_corpus_key",
                        metadata_filter="",
                        lexical_interpolation=1,
                    )
                ],
                offset=1,
                limit=1,
                context_configuration=ContextConfiguration(
                    characters_before=1,
                    characters_after=1,
                    sentences_before=1,
                    sentences_after=1,
                    start_tag="%",
                    end_tag="%",
                ),
                reranker=CustomerSpecificReranker(
                    reranker_id="test_id",
                    reranker_name="test",
                ),
            )
        self.generation_params = GenerationParameters(
                generation_preset_name="test",
                prompt_name="test",
                max_used_search_results=1,
                prompt_template="test",
                prompt_text="test",
                max_response_characters=1,
                response_language="test",
                model_parameters=ModelParameters(
                    max_tokens=1,
                    temperature=1.1,
                    frequency_penalty=1.1,
                    presence_penalty=1.1,
                ),
                citations=CitationParameters(
                    style="none",
                ),
                enable_factual_consistency_score=True,
            )
        self.chat_params = ChatParameters(store=True)
        self.request_options = RequestOptions(timeout_in_seconds=100)
        self.request_timeout = 1
        self.request_timeout_millis = 1

    def test_create_and_retrieve_session(self):
        chat_id = "test_chat"

        self.session_manager.create_session(chat_id, self.search_params, self.generation_params, self.chat_params,
                                            self.request_options, self.request_timeout, self.request_timeout_millis)

        session = self.session_manager.get_session(chat_id)
        self.assertIsNotNone(session)
        self.assertEqual(session["search"], self.search_params)
        self.assertEqual(session["generation"], self.generation_params)
        self.assertEqual(session["chat"], self.chat_params)
        self.assertEqual(session["request_options"], self.request_options)
        self.assertEqual(session["request_timeout"], self.request_timeout)
        self.assertEqual(session["request_timeout_millis"], self.request_timeout_millis)

    def test_session_expiration(self):
        chat_id = "test_chat_expiration"

        self.session_manager.create_session(chat_id, self.search_params, self.generation_params, self.chat_params)

        time.sleep(7)

        session = self.session_manager.get_session(chat_id)
        self.assertIsNone(session)

    def test_clean_expired_sessions(self):
        self.session_manager.create_session("chat1", self.search_params, self.generation_params, self.chat_params)
        self.session_manager.create_session("chat2", self.search_params, self.generation_params, self.chat_params)

        time.sleep(7)

        self.session_manager.clean_expired_sessions()

        self.assertIsNone(self.session_manager.get_session("chat1"))
        self.assertIsNone(self.session_manager.get_session("chat2"))

    def test_threaded_cleanup(self):
        chat_id = "test_threaded_cleanup"
        self.session_manager.create_session(chat_id, self.search_params, self.generation_params, self.chat_params)

        time.sleep(7)

        session = self.session_manager.get_session(chat_id)
        self.assertIsNone(session)

    def tearDown(self):
        self.session_manager.cleanup_thread.join(timeout=0.1)
