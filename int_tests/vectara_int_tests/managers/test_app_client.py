import os
import unittest

from vectara import Vectara


class TestAppClient(unittest.TestCase):
    client = None
    created_clients = None

    @classmethod
    def setUpClass(cls):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        cls.client = Vectara(api_key=api_key)
        cls.created_clients = set()

    def _create_app_client(self, name="test-client", api_roles=["owner"]):
        """Helper method to create an app client with given parameters."""
        response = self.client.app_clients.create(name=name, api_roles=api_roles)
        self.created_clients.add(response.id)
        return response

    def test_create_app_client(self):
        response = self._create_app_client()
        self.assertEqual(response.name, "test-client")
        self.assertIsNotNone(response.client_id)
        self.assertIsNotNone(response.client_secret)

    def test_get_app_client(self):
        create_response = self._create_app_client()
        get_response = self.client.app_clients.get(create_response.id)

        self.assertEqual(get_response.client_id, create_response.client_id)
        self.assertEqual(get_response.client_secret, create_response.client_secret)

    def test_delete_app_client(self):
        create_response = self._create_app_client()
        del_response = self.client.app_clients.delete(create_response.id)
        self.assertIsNone(del_response)
        self.created_clients.remove(create_response.id)

    def test_update_app_client(self):
        create_response = self._create_app_client()
        update_response = self.client.app_clients.update(
            create_response.id, 
            api_roles=["owner", "administrator"], 
            description="test client"
        )

        self.assertEqual(update_response.api_roles, ["owner", "administrator"])
        self.assertEqual(update_response.description, "test client")

    def test_list_app_clients(self):
        # Create two test clients
        created_clients = []
        for index in range(2):
            create_response = self._create_app_client(name=f"test-client-{index}")
            created_clients.append(create_response)

        # Get all clients and verify our created clients are in the list
        all_clients = list(self.client.app_clients.list())
        created_client_ids = {client.id for client in created_clients}
        
        # Verify our created clients are in the list
        for client in all_clients:
            if client.id in created_client_ids:
                self.assertIn(client.name, [c.name for c in created_clients])

    @classmethod
    def tearDownClass(cls):
        """Clean up all test resources."""
        for client_id in cls.created_clients:
            try:
                cls.client.app_clients.delete(client_id)
            except Exception:
                pass
