# Vectara Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fvectara%2Fpython-sdk)
[![pypi](https://img.shields.io/pypi/v/vectara)](https://pypi.python.org/pypi/vectara)

The Vectara Python library provides convenient access to the Vectara API from Python.

## Documentation

API reference documentation is available [here](https://vectara.docs.buildwithfern.com/).

## Installation

```sh
pip install vectara
```

## Reference

A full reference for this library is available [here](./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from vectara import SearchCorporaParameters, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.query(
    query="Am I allowed to bring pets to work?",
    search=SearchCorporaParameters(),
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from vectara import AsyncVectara, SearchCorporaParameters

client = AsyncVectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main() -> None:
    await client.query(
        query="Am I allowed to bring pets to work?",
        search=SearchCorporaParameters(),
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from vectara.core.api_error import ApiError

try:
    client.query(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Streaming

The SDK supports streaming responses, as well, the response will be a generator that you can loop over.

```python
from vectara import (
    CitationParameters,
    ContextConfiguration,
    CustomerSpecificReranker,
    GenerationParameters,
    ModelParameters,
    Vectara,
)
from vectara.corpora import SearchCorpusParameters

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.corpora.query_stream(
    corpus_key="string",
    request_timeout=1,
    request_timeout_millis=1,
    query="string",
    search=SearchCorpusParameters(
        custom_dimensions={"string": 1.1},
        metadata_filter="string",
        lexical_interpolation=1.1,
        semantics="default",
        offset=1,
        limit=1,
        context_configuration=ContextConfiguration(
            characters_before=1,
            characters_after=1,
            sentences_before=1,
            sentences_after=1,
            start_tag="string",
            end_tag="string",
        ),
        reranker=CustomerSpecificReranker(
            reranker_id="string",
            reranker_name="string",
            limit=1,
            cutoff=1.1,
        ),
    ),
    generation=GenerationParameters(
        generation_preset_name="string",
        prompt_name="string",
        max_used_search_results=1,
        prompt_template="string",
        prompt_text="string",
        max_response_characters=1,
        response_language="auto",
        model_parameters=ModelParameters(
            max_tokens=1,
            temperature=1.1,
            frequency_penalty=1.1,
            presence_penalty=1.1,
        ),
        citations=CitationParameters(
            style="none",
            url_pattern="string",
            text_pattern="string",
        ),
        enable_factual_consistency_score=True,
    ),
)
for chunk in response:
    yield chunk
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from vectara import Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.corpora.list(
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page
```

## Advanced

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retriable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retriable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.query(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from vectara import Vectara

client = Vectara(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.query(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.
```python
import httpx
from vectara import Vectara

client = Vectara(
    ...,
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
