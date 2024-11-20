import time
import unittest
from datetime import timedelta
from pathlib import Path

from vectara import SearchCorporaParameters, KeyedSearchCorpus, ContextConfiguration, \
    GenerationParameters, CitationParameters, ChatParameters
from vectara.client import ChatSessionManager
from vectara.factory import Factory
from vectara.managers import CreateCorpusRequest


class TestChat(unittest.TestCase):

    def setUp(self):
        self.client = Factory().build()
        request = CreateCorpusRequest(name="int-test-upload-fern", key="int-test-upload-fern")
        create_response = self.client.lab_helper.create_lab_corpus(request, user_prefix=False)
        self.key = create_response.key

        self.client.session_manager = ChatSessionManager(session_expiry_time=timedelta(seconds=5),
                                                         cleanup_interval_in_seconds=6)

        self.search_params = SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key=self.key,
                    lexical_interpolation=0,
                )
            ],
            offset=1,
            limit=1,
            context_configuration=ContextConfiguration(
                characters_before=1,
                characters_after=1,
                sentences_before=1,
                sentences_after=1,
            ),
        )
        self.generation_params = GenerationParameters(
            citations=CitationParameters(
                style="none",
            ),
            enable_factual_consistency_score=True,
        )
        self.chat_params = ChatParameters(store=True)

        path = Path("examples/01_getting_started/resources/arxiv/2409.05865v1.pdf")
        with open(path, "rb") as f:
            content = f.read()
            self.client.upload.file(self.key, file=(content, "application/pdf"),
                                    metadata={"test_sdk": "ok"}, filename="test-document")

    def test_chat(self):
        response = self.client.chat(
            query="what is vectara?",
            search=self.search_params,
            generation=self.generation_params,
            chat=self.chat_params
        )

        self.assertIsNotNone(response.chat_id)
        self.assertIsNotNone(response.answer)

        response = self.client.chat(
            query="what is vectara?",
            chat_id=response.chat_id
        )

        self.assertIsNotNone(response.chat_id)
        self.assertIsNotNone(response.answer)

    def tearDown(self):
        self.client.corpora.delete(corpus_key=self.key)
