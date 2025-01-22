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

First, create an SDK client.<br />
You can use either an `api_key` or OAuth (`client_id` and `client_secret`) for [authentication](https://docs.vectara.com/docs/console-ui/api-access-overview).

```python
from vectara import Vectara

# creating the client using API key
client = Vectara(
    api_key="YOUR_API_KEY"
)
    
# creating the client using oauth credentials
client = Vectara(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)  
```

If you don't already have a corpus, you can create it using the SDK:

```python
client.corpora.create(name="my-corpus", key="my-corpus-key")
```
  
### Add a document to a corpus
You can add documents to a corpus in two formats: [structured](https://docs.vectara.com/docs/learn/select-ideal-indexing-api#structured-document-definition) or [core](https://docs.vectara.com/docs/learn/select-ideal-indexing-api#core-document-definition).<br/> For more information, refer to the [Indexing Guide](https://docs.vectara.com/docs/learn/select-ideal-indexing-api).

Here is an example for adding a Structured document
  ```python
  from vectara import StructuredDocument, StructuredDocumentSection
  client.documents.create(
      corpus_key="my-corpus-key",
      request=StructuredDocument(
          id="my-doc-id",
          type="structured",
          sections=[
            StructuredDocumentSection(
                id="id_1",
                title="A nice title.",
                text="I'm a nice document section.",
                metadata={'section': '1.1'}
            ),
            StructuredDocumentSection(
                id="id_2",
                title="Another nice title.",
                text="I'm another document section on something else.",
                metadata={'section': '1.2'}
            ),
          ],
          metadata={'url': 'https://example.com'}
      ),
  )
  ```


And here is one with Core document:
```python
from vectara import CoreDocument, CoreDocumentPart

client.documents.create(
    corpus_key="my-corpus-key",
    request=CoreDocument(
        id="my-doc-id",
        type="core",
        document_parts=[
            CoreDocumentPart(
                text="I'm a first document part.",
                metadata={'author': 'Ofer'}
            )
            CoreDocumentPart(
                text="I'm a second document part.",
                metadata={'author': 'Adeel'}
            )
        ],
        metadata={'url': 'https://example.com'}
    ),
)
```

### Upload a file to the corpus
In addition to creating a document as shown above (using StructuredDocument or CoreDocument), you can also upload files (such as PDFs or Word Documents) directly to Vectara.
In this case Vectara will parse the files automatically, extract text and metadata, chunk them and add them to the corpus.

Using the SDK you need to provide both the file name, the binary content of the file, and the content_type, as follows:

```python
filename = "examples.pdf"
with open(filename, "rb") as f:
    content = f.read()

client.upload.file(
    'my-corpus-key', 
    file=content,
    filename=filename,
    metadata={"author": "Adeel"}
)
```


### Querying the corpora
With the SDK it's super easy to run a query from one or more corpora. For more detailed information, see this [Query API guide](https://docs.vectara.com/docs/api-reference/search-apis/search)

A query uses two important objects:
* The `SearchCorporaParameters` object defines parameters for search such as hybrid search, metadata filtering or reranking
* The `GenerationParameters` object defines parameters for the generative step.

Here is an example query for our corpus above:

```python 
search = SearchCorporaParameters(
        corpora=[
            KeyedSearchCorpus(
                corpus_key="my-corpus-key",
                metadata_filter="",
                lexical_interpolation=0.005,
            )
        ],
        context_configuration=ContextConfiguration(
            sentences_before=2,
            sentences_after=2,
        ),
        reranker=CustomerSpecificReranker(
            reranker_id="rnk_272725719"
        ),
    )
generation = GenerationParameters(
        response_language="eng",
        enable_factual_consistency_score=True,
    )

client.query(
    query="Am I allowed to bring pets to work?",
    search=search,
    generation=generation
    
)
```
 
### Using Chat

Vectara [chat](https://docs.vectara.com/docs/api-reference/chat-apis/chat-apis-overview) provides a way to automatically store chat history to support multi-turn conversations.

Here is an example of how to start a chat with the SDK:

```python
from vectara import SearchCorporaParameters    
search = SearchCorporaParameters(
        corpora=[
            KeyedSearchCorpus(
                corpus_key="test-corpus",
                metadata_filter="",
                lexical_interpolation=0.005,
            )
        ],
        context_configuration=ContextConfiguration(
            sentences_before=2,
            sentences_after=2,
        ),
        reranker=CustomerSpecificReranker(
            reranker_id="rnk_272725719"
        ),
    )
generation = GenerationParameters(
        response_language="eng",
        citations=CitationParameters(
            style="none",
        ),
        enable_factual_consistency_score=True,
    )
chat = ChatParameters(store=True)

session = client.create_chat_session(
    search=search,
    generation=generation,
    chat_config=chat,
)

response_1 = session.chat(query="Tell me about machine learning.")
print(response_1.answer)
response_2 = session.chat(query="what is generative AI?")
print(response_2.answer)
```

Note that we used the `create_chat_session` with `chat_config` set for storing chat history. The resulting session can then be used for turn-by-turn chat, simply by using the `chat()` method of the session object.


### Streaming

The SDK supports streaming responses for both query and chat. When using streaming, the response will be a generator that you can iterate.

Here's an example of calling `query_stream`:
  
Streaming the query response
```python
from vectara import SearchCorporaParameters
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
    if chunk.type == 'generation_chunk':
        print(chunk.generation_chunk)
    if chunk.type == "search_results":
        print(chunk.search_results)
```

And streaming the chat response:

```python
from vectara import SearchCorporaParameters

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
    if chunk.type == 'generation_chunk':
        print(chunk.generation_chunk)
    if chunk.type == "search_results":
        print(chunk.search_results)   
    if chunk.type == "chat_info":
        print(chunk.chat_id)
        print(chunk.turn_id)
```

## Additional Functionality
There is a lot more functionality packed into the SDK, matching [all API endpoints](https://docs.vectara.com/docs/rest-api) that are available in Vectara including for things like managing documents, corpora, api keys, users, and even for query history retrieval. 


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

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
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

For more information related to customization, Timeouts and Retries in the SDK, refer to the [Advanced Usage Guide](./ADVANCED.md)


### Using the SDK in Different Contexts
The Python library can be used in a number of environments with different requirements:

1. **Notebooks** - using implicit configuration from a users home directory
2. **Docker Environments** - using ENV variables for configuration
3. **Complex Applications** - allowing explicit configuration from mutable stores (e.g. RDBMS / NoSQL)

For more details, refer to the [Configuration Guide](./CONFIGURATION.md)

## Author

👤 **Vectara**

- Website: https://vectara.com
- Twitter: [@vectara](https://twitter.com/vectara)
- GitHub: [@vectara](https://github.com/vectara)
- LinkedIn: [@vectara](https://www.linkedin.com/company/vectara/)
- Discord: [@vectara](https://discord.gg/GFb8gMz6UH)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br/>
Feel free to check [issues page](https://github.com/vectara/python-sdk/issues). You can also take a look at the [contributing guide](./CONTRIBUTING.md).

## Show your support

Give a ⭐️ if this project helped you!