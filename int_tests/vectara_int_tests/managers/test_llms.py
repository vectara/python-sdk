import unittest
import os

from vectara import Vectara, RemoteAuth


class TestLlmsManager(unittest.TestCase):
    client = None
    created_llms = None

    @classmethod
    def setUpClass(cls):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        
        cls.client = Vectara(api_key=api_key)
        cls.created_llms = set()

    def test_list_llms(self):
        # Test with default parameters
        found_llms = set()
        llms_list = self.client.llms.list()
        for llm in llms_list.items:
            self.assertIsNotNone(llm.name)
            found_llms.add(llm.name)

        # Test with filter parameter
        filtered_llms = self.client.llms.list(filter="gpt")
        for llm in filtered_llms.items:
            self.assertIn("gpt", llm.name.lower())

        # Test with limit parameter
        limited_llms = self.client.llms.list(limit=2)
        self.assertLessEqual(len(limited_llms.items), 2)

    # def test_create_and_delete_llm(self):
    #     # Create a test LLM
    #     llm_name = f"test-custom-llm"
    #     llm = self.client.llms.create(
    #         name=llm_name,
    #         description="Test LLM for integration tests",
    #         model="gpt-3.5-turbo",
    #         uri="https://api.openai.com/v1/chat/completions",
    #         auth={
    #             "type": "bearer",
    #             "token": os.getenv("OPENAI_API_KEY")
    #         }
    #     )
    #     self.created_llms.add(llm_name)
        
    #     # Verify the LLM was created
    #     self.assertEqual(llm.name, llm_name)
    #     self.assertEqual(llm.uri, "https://api.openai.com/v1/chat/completions")
    #     self.assertEqual(llm.description, "Test LLM for integration tests")

    #     # Get the LLM
    #     retrieved_llm = self.client.llms.get(llm_id=llm_name)
    #     self.assertEqual(retrieved_llm.name, llm_name)
    #     self.assertEqual(retrieved_llm.uri, "https://api.openai.com/v1/chat/completions")

    #     # Delete the LLM
    #     self.client.llms.delete(llm_id=llm_name)
    #     self.created_llms.remove(llm_name)

    #     # Verify the LLM was deleted
    #     with self.assertRaises(Exception):
    #         self.client.llms.get(llm_id=llm_name)