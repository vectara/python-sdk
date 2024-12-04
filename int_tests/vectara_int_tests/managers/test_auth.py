import unittest

from vectara.factory import Factory


class TestAuthManager(unittest.TestCase):

    def setUp(self):
        self.addCleanup(self.cleanup)
        self.client = Factory().build()
        response = self.client.app_clients.create(name="test-client", api_roles=["owner"])
        self.client_id = response.client_id
        self.client_secret = response.client_secret

    def test_get_access_token(self):
        response = self.client.auth.get_token(
            client_id=self.client_id,
            client_secret=self.client_secret,
            grant_type="client_credentials"
        )

        self.assertIsNotNone(response.access_token)
        self.assertIsNotNone(response.token_type)
        self.assertIsNotNone(response.expires_in)

    def cleanup(self):
        for client in self.client.app_clients.list():
            self.client.app_clients.delete(client.id)

    def tearDown(self):
        for client in self.client.app_clients.list():
            self.client.app_clients.delete(client.id)
