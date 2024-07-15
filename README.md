# Vectara Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)
[![pypi](https://img.shields.io/pypi/v/vectara)](https://pypi.python.org/pypi/vectara)

The Vectara Python library provides convenient access to the Vectara API from Python.

## Installation

```sh
pip install vectara
```

## Usage

Instantiate and use the client with the following:

```python
from vectara import (
    CitationParameters,
    ContextConfiguration,
    GenerationParameters,
    KeyedSearchCorpus,
    ModelParameters,
    SearchCorporaParameters,
    SearchReranker_CustomerReranker,
)
from vectara.client import Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    token="YOUR_TOKEN",
)
response = client.queries.query_stream(
    query="string",
    search=SearchCorporaParameters(
        corpora=[KeyedSearchCorpus()],
        offset=1,
        limit=1,
        context_configuration=ContextConfiguration(),
        reranker=SearchReranker_CustomerReranker(),
    ),
    generation=GenerationParameters(
        prompt_name="string",
        max_used_search_results=1,
        prompt_text="string",
        max_response_characters=1,
        response_language="auto",
        model_parameters=ModelParameters(
            max_tokens=1,
            temperature=1.1,
            frequency_penalty=1.1,
            presence_penalty=1.1,
        ),
        citations=CitationParameters(),
        enable_factual_consistency_score=True,
    ),
    stream_response=True,
)
for chunk in response:
    yield chunk
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from vectara import (
    CitationParameters,
    ContextConfiguration,
    GenerationParameters,
    KeyedSearchCorpus,
    ModelParameters,
    SearchCorporaParameters,
    SearchReranker_CustomerReranker,
)
from vectara.client import AsyncVectara

client = AsyncVectara(
    api_key="YOUR_API_KEY",
    token="YOUR_TOKEN",
)


async def main() -> None:
    response = await client.queries.query_stream(
        query="string",
        search=SearchCorporaParameters(
            corpora=[KeyedSearchCorpus()],
            offset=1,
            limit=1,
            context_configuration=ContextConfiguration(),
            reranker=SearchReranker_CustomerReranker(),
        ),
        generation=GenerationParameters(
            prompt_name="string",
            max_used_search_results=1,
            prompt_text="string",
            max_response_characters=1,
            response_language="auto",
            model_parameters=ModelParameters(
                max_tokens=1,
                temperature=1.1,
                frequency_penalty=1.1,
                presence_penalty=1.1,
            ),
            citations=CitationParameters(),
            enable_factual_consistency_score=True,
        ),
        stream_response=True,
    )
    async for chunk in response:
        yield chunk


asyncio.run(main())
```

## Authentication

The SDK supports two authentication mechanisms: 

### OAuth

To use OAuth2 authentication (recommended), instantiate the SDK by passing in `client_id` and `client_secret`. The SDK 
will handle fetching an access token and automatically refreshing the token before expiry. 

```python
from vectara.client import Vectara

client = Vectara(
    client_id="YOUR_CLIENT_ID", # Defaults to VECTARA_CLIENT_ID
    client_secret="YOUR_CLIENT_SECRET" # Defaults to VECTARA_CLIENT_SECRET
)
```

### API Key

To use an API key, pass in `api_key`:

```python
from vectara.client import Vectara

client = Vectara(
    api_key="YOUR_API_KEY"  # Defaults to VECTARA_API_KEY
)
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from .api_error import ApiError

try:
    client.queries.query_stream(...)
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
    GenerationParameters,
    KeyedSearchCorpus,
    ModelParameters,
    SearchCorporaParameters,
    SearchReranker_CustomerReranker,
)
from vectara.client import Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    token="YOUR_TOKEN",
)
response = client.queries.query_stream(
    query="string",
    search=SearchCorporaParameters(
        corpora=[KeyedSearchCorpus()],
        offset=1,
        limit=1,
        context_configuration=ContextConfiguration(),
        reranker=SearchReranker_CustomerReranker(),
    ),
    generation=GenerationParameters(
        prompt_name="string",
        max_used_search_results=1,
        prompt_text="string",
        max_response_characters=1,
        response_language="auto",
        model_parameters=ModelParameters(
            max_tokens=1,
            temperature=1.1,
            frequency_penalty=1.1,
            presence_penalty=1.1,
        ),
        citations=CitationParameters(),
        enable_factual_consistency_score=True,
    ),
    stream_response=True,
)
for chunk in response:
    yield chunk
```

## File Uploads
The SDK supports uploading documents via multiparm form data. File request parameters will be typed as [`core.File`](./src/core/file.py). File parameters 
can either be bytes or a tuple of (filename, bytes, content type). 

```python
response = client.upload(
  corpus_key="employee-handbook",
  file=open('Users/username/Documents/tmp/doc.rtf', 'rb')
)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from vectara.client import Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    token="YOUR_TOKEN",
)
response = client.corpora.list()
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
client.queries.query_stream(...,{
    max_retries=1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from vectara.client import Vectara

client = Vectara(..., { timeout=20.0 }, )


# Override timeout for a specific method
client.queries.query_stream(...,{
    timeout_in_seconds=1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.
```python
import httpx
from vectara.client import Vectara

client = Vectara(
    ...,
    http_client=httpx.Client(
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
