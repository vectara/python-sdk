import unittest
import os

from vectara import Vectara


class TestUserManager(unittest.TestCase):
    client = None
    created_users = None

    @classmethod
    def setUpClass(cls):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        
        cls.client = Vectara(api_key=api_key)
        cls.created_users = set()

    def _create_test_user(self, username_suffix=""):
        """Helper method to create a test user."""
        username = f"test-user-{username_suffix}" if username_suffix else "test-user"
        email = f"test-email-{username_suffix}@example.com" if username_suffix else "test-email@example.com"
        
        response = self.client.users.create(
            email=email,
            username=username,
            api_roles=["administrator"]
        )
        self.created_users.add(username)
        return response

    def test_create_user(self):
        response = self._create_test_user()
        
        self.assertEqual(response.username, "test-user")
        self.assertEqual(response.email, "test-email@example.com")
        self.assertEqual(response.api_roles, ["administrator"])
        self.assertEqual(response.enabled, False)

    def test_update_user(self):
        # Create initial user
        user = self._create_test_user("update")
        self.assertEqual(user.api_roles, ["administrator"])
        self.assertEqual(user.enabled, False)

        # Update user
        update_response = self.client.users.update(
            username=user.username,
            enabled=True,
            api_roles=["corpus_administrator"]
        )

        self.assertEqual(update_response.api_roles, ["corpus_administrator"])
        self.assertEqual(update_response.enabled, True)
        self.assertEqual(update_response.username, user.username)
        self.assertEqual(update_response.email, user.email)

    def test_delete_user(self):
        # Create and then delete user
        user = self._create_test_user("delete")
        del_response = self.client.users.delete(username=user.username)
        
        self.assertIsNone(del_response)
        self.created_users.remove(user.username)

        # Verify user is deleted
        with self.assertRaises(Exception):
            self.client.users.get(username=user.username)

    def test_get_user(self):
        user = self._create_test_user("get")
        
        get_response = self.client.users.get(username=user.username)

        self.assertEqual(get_response.username, user.username)
        self.assertEqual(get_response.email, user.email)
        self.assertEqual(get_response.api_roles, ["administrator"])
        self.assertEqual(get_response.enabled, False)

    def test_list_users(self):
        # Create multiple test users
        created_usernames = set()
        for i in range(2):
            user = self._create_test_user(f"list-{i}")
            created_usernames.add(user.username)

        # Get all users and verify our created users are in the list
        found_usernames = set()
        for user in self.client.users.list().items:
            if user.username in created_usernames:
                found_usernames.add(user.username)
            
            # If we've found all our users, we can stop
            if found_usernames == created_usernames:
                break

        # Verify all our created users were found
        self.assertEqual(found_usernames, created_usernames)

    @classmethod
    def tearDownClass(cls):
        """Clean up all test users."""
        for username in cls.created_users:
            try:
                cls.client.users.delete(username=username)
            except Exception:
                pass
