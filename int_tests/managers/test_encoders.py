import unittest
import os

from vectara.client import Vectara


class TestEncodersManager(unittest.TestCase):

    def setUp(self):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        self.client = Vectara(api_key=api_key)

    def test_list_encoders(self):
        response = self.client.encoders.list()
        for encoder in response:
            self.assertIsNotNone(encoder.name)
