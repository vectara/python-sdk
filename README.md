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
from vectara import Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.api_keys.create(
    name="name",
    api_key_role="serving",
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from vectara import AsyncVectara

client = AsyncVectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main() -> None:
    await client.api_keys.create(
        name="name",
        api_key_role="serving",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from vectara.core.api_error import ApiError

try:
    client.api_keys.create(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Streaming

The SDK supports streaming responses, as well, the response will be a generator that you can loop over.

```python
from vectara import (
    ChatParameters,
    CitationParameters,
    ContextConfiguration,
    CustomerSpecificReranker,
    GenerationParameters,
    KeyedSearchCorpus,
    ModelParameters,
    SearchCorporaParameters,
    Vectara,
)

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.chats.create_stream(
    query="string",
    search=SearchCorporaParameters(
        corpora=[KeyedSearchCorpus()],
        offset=1,
        limit=1,
        context_configuration=ContextConfiguration(),
        reranker=CustomerSpecificReranker(),
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
    chat=ChatParameters(
        store=True,
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
response = client.chats.list()
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
client.api_keys.create(..., {
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
client.api_keys.create(..., {
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
