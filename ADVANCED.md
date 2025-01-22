## Advanced Usage

### Retries

The SDK includes **automatic retry handling** with exponential backoff to enhance reliability. A request will be retried if it meets the following conditions:
1. The response status code indicates a retriable error.
2. The number of retry attempts is less than the configured retry limit (default: `2`).

#### Retriable HTTP Status Codes
The following status codes are considered retriable:
- **[408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408)**: Request Timeout
- **[429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)**: Too Many Requests
- **[5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500)**: Internal Server Errors

#### Configuring Retries
You can customize the retry behavior using the `max_retries` option in `request_options`.

```python
client.query(
    query="Tell me about AI.",
    request_options={"max_retries": 3}  # Configure the maximum number of retries
)
```

### Timeouts
The SDK applies a **default timeout of 60 seconds** for all requests. You can adjust this timeout globally at the client level or for specific API calls.

#### Configuring a Global Timeout
Set the timeout for all SDK operations when initializing the client:

```python
from vectara import Vectara

client = Vectara(
    ...,
    timeout=30.0  # Set a 30-second timeout for all requests
)

```
#### Overriding Timeout Per Request
Customize the timeout for individual API calls using `request_options`:

```python
client.query(
    query="Tell me about AI.",
    request_options={"timeout_in_seconds": 10}  # Set a 10-second timeout for this request
)

```
### Custom HTTP Client
The SDK allows you to provide a custom `httpx.Client` to fine-tune network configurations, such as:

1. Using a proxy server.
2. Specifying a local transport address.
#### Example: Custom HTTP Client Configuration

```python
import httpx
from vectara import Vectara

client = Vectara(
    ...,
    httpx_client=httpx.Client(
        proxies="http://proxy.example.com:8080",
        transport=httpx.HTTPTransport(local_address="192.168.1.100"),
    )
)

```