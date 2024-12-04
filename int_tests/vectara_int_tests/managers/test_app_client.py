import unittest

from vectara.factory import Factory


class TestAppClient(unittest.TestCase):
    def setUp(self):
        self.client = Factory().build()

    def test_create_app_client(self):
        response = self.client.app_clients.create(name="test-client", api_roles=["owner"])
        self.assertEqual(response.name, "test-client")
        self.assertIsNotNone(response.client_id)
        self.assertIsNotNone(response.client_secret)

    def test_get_app_client(self):
        create_response = self.client.app_clients.create(name="test-client", api_roles=["owner"])
        get_response = self.client.app_clients.get(create_response.id)

        self.assertEqual(get_response.client_id, create_response.client_id)
        self.assertEqual(get_response.client_secret, create_response.client_secret)

    def test_delete_app_client(self):
        create_response = self.client.app_clients.create(name="test-client", api_roles=["owner"])
        del_response = self.client.app_clients.delete(create_response.id)

        self.assertIsNone(del_response)

    def test_update_app_client(self):
        create_response = self.client.app_clients.create(name="test-client", api_roles=["owner"])
        update_response = self.client.app_clients.update(
            create_response.id, api_roles=["owner", "administrator"], description="test client")

        self.assertEqual(update_response.api_roles, ["administrator"])
        self.assertEqual(update_response.description, "test client")

    def test_list_app_clients(self):
        client_ids = []
        for index in range(2):
            create_response = self.client.app_clients.create(name=f"test-client-{index}", api_roles=["owner"])
            client_ids.append(create_response.client_id)

        for client in self.client.app_clients.list():
            self.assertIn(client.client_id, client_ids)

    def tearDown(self):
        for client in self.client.app_clients.list():
            self.client.app_clients.delete(client.id)
