import unittest
import os

from vectara import Vectara


class TestRerankersManager(unittest.TestCase):
    def setUp(self):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        
        self.client = Vectara(api_key=api_key)

    def test_list_rerankers(self):
        response = self.client.rerankers.list()
        for reranker in response:
            self.assertIsNotNone(reranker.name)
