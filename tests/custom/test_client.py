import pytest

import vectara
from vectara.client import Vectara

client = Vectara()

def test_query() -> None:
    response = client.queries.query(
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

def test_query_stream() -> None:
    response = client.queries.query_stream(
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
    for message in response: 
        if message.type == "generation_chunk": 
            print(message.generation_chunk, end='')
