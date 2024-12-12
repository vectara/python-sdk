import unittest

from vectara.factory import Factory


class TestUserManager(unittest.TestCase):

    def setUp(self):
        self.client = Factory().build()

    def test_create_user(self):
        response = self.client.users.create(email="test-email@example.com",
                                            username="test-user", api_roles=["administrator"])

        self.assertEqual(response.username, "test-user")
        self.assertEqual(response.email, "test-email@example.com")
        self.assertEqual(response.api_roles, ["administrator"])
        self.assertEqual(response.enabled, False)

    def test_update_user(self):
        create_eresponse = self.client.users.create(email="test-email@example.com",
                                                    username="test-user", api_roles=["administrator"])

        self.assertEqual(create_eresponse.api_roles, ["administrator"])
        self.assertEqual(create_eresponse.enabled, False)

        update_response = self.client.users.update(username="test-user", enabled=True,
                                                   api_roles=["corpus_administrator"])

        self.assertEqual(update_response.api_roles, ["corpus_administrator"])
        self.assertEqual(update_response.enabled, True)

    def test_delete_user(self):
        create_eresponse = self.client.users.create(email="test-email@example.com",
                                                    username="test-user", api_roles=["administrator"])

        del_response = self.client.users.delete(username=create_eresponse.username)

        self.assertIsNone(del_response)

    def test_get_user(self):
        create_eresponse = self.client.users.create(email="test-email@example.com",
                                                    username="test-user", api_roles=["administrator"])

        get_response = self.client.users.get(username=create_eresponse.username)

        self.assertEqual(get_response.username, "test-user")
        self.assertEqual(get_response.email, "test-email@example.com")
        self.assertEqual(get_response.api_roles, ["administrator"])
        self.assertEqual(get_response.enabled, False)

    def test_list_users(self):
        usernames = []
        for index in range(2):
            create_eresponse = self.client.users.create(email="test-email@example.com",
                                                        username=f"test-user-{index}", api_roles=["administrator"])
            usernames.append(create_eresponse.username)

        for user in self.client.users.list():
            self.assertIn(user.username, usernames)

    def tearDown(self):
        for user in self.client.users.list():
            self.client.users.delete(username=user.username)
