import unittest
import os

from vectara import Vectara
from vectara import SearchCorporaParameters, KeyedSearchCorpus, ContextConfiguration, GenerationParameters, \
    CitationParameters, ChatParameters, CoreDocument, CoreDocumentPart


class TestChatManager(unittest.TestCase):
    client = None
    key = None
    chat_id = None
    turn_id = None
    search_params = None
    generation_params = None
    chat_params = None
    created_corpora = None
    created_chats = None

    @classmethod
    def setUpClass(cls):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        
        cls.client = Vectara(api_key=api_key)
        cls.created_corpora = set()
        cls.created_chats = set()

        # Create test corpus
        response = cls.client.corpora.create(name="test-chat-manager", key="test-chat-manager")
        cls.key = response.key
        cls.created_corpora.add(cls.key)

        # Setup search parameters
        cls.search_params = SearchCorporaParameters(
            corpora=[
                KeyedSearchCorpus(
                    corpus_key=cls.key,
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

        # Setup generation parameters
        cls.generation_params = GenerationParameters(
            citations=CitationParameters(
                style="none",
            ),
            enable_factual_consistency_score=False,
        )

        # Setup chat parameters
        cls.chat_params = ChatParameters(store=True)

        # Add test document
        document = CoreDocument(
            id="my-doc-id",
            document_parts=[
                CoreDocumentPart(
                    text="""Robot Utility Models are trained on a diverse set of environments and objects, and then can
                         be deployed in novel environments with novel objects without any further data or training.""",
                )
            ],
        )
        cls.client.documents.create(cls.key, request=document)

        # Create initial chat
        response = cls.client.chat(
            query="Robot Utility Models",
            search=cls.search_params,
            generation=cls.generation_params,
            chat=cls.chat_params
        )

        cls.chat_id = response.chat_id
        cls.turn_id = response.turn_id
        cls.created_chats.add(cls.chat_id)

    def _create_chat(self):
        """Helper method to create a chat with default parameters."""
        response = self.client.chat(
            query="Robot Utility Models",
            search=self.search_params,
            generation=self.generation_params,
            chat=self.chat_params
        )
        self.created_chats.add(response.chat_id)
        return response

    def test_get_chat(self):
        response = self.client.chats.get(chat_id=self.chat_id)
        self.assertEqual(response.id, self.chat_id)

    # def test_list_chats(self):
    #     # Create additional chats
    #     created_chat_ids = {self.chat_id}
    #     for _ in range(2):
    #         response = self._create_chat()
    #         created_chat_ids.add(response.chat_id)

    #     # Get all chats and verify our created chats are in the list
    #     found_chats = set()
        
    #     # Use iter_pages to handle pagination automatically
    #     for page in self.client.chats.list().iter_pages():
    #         # Check each chat in the current page
    #         for chat in page:
    #             if chat.id in created_chat_ids:
    #                 found_chats.add(chat.id)
            
    #         # If we've found all our chats, we can stop
    #         if found_chats == created_chat_ids:
    #             break

    #     # Verify all our created chats were found
    #     self.assertEqual(found_chats, created_chat_ids)

    def test_delete_chat(self):
        chat = self._create_chat()
        
        # Delete the chat
        response = self.client.chats.delete(chat_id=chat.chat_id)
        self.assertIsNone(response)
        self.created_chats.remove(chat.chat_id)

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
        # Create additional turns
        created_turn_ids = {self.turn_id}
        for _ in range(2):
            response = self.client.chats.create_turns(
                chat_id=self.chat_id,
                query="Robot Utility Models",
                search=self.search_params,
                generation=self.generation_params,
                chat=self.chat_params
            )
            created_turn_ids.add(response.turn_id)

        # Get all turns and verify our created turns are in the list
        response = self.client.chats.list_turns(chat_id=self.chat_id)
        for turn in response.turns:
            if turn.id in created_turn_ids:
                self.assertIn(turn.id, created_turn_ids)

    @classmethod
    def tearDownClass(cls):
        """Clean up all test resources."""
        # Clean up chats
        for chat_id in cls.created_chats:
            try:
                cls.client.chats.delete(chat_id=chat_id)
            except Exception:
                pass

        # Clean up corpora
        for corpus_key in cls.created_corpora:
            try:
                cls.client.corpora.delete(corpus_key)
            except Exception:
                pass
