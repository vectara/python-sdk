import unittest

from vectara.client import Vectara

class ClientTest(unittest.TestCase):

    def test_construct(self):
        client = Vectara(api_key="asdf")
