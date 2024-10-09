import unittest
import logging

from vectara.factory import Factory
from vectara.corpora.client import CorporaClient
from vectara import Vectara

class FactoryTest(unittest.TestCase):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)

    def test_query(self) -> None:
        self.logger.info("Starting test")

        client: Vectara = Factory().build()

        corpora_client: CorporaClient = client.corpora

        def list_corpora_gen():
            response = corpora_client.list(filter="company_names")
            for item in response:
                yield item

        for corpus in list_corpora_gen():
            self.logger.info(f"Found {corpus.name} with key {corpus.key}")