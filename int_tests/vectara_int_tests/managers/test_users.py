import unittest
import os
import json

from vectara import Vectara
from vectara.types import ApiRole


class TestUsersManager(unittest.TestCase):
    client = None
    created_users = None
    app_client = None

    @classmethod
    def setUpClass(cls):
        # Create app client
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        cls.client = Vectara(api_key=api_key)
        cls.app_client = cls.client.app_clients.create(name="test-users", api_roles=["owner"])

        cls.created_users = set()
        cls.client_wit_oauth = Vectara(client_id=cls.app_client.client_id, client_secret=cls.app_client.client_secret)


    def _create_test_user(self, suffix=""):
        """Helper method to create a test user."""
        username = f"test-user-{suffix}" if suffix else "test-user"
        email = f"{username}@example.com"
        
        response = self.client_wit_oauth.users.create(
            email=email,
            username=username,
            description=f"Test user {suffix}",
            api_roles=["owner"]
        )
        self.created_users.add(username)
        print("\nCreated user response:")
        print(json.dumps(response.model_dump(mode="json"), indent=2))
        print(response.email)
        print(response.username)
        print(response.description)
        print(response.api_roles)
        
        return response

    def test_create_user(self):
        """Test user creation."""
        user = self._create_test_user("create")
        self.assertEqual(user.username, "test-user-create")
        self.assertEqual(user.email, "test-user-create@example.com")
        self.assertEqual(user.description, "Test user create")
        self.assertIn(ApiRole, user.api_roles)

    def test_get_user(self):
        """Test getting a user."""
        # Create a user first
        created_user = self._create_test_user("get")
        
        # Get the user
        user = self.client.users.get(username=created_user.username)
        print("\nGet user response:")
        print(json.dumps(user.to_dict(), indent=2))
        
        self.assertEqual(user.username, created_user.username)
        self.assertEqual(user.email, created_user.email)
        self.assertEqual(user.description, created_user.description)
        self.assertEqual(user.api_roles, created_user.api_roles)

    def test_update_user(self):
        """Test updating a user."""
        # Create a user first
        user = self._create_test_user("update")
        
        # Update the user
        updated_user = self.client.users.update(
            username=user.username,
            description="Updated description",
            api_roles=[ApiRole.ADMIN, ApiRole.USER]
        )
        print("\nUpdate user response:")
        print(json.dumps(updated_user.to_dict(), indent=2))
        
        self.assertEqual(updated_user.username, user.username)
        self.assertEqual(updated_user.description, "Updated description")
        self.assertEqual(len(updated_user.api_roles), 2)
        self.assertIn(ApiRole.ADMIN, updated_user.api_roles)
        self.assertIn(ApiRole.USER, updated_user.api_roles)

    def test_list_users(self):
        """Test listing users."""
        # Create some test users
        self._create_test_user("list1")
        self._create_test_user("list2")
        
        # List users
        users = self.client.users.list()
        print("\nList users response:")
        print(json.dumps([user.to_dict() for user in users.items], indent=2))
        
        # Verify our test users are in the list
        found_users = {user.username for user in users.items}
        self.assertTrue(all(f"test-user-list{i}" in found_users for i in range(1, 3)))

    def test_delete_user(self):
        """Test deleting a user."""
        # Create a user first
        user = self._create_test_user("delete")
        
        # Delete the user
        self.client.users.delete(username=user.username)
        self.created_users.remove(user.username)
        
        # Verify the user was deleted
        with self.assertRaises(Exception):
            self.client.users.get(username=user.username)

    @classmethod
    def tearDownClass(cls):
        """Clean up test resources."""
        # Delete all created users
        for username in cls.created_users:
            try:
                cls.client_wit_oauth.users.delete(username=username)
            except Exception:
                pass
        
        # Delete the app client
        if cls.app_client:
            try:
                cls.app_client.delete()
            except Exception:
                pass
