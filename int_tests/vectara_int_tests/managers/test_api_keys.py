import unittest
import os

from vectara import Vectara


class TestApiKeys(unittest.TestCase):
    client = None
    corpus_name = None
    corpus_key = None
    created_api_keys = None

    @classmethod
    def setUpClass(cls):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        
        cls.client = Vectara(api_key=api_key)
        cls.corpus_name = "test-api-keys"
        cls.corpus_key = cls.corpus_name
        cls.created_api_keys = set()

        # Create corpus
        response = cls.client.corpora.create(name=cls.corpus_name, key=cls.corpus_key)
        cls.key = response.key

    def _create_api_key(self, name="test-key", api_key_role="serving"):
        """Helper method to create an API key with given parameters."""
        response = self.client.api_keys.create(
            name=name,
            api_key_role=api_key_role,
            corpus_keys=[self.key]
        )
        self.created_api_keys.add(response.id)
        return response

    def test_create_api_key(self):
        response = self._create_api_key()
        self.assertEqual(response.name, "test-key")
        self.assertEqual(response.api_key_role, "serving")

    def test_delete_api_key(self):
        create_response = self._create_api_key()
        delete_response = self.client.api_keys.delete(create_response.id)
        self.assertIsNone(delete_response)
        self.created_api_keys.remove(create_response.id)

    def test_get_api_key(self):
        create_response = self._create_api_key()
        get_response = self.client.api_keys.get(create_response.id)
        self.assertEqual(get_response.name, create_response.name)

    def test_update_api_key(self):
        create_response = self._create_api_key()
        update_response = self.client.api_keys.update(create_response.id, enabled=False)
        self.assertEqual(update_response.enabled, False)

    def test_list_api_keys(self):
        # Create two test keys
        created_keys = []
        for index in range(2):
            create_response = self._create_api_key(name=f"test-key-{index}")
            created_keys.append(create_response.name)

        # Get all keys and verify our created keys are in the list
        all_keys = list(self.client.api_keys.list())
        
        # Verify our created keys are in the list
        for key in all_keys:
            if key.name in created_keys:
                self.assertIn(key.name, [name for name in created_keys])

    @classmethod
    def tearDownClass(cls):
        """Clean up all test resources."""
        # Clean up created API keys
        for api_key_id in cls.created_api_keys:
            try:
                cls.client.api_keys.delete(api_key_id)
            except Exception:
                pass
        
        # Clean up corpus
        try:
            cls.client.corpora.delete(cls.corpus_key)
        except Exception:
            pass
