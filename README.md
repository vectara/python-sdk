# Vectara Python SDK

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fvectara%2Fpython-sdk)
[![pypi](https://img.shields.io/pypi/v/vectara)](https://pypi.python.org/pypi/vectara)

The Vectara Python SDK provides convenient access to the Vectara API for building powerful AI applications.

---

## Installation

Install the library via pip:

```bash
pip install vectara
```
## Getting Started

### API Generated Documentation
API reference documentation is available [here](https://vectara.docs.buildwithfern.com/).

### Examples
Complete examples can be found in the [Getting Started notebooks](./examples/01_getting_started).

### Usage

* Querying the corpora
    ```python
    from vectara import SearchCorporaParameters, Vectara
    client = Vectara(
        api_key="YOUR_API_KEY",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    )
    
    search = SearchCorporaParameters(
        corpora=[...],
        ...
    )
    generation = GenerationParameters(...)
    
    client.query(
        query="Am I allowed to bring pets to work?",
        search=search,
        generation=generation
        
    )
    ```
 
* Starting the chat session
   ```python
   from vectara import SearchCorporaParameters, Vectara
   client = Vectara(
       api_key="YOUR_API_KEY",
       client_id="YOUR_CLIENT_ID",
       client_secret="YOUR_CLIENT_SECRET",
   )
    
   search = SearchCorporaParameters(
       corpora=[...],
       ...
   )
   generation = GenerationParameters(...)
   chat_params = ChatParameters(store=True)

   session = client.create_chat_session(
       search=search_params,
       generation=generation_params,
       chat_config=chat_params,
   )
   
   response = session.chat(query="Tell me about machine learning.")
   print(response.answer)
   ```
  
### Streaming

The SDK supports streaming responses, as well, the response will be a generator that you can loop over.
  
* Streaming the query response
    ```python
    from vectara import SearchCorporaParameters, Vectara
    client = Vectara(
       api_key="YOUR_API_KEY",
       client_id="YOUR_CLIENT_ID",
       client_secret="YOUR_CLIENT_SECRET",
    )
    
    search = SearchCorporaParameters(
       corpora=[...],
       ...
    )
    generation = GenerationParameters(...)
    
    response = client.query_stream(
       query="Am I allowed to bring pets to work?",
       search=search,
       generation=generation
        
    )
    for chunk in response:
       yield chunk
    ```

* Streaming the chat response
    ```python
    from vectara import SearchCorporaParameters, Vectara
    client = Vectara(
       api_key="YOUR_API_KEY",
       client_id="YOUR_CLIENT_ID",
       client_secret="YOUR_CLIENT_SECRET",
    )
    
    search = SearchCorporaParameters(
       corpora=[...],
       ...
    )
    generation = GenerationParameters(...)
    chat_params = ChatParameters(store=True)
    
    session = client.create_chat_session(
       search=search_params,
       generation=generation_params,
       chat_config=chat_params,
    )
    
    response = session.chat_stream(query="Tell me about machine learning.")
    for chunk in response:
      yield response
    ```

### Exception Handling

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

### Advance Usage

For more information related to customization, Timeouts and Retries, refer to the [Advanced Usage Guide](./advanced.md)


### Using the SDK in Different Contexts
The Python library is designed to run in a number of environments with different requirements:

1. **Notebooks** - using implicit configuration from a users home directory
2. **Docker Environments** - using ENV variables for configuration
3. **Complex Applications** - allowing explicit configuration from mutable stores (e.g. RDBMS / NoSQL)

For more details, refer to the [Configuration Guide](./configuration.md)

## Author

👤 **Vectara**

- Website: https://vectara.com
- Twitter: [@vectara](https://twitter.com/vectara)
- GitHub: [@vectara](https://github.com/vectara)
- LinkedIn: [@vectara](https://www.linkedin.com/company/vectara/)
- Discord: [@vectara](https://discord.gg/GFb8gMz6UH)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br/>
Feel free to check [issues page](https://github.com/vectara/python-sdk/issues). You can also take a look at the [contributing guide](./contributing.md).

## Show your support

Give a ⭐️ if this project helped you!