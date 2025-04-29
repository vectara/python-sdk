import unittest
import os

from vectara import Vectara


class TestAuthManager(unittest.TestCase):
    client = None
    client_id = None
    client_secret = None
    created_clients = None

    @classmethod
    def setUpClass(cls):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        
        cls.client = Vectara(api_key=api_key)
        cls.created_clients = set()

        # Create test client
        response = cls.client.app_clients.create(name="test-client", api_roles=["owner"])
        cls.client_id = response.client_id
        cls.client_secret = response.client_secret
        cls.created_clients.add(response.id)

    def test_get_access_token(self):
        response = self.client.auth.get_token(
            client_id=self.client_id,
            client_secret=self.client_secret,
            grant_type="client_credentials"
        )

        self.assertIsNotNone(response.access_token)
        self.assertIsNotNone(response.token_type)
        self.assertIsNotNone(response.expires_in)

    @classmethod
    def tearDownClass(cls):
        """Clean up all test resources."""
        for client_id in cls.created_clients:
            try:
                cls.client.app_clients.delete(client_id)
            except Exception:
                pass
