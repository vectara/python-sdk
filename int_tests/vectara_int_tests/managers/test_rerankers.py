import unittest

from vectara.factory import Factory


class TestRerankersManager(unittest.TestCase):
    def setUp(self):
        self.client = Factory().build()

    def test_list_rerankers(self):
        response = self.client.rerankers.list()
        for llm in response:
            self.assertIsNotNone(llm.name)
