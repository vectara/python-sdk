import pytest
import os

import vectara
from vectara.client import Vectara

def test_oauth() -> None:
    oauth_client = Vectara(
        client_id="63gl02sr1ohf60o6qbiqumg86g",
        client_secret=os.getenv("VECTARA_CLIENT_SECRET")
    )
    response = oauth_client.queries.query(
        query="Can i bring my velociraptor to the office? Please explain in 5 paragraphs.",
        search=vectara.SearchCorporaParameters(
            corpora=[vectara.KeyedSearchCorpus(corpus_key="Test")],
            reranker=vectara.MmrReranker(diversity_bias=0.2)
        ),
        generation=vectara.GenerationParameters(
            prompt_name="vectara-summary-ext-24-05-sml",
            response_language="eng",
            max_used_search_results=7,
        ),
    )
    print(response.summary)