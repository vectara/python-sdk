import unittest

from vectara import SearchCorporaParameters, KeyedSearchCorpus, ContextConfiguration, GenerationParameters, \
    CitationParameters, ChatParameters, CoreDocument, CoreDocumentPart
from vectara.factory import Factory


class TestChatManager(unittest.TestCase):
    def setUp(self):
        self.addCleanup(self.cleanup)
        self.client = Factory().build()
        response = self.client.corpora.create(name="test-chat-manager", key="test-chat-manager")
        self.key = response.key
        self.search_params = SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key=self.key,
                    lexical_interpolation=0,
                )
            ],
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

        document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="""Robot Utility Models are trained on a diverse set of environments and objects, and then can
                         be deployed in novel environments with novel objects without any further data or training.""",
                )
            ],
        )
        self.client.documents.create("test-chat-manager", request=document)

        response = self.client.chat(
            query="Robot Utility Models",
            search=self.search_params,
            generation=self.generation_params,
            chat=self.chat_params
        )

        self.chat_id = response.chat_id
        self.turn_id = response.turn_id

    def test_get_chat(self):
        response = self.client.chats.get(chat_id=self.chat_id)
        self.assertEqual(response.id, self.chat_id)

    def test_list_chats(self):
        chat_ids = [self.chat_id]
        for _ in range(2):
            response = self.client.chat(
                query="Robot Utility Models",
                search=self.search_params,
                generation=self.generation_params,
                chat=self.chat_params
            )
            chat_ids.append(response.chat_id)

        response = self.client.chats.list()
        for chat in response:
            self.assertIn(chat.id, chat_ids)

    def test_delete_chat(self):
        response = self.client.chats.delete(chat_id=self.chat_id)
        self.assertIsNone(response)

    def test_create_turn(self):
        response = self.client.chats.create_turns(
            chat_id=self.chat_id,
            query="Robot Utility Models",
            search=self.search_params,
            generation=self.generation_params,
            chat=self.chat_params
        )

        self.assertEqual(response.chat_id, self.chat_id)
        self.assertIsNotNone(response.turn_id)

    def test_get_turn(self):
        response = self.client.chats.create_turns(
            chat_id=self.chat_id,
            query="Robot Utility Models",
            search=self.search_params,
            generation=self.generation_params,
            chat=self.chat_params
        )

        get_response = self.client.chats.get_turn(chat_id=self.chat_id, turn_id=response.turn_id)

        self.assertEqual(get_response.chat_id, self.chat_id)
        self.assertEqual(get_response.id, response.turn_id)

    def test_delete_turn(self):
        response = self.client.chats.create_turns(
            chat_id=self.chat_id,
            query="Robot Utility Models",
            search=self.search_params,
            generation=self.generation_params,
            chat=self.chat_params
        )

        del_response = self.client.chats.delete_turn(chat_id=self.chat_id, turn_id=response.turn_id)
        self.assertIsNone(del_response)

    def test_update_turn(self):
        response = self.client.chats.create_turns(
            chat_id=self.chat_id,
            query="Robot Utility Models",
            search=self.search_params,
            generation=self.generation_params,
            chat=self.chat_params
        )
        turn = self.client.chats.update_turn(chat_id=self.chat_id, turn_id=response.turn_id, enabled=False)

        self.assertEqual(turn.enabled, False)

    def test_list_turns(self):
        turn_ids = [self.turn_id]
        for _ in range(2):
            response = self.client.chats.create_turns(
                chat_id=self.chat_id,
                query="Robot Utility Models",
                search=self.search_params,
                generation=self.generation_params,
                chat=self.chat_params
            )
            turn_ids.append(response.turn_id)

        response = self.client.chats.list_turns(chat_id=self.chat_id)
        for turn in response.turns:
            self.assertIn(turn.id, turn_ids)

    def cleanup(self):
        self.client.chats.delete(chat_id=self.chat_id)
        for corpora in self.client.corpora.list():
            self.client.corpora.delete(corpora.key)

    def tearDown(self):
        self.client.chats.delete(chat_id=self.chat_id)
        for corpora in self.client.corpora.list():
            self.client.corpora.delete(corpora.key)
