# Vectara Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

The Vectara Python Library provides convenient access to the Vectara API from applications written in Python.

## Installation

```sh
pip install --upgrade vectara
```

## Usage

```python
from vectara.client import Vectara

client = Vectara(
    ...
)
```

## Async Client

```python
from vectara.client import AsyncVectara

client = AsyncVectara(
    ...
)
```

## Authentication

To use OAuth2 authentication (recommended), use `client_id` and `client_secret`:

```python
from vectara.client import Vectara

client = Vectara(
    client_id="...",
    client_secret="..."
)
```

To use an API key, use `api_key`:

```python
from vectara.client import Vectara

client = Vectara(
    api_key="..."
)
```

## Exception Handling
All errors thrown by the SDK will be subclasses of [`ApiError`](./src/vectara/core/api_error.py):

```python
try:
    client.corpora.list_corpora(...)
except corpora.core.ApiError as e: # Handle all errors
  print(e.status_code)
  print(e.body)
```

## Streaming
The SDK supports streaming endpoints. To take advantage of this feature for queries or chats, look for the `_stream` suffix:

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
)
from vectara.client import Vectara

...

response = client.chats.create_stream(
    query="string",
    search=SearchCorporaParameters(
        corpora=[KeyedSearchCorpus()],
        offset=0,
        limit=10,
        context_configuration=ContextConfiguration(),
        reranker=CustomerSpecificReranker(),
    ),
    generation=GenerationParameters(
        prompt_name="vectara-summary-ext-v1.2.0",
        max_used_search_results=10,
        prompt_text="[\n ... {\"role\": \"user\", \"content\": \"Generate a summary for the query '\''${vectaraQuery}'\'' based on the above results.\"} ... \n] \n",
        max_response_characters=300,
        response_language="auto",
        model_parameters=ModelParameters(
            max_tokens=2,
            temperature=0.4,
            frequency_penalty=0.9,
            presence_penalty=0.2,
        ),
        citations=CitationParameters(),
        enable_factual_consistency_score=True,
    ),
    chat=ChatParameters(
        store=True,
    ),
)
for item in response:
    print(chunk)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object. For example, `corpora.list` will return a generator over `Corpus` and handle the pagination behind the scenes:

```python
for corpus in client.corpora.list():
    print(corpus)
```

you could also iterate page-by-page:

```python
for page in client.corpora.list().iter_pages():
    print(page.items)
```

or manually: 

```python
pager = client.corpora.list()
# First page
print(pager.items)
# Second page
pager = pager.next_page()
print(pager.items)
```

## Advanced 

### Timeouts

By default, requests time out after 60 seconds. You can configure this with a
timeout option at the client or request level.

```python
from vectara.client import Vectara

client = Vectara(
    ...,
    # All timeouts are 20 seconds
    timeout=20.0,
)

# Override timeout for a specific method
client.corpora.list_corpora(..., {
    timeout_in_seconds=20.0
})
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be
retried as long as the request is deemed retriable and the number of retry attempts has not grown larger
than the configured retry limit (default: 2).

A request is deemed retriable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.corpora.list_corpora(..., {
    max_retries=1
})
```

### Custom HTTP client

You can override the httpx client to customize it for your use-case. Some common use-cases
include support for proxies and transports.

```python
import httpx

from vectara.client import Vectara

client = Vectara(...,
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Beta Status

This SDK is in beta, and there may be breaking changes between versions without a major 
version update. Therefore, we recommend pinning the package version to a specific version. 
This way, you can install the same version each time without breaking changes.