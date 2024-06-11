# Vectara Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

The Vectara Python Library provides convenient access to the Vectara API from applications written in Python.

## Installation

```sh
pip install vectara
# or
poetry add vectara
```

## Usage
Simply import `Vectara` and start making calls to our API.

```python
from vectara.client import Vectara
from vectara import SearchCorporaParameters

client = Vectara(
    api_key="YOUR_API_KEY" # defaults to VECTARA_API_KEY
)
client.query(
    query="Am I allowed to bring pets to work?",
    search=SearchCorporaParameters(
        offset=10,
        limit=10
    ),
)
```

## Async Client
The SDK also exports an async client so that you can make non-blocking calls to our API.

```python
import asyncio

from vectara.client import AsyncVectara
from vectara import SearchCorporaParameters

client = AsyncVectara(
  api_key="YOUR_API_KEY" # defaults to VECTARA_API_KEY
)

async def main() -> None:
    await client.query(
        query="Am I allowed to bring pets to work?",
        search=SearchCorporaParameters(
            offset=10,
            limit=10
        ),
    )
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

## Streaming
The SDK supports streaming endpoints. To take advantage of this feature for queries or chats, pass in the argument 
`stream_response=True`. 

```python
from vectara import GenerationParameters, ModelParameters

response = client.chats.start(
    stream_response=True,
    query="How can I use the Vectara platform?",
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
        enable_factual_consistency_score=True,
    ),
)

for item in response:
    print(chunk)
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

## Exception Handling
All errors thrown by the SDK will be subclasses of [`ApiError`](./src/vectara/core/api_error.py):

```python
try:
    client.query(...)
except corpora.core.ApiError as e: # Handle all errors
  print(e.status_code)
  print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object. For example, `corpora.list` will return a generator over `Corpus` and handle the pagination behind the scenes:

```python
for corpus in client.corpus.list():
    print(corpus)
```

you could also iterate page-by-page:

```python
for page in client.corpus.list().iter_pages():
    print(page.items)
```

or manually: 

```python
pager = client.corpus.list()
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
