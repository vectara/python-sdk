import time
import unittest

from vectara.factory import Factory


class TestApiKeys(unittest.TestCase):
    def setUp(self):
        self.client = Factory().build()
        self.addCleanup(self.cleanup)
        response = self.client.corpora.create(name="test-api-key-manager", key="test-document-manager")
        self.key = response.key
        time.sleep(60)

    def test_create_api_key(self):
        response = self.client.api_keys.create(name="test-key", api_key_role="serving", corpus_keys=[self.key])
        self.assertEqual(response.name, "test-key")
        self.assertEqual(response.enabled, True)
        self.assertEqual(response.api_key_role, "serving")

    def test_delete_api_key(self):
        create_response = self.client.api_keys.create(name="test-key", api_key_role="serving", corpus_keys=[self.key])
        delete_response = self.client.api_keys.delete(create_response.id)

        self.assertIsNone(delete_response)

    def test_get_api_key(self):
        create_response = self.client.api_keys.create(name="test-key", api_key_role="serving", corpus_keys=[self.key])
        get_response = self.client.api_keys.get(create_response.id)

        self.assertEqual(get_response.name, create_response.name)

    def test_update_api_key(self):
        create_response = self.client.api_keys.create(name="test-key", api_key_role="serving", corpus_keys=[self.key])
        update_response = self.client.api_keys.update(create_response.id, enabled=False)

        self.assertEqual(update_response.enabled, False)

    def test_list_api_keys(self):
        api_keys_names = []
        for index in range(2):
            create_response = self.client.api_keys.create(name=f"test-key-{index}", api_key_role="serving",
                                                          corpus_keys=[self.key])
            api_keys_names.append(create_response.name)

        for key in self.client.api_keys.list():
            self.assertIn(key.name, api_keys_names)

    def cleanup(self):
        response = self.client.corpora.list()
        for corpora in response:
            self.client.corpora.delete(corpora.key)

    def tearDown(self):
        for corpora in self.client.corpora.list():
            self.client.corpora.delete(corpora.key)
        for key in self.client.api_keys.list():
            self.client.api_keys.delete(key.id)
