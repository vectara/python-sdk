import unittest

from vectara.factory import Factory


class TestEncodersManager(unittest.TestCase):

    def setUp(self):
        self.client = Factory().build()

    def test_list_encoders(self):
        response = self.client.encoders.list()
        for encoder in response:
            self.assertIsNotNone(encoder.name)
