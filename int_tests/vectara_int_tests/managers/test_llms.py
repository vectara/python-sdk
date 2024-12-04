import unittest

from vectara.factory import Factory


class TestLlmsManager(unittest.TestCase):
    def setUp(self):
        self.client = Factory().build()

    def test_list_llms(self):
        response = self.client.llms.list()
        for reranker in response:
            self.assertIsNotNone(reranker.name)