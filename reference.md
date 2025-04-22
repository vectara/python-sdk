# Reference
## Corpora
<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List corpora in the account. The returned corpus objects contain less
detail compared to those retrieved the direct corpus retrieval operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.corpora.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of corpora to return at one time.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — A regular expression to filter the corpora by their name or summary.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of corpora after the limit has been reached.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a corpus, which is a container to store documents and associated metadata. Here, you 
define the unique `corpus_key` that identifies the corpus. The `corpus_key` can be custom-defined 
following your preferred naming convention, allowing you to easily manage the corpus's data and 
reference it in queries. For more information, see 
[Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.corpora.create(key='my-corpus', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `CorpusKey` 
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name for the corpus. This value defaults to the key.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the corpus.
    
</dd>
</dl>

<dl>
<dd>

**save_history:** `typing.Optional[bool]` — Indicates whether to save corpus queries to query history by default.
    
</dd>
</dl>

<dl>
<dd>

**queries_are_answers:** `typing.Optional[bool]` — Queries made to this corpus are considered answers, and not questions.
    
</dd>
</dl>

<dl>
<dd>

**documents_are_questions:** `typing.Optional[bool]` — Documents inside this corpus are considered questions, and not answers.
    
</dd>
</dl>

<dl>
<dd>

**encoder_id:** `typing.Optional[str]` — *Deprecated*: Use `encoder_name` instead.
    
</dd>
</dl>

<dl>
<dd>

**encoder_name:** `typing.Optional[str]` — The encoder used by the corpus, `boomerang-2023-q3`.
    
</dd>
</dl>

<dl>
<dd>

**filter_attributes:** `typing.Optional[typing.Sequence[FilterAttribute]]` 

The new filter attributes of the corpus. 
If unset then the corpus will not have filter attributes.
    
</dd>
</dl>

<dl>
<dd>

**custom_dimensions:** `typing.Optional[typing.Sequence[CorpusCustomDimension]]` 

A custom dimension is an additional numerical field attached to a document part. You
can then multiply this numerical field with a query time custom dimension of the same
name. This allows boosting (or burying) document parts for arbitrary reasons.
This feature is only enabled for Pro and Enterprise customers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get metadata about a corpus. This operation does not search the corpus contents. 
Specify the `corpus_key` to identify the corpus whose metadata you want to 
retrieve. The `corpus_key` is created when the corpus is set up, either through
the Vectara Console UI or the Create Corpus API. For more information, 
see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.corpora.get(corpus_key='my-corpus', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a corpus and all its associated data. The `corpus_key` uniquely identifies 
the corpus. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.corpora.delete(corpus_key='my-corpus', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enable, disable, or update the name and description of a corpus. This lets you
manage data availability without deleting the corpus, which is useful for 
maintenance and security purposes. The `corpus_key` uniquely identifies the corpus. 
For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition). 
Consider updating the name and description of a corpus dynamically to help keep your data 
aligned with changing business needs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.corpora.update(corpus_key='my-corpus', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus to update.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Set whether or not the corpus is enabled. If unset then the corpus will remain in the same state.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name for the corpus. If unset or null, then the corpus will remain in the same state.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the corpus. If unset or null, then the corpus will remain in the same state.
    
</dd>
</dl>

<dl>
<dd>

**save_history:** `typing.Optional[bool]` — Indicates whether to save corpus queries to query history by default.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">reset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resets a corpus, which removes all documents and data from the specified corpus, 
while keeping the corpus itself. The `corpus_key` uniquely identifies the corpus. 
For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.corpora.reset(corpus_key='my-corpus', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus to reset.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">replace_filter_attributes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace the filter attributes of a corpus. This does not happen immediately, as
this operation creates a job that completes asynchronously. These new filter 
attributes will not work until the job completes.

You can monitor the status of the filter change using the returned job ID. The 
`corpus_key` uniquely identifies the corpus. For more information, see 
[Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
from vectara import FilterAttribute
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.corpora.replace_filter_attributes(corpus_key='my-corpus', filter_attributes=[FilterAttribute(name='Title', level="document", type="integer", )], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus having its filters replaced.
    
</dd>
</dl>

<dl>
<dd>

**filter_attributes:** `typing.Sequence[FilterAttribute]` — The new filter attributes.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">compute_size</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the current size of a corpus, including number of documents, parts, and characters.
The `corpus_key` uniquely identifies the corpus. For more information, see 
[Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.corpora.compute_size(corpus_key='my-corpus', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus to compute size for.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search a single corpus with a straightforward query request, specifying the corpus key and query parameters.
* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is 
[created in the Vectara Console UI](https://docs.vectara.com/docs/console-ui/creating-a-corpus) or the [Create Corpus API definition](https://docs.vectara.com/docs/api-reference/admin-apis/create-corpus). When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
* Enter the search `query` string for the corpus, which is the question you want to ask.
* Set the maximum number of results (`limit`) to return. **Default**: 10, **minimum**: 1
* Define the `offset` position from which to start in the result set.

For more detailed information, see this [Query API guide](https://docs.vectara.com/docs/api-reference/search-apis/search).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.corpora.search(corpus_key='my-corpus', query='query', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus to query.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The search query string for the corpus, which is the question the user is asking.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The position from which to start in the result set.
    
</dd>
</dl>

<dl>
<dd>

**save_history:** `typing.Optional[bool]` — Indicates whether to save the query in the query history.
    
</dd>
</dl>

<dl>
<dd>

**intelligent_query_rewriting:** `typing.Optional[bool]` 

Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to
extract metadata filter and rewrite the query to improve search results.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">query_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform an advanced query on a specific corpus to find relevant results, highlight relevant snippets, and use Retrieval Augmented Generation:

* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is [created in the Vectara Console UI](https://docs.vectara.com/docs/console-ui/creating-a-corpus) or the [Create Corpus API definition](https://docs.vectara.com/docs/api-reference/admin-apis/create-corpus). When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
* Customize your search by specifying the query text (`query`), pagination details (`offset` and `limit`), and metadata filters (`metadata_filter`) to tailor your search results. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#query-definition)
* Leverage advanced search capabilities like reranking (`reranker`) and Retrieval Augmented Generation (RAG) (`generation`) for enhanced query performance. Generation is opt in by setting the `generation` property. By excluding the property or by setting it to null, the response
will not include generation. [Learn more](https://docs.vectara.com/docs/learn/grounded-generation/configure-query-summarization).
* Use hybrid search to achieve optimal results by setting different values for `lexical_interpolation` (e.g., `0.025`). [Learn more](https://docs.vectara.com/docs/learn/hybrid-search)
* Specify Vectara's RAG-focused LLM (Mockingbird) for the `generation_preset_name`. [Learn more](https://docs.vectara.com/docs/learn/mockingbird-llm)
* Use advanced summarization options that utilize detailed summarization parameters such as `max_response_characters`, `temperature`, and `frequency_penalty` for generating precise and relevant summaries. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#advanced-summarization-options)

For more detailed information, see [Query API guide](https://docs.vectara.com/docs/api-reference/search-apis/search).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.corpora.query_stream(corpus_key='my-corpus', query='query', )
for chunk in response.data:
    yield chunk

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus to query.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The search query string, which is the question the user is asking.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[SearchCorpusParameters]` — The parameters to search one corpus.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[GenerationParameters]` 
    
</dd>
</dl>

<dl>
<dd>

**save_history:** `typing.Optional[bool]` — Indicates whether to save the query to query history.
    
</dd>
</dl>

<dl>
<dd>

**intelligent_query_rewriting:** `typing.Optional[bool]` 

Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to
extract metadata filter and rewrite the query to improve search results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform an advanced query on a specific corpus to find relevant results, highlight relevant snippets, and use Retrieval Augmented Generation:

* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is [created in the Vectara Console UI](https://docs.vectara.com/docs/console-ui/creating-a-corpus) or the [Create Corpus API definition](https://docs.vectara.com/docs/api-reference/admin-apis/create-corpus). When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
* Customize your search by specifying the query text (`query`), pagination details (`offset` and `limit`), and metadata filters (`metadata_filter`) to tailor your search results. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#query-definition)
* Leverage advanced search capabilities like reranking (`reranker`) and Retrieval Augmented Generation (RAG) (`generation`) for enhanced query performance. Generation is opt in by setting the `generation` property. By excluding the property or by setting it to null, the response
will not include generation. [Learn more](https://docs.vectara.com/docs/learn/grounded-generation/configure-query-summarization).
* Use hybrid search to achieve optimal results by setting different values for `lexical_interpolation` (e.g., `0.025`). [Learn more](https://docs.vectara.com/docs/learn/hybrid-search)
* Specify Vectara's RAG-focused LLM (Mockingbird) for the `generation_preset_name`. [Learn more](https://docs.vectara.com/docs/learn/mockingbird-llm)
* Use advanced summarization options that utilize detailed summarization parameters such as `max_response_characters`, `temperature`, and `frequency_penalty` for generating precise and relevant summaries. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#advanced-summarization-options)

For more detailed information, see [Query API guide](https://docs.vectara.com/docs/api-reference/search-apis/search).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.corpora.query(corpus_key='my-corpus', query='query', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus to query.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The search query string, which is the question the user is asking.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[SearchCorpusParameters]` — The parameters to search one corpus.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[GenerationParameters]` 
    
</dd>
</dl>

<dl>
<dd>

**save_history:** `typing.Optional[bool]` — Indicates whether to save the query to query history.
    
</dd>
</dl>

<dl>
<dd>

**intelligent_query_rewriting:** `typing.Optional[bool]` 

Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to
extract metadata filter and rewrite the query to improve search results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Queries
<details><summary><code>client.queries.<a href="src/vectara/queries/client.py">query_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform a multipurpose query across to retrieve relevant information from one or more corpora and generate a response using Retrieval Augmented Generation (RAG).

* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is [created in the Vectara Console UI](https://docs.vectara.com/docs/console-ui/creating-a-corpus) or the [Create Corpus API definition](https://docs.vectara.com/docs/api-reference/admin-apis/create-corpus). When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
* Customize your search by specifying the query text (`query`), pagination details (`offset` and `limit`), and metadata filters (`metadata_filter`) to tailor your search results. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#query-definition)
* Leverage advanced search capabilities like reranking (`reranker`) and opt-in Retrieval Augmented Generation (RAG) (`generation`) for enhanced query performance. Generation is opt in by setting the `generation` property. By excluding the property or by setting it to null, the response
will not include generation. [Learn more](https://docs.vectara.com/docs/learn/grounded-generation/configure-query-summarization)
* Specify Vectara's RAG-focused LLM (Mockingbird) for the `generation_preset_name`. [Learn more](https://docs.vectara.com/docs/learn/mockingbird-llm)
* Use advanced summarization options that utilize detailed summarization parameters such as `max_response_characters`, `temperature`, and `frequency_penalty` for generating precise and relevant summaries. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#advanced-summarization-customization-options)
* Customize citation formats in summaries using the `citations` object to include numeric, HTML, or Markdown links. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#citation-format-in-summary)

For more detailed information, see this [Query API guide](https://docs.vectara.com/docs/api-reference/search-apis/search).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
from vectara import SearchCorporaParameters
from vectara import KeyedSearchCorpus
from vectara import ContextConfiguration
from vectara import CustomerSpecificReranker
from vectara import GenerationParameters
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.queries.query_stream(query='What is a hallucination?', search=SearchCorporaParameters(corpora=[KeyedSearchCorpus(corpus_key='corpus_key', metadata_filter='', lexical_interpolation=0.005, )], context_configuration=ContextConfiguration(sentences_before=2, sentences_after=2, ), reranker=CustomerSpecificReranker(reranker_id='rnk_272725719', ), ), generation=GenerationParameters(response_language="eng", enable_factual_consistency_score=True, ), )
for chunk in response.data:
    yield chunk

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — The search query string, which is the question the user is asking.
    
</dd>
</dl>

<dl>
<dd>

**search:** `SearchCorporaParameters` 
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[GenerationParameters]` 
    
</dd>
</dl>

<dl>
<dd>

**save_history:** `typing.Optional[bool]` — Indicates whether to save the query to query history.
    
</dd>
</dl>

<dl>
<dd>

**intelligent_query_rewriting:** `typing.Optional[bool]` 

Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to
extract metadata filter and rewrite the query to improve search results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queries.<a href="src/vectara/queries/client.py">query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform a multipurpose query across to retrieve relevant information from one or more corpora and generate a response using Retrieval Augmented Generation (RAG).

* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is [created in the Vectara Console UI](https://docs.vectara.com/docs/console-ui/creating-a-corpus) or the [Create Corpus API definition](https://docs.vectara.com/docs/api-reference/admin-apis/create-corpus). When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
* Customize your search by specifying the query text (`query`), pagination details (`offset` and `limit`), and metadata filters (`metadata_filter`) to tailor your search results. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#query-definition)
* Leverage advanced search capabilities like reranking (`reranker`) and opt-in Retrieval Augmented Generation (RAG) (`generation`) for enhanced query performance. Generation is opt in by setting the `generation` property. By excluding the property or by setting it to null, the response
will not include generation. [Learn more](https://docs.vectara.com/docs/learn/grounded-generation/configure-query-summarization)
* Specify Vectara's RAG-focused LLM (Mockingbird) for the `generation_preset_name`. [Learn more](https://docs.vectara.com/docs/learn/mockingbird-llm)
* Use advanced summarization options that utilize detailed summarization parameters such as `max_response_characters`, `temperature`, and `frequency_penalty` for generating precise and relevant summaries. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#advanced-summarization-customization-options)
* Customize citation formats in summaries using the `citations` object to include numeric, HTML, or Markdown links. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#citation-format-in-summary)

For more detailed information, see this [Query API guide](https://docs.vectara.com/docs/api-reference/search-apis/search).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
from vectara import SearchCorporaParameters
from vectara import KeyedSearchCorpus
from vectara import ContextConfiguration
from vectara import CustomerSpecificReranker
from vectara import GenerationParameters
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.queries.query(query='What is a hallucination?', search=SearchCorporaParameters(corpora=[KeyedSearchCorpus(corpus_key='corpus_key', metadata_filter='', lexical_interpolation=0.005, )], context_configuration=ContextConfiguration(sentences_before=2, sentences_after=2, ), reranker=CustomerSpecificReranker(reranker_id='rnk_272725719', ), ), generation=GenerationParameters(response_language="eng", enable_factual_consistency_score=True, ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — The search query string, which is the question the user is asking.
    
</dd>
</dl>

<dl>
<dd>

**search:** `SearchCorporaParameters` 
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[GenerationParameters]` 
    
</dd>
</dl>

<dl>
<dd>

**save_history:** `typing.Optional[bool]` — Indicates whether to save the query to query history.
    
</dd>
</dl>

<dl>
<dd>

**intelligent_query_rewriting:** `typing.Optional[bool]` 

Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to
extract metadata filter and rewrite the query to improve search results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Upload
<details><summary><code>client.upload.<a href="src/vectara/upload/client.py">file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload files such as PDFs and Word Documents for automatic text extraction and metadata parsing.
The request expects a `multipart/form-data` format containing the following parts:
* `metadata` - (Optional) Specifies a JSON object representing any additional metadata to be associated with the extracted document. For example, `'metadata={"key": "value"};type=application/json'`
* `chunking_strategy` - (Optional) Specifies the chunking strategy for the platform to use. If you do not set this option, the platform uses the default strategy, which creates one chunk per sentence. You can explicitly set sentence chunking with `'chunking_strategy={"type":"sentence_chunking_strategy"};type=application/json'` or use max chars chunking with `'chunking_strategy={"type":"max_chars_chunking_strategy","max_chars_per_chunk":200};type=application/json'`
* `table_extraction_config` - (Optional) Specifies whether to extract table data from the uploaded file. If you do not set this option, the platform does not extract tables from PDF files. Example config, `'table_extraction_config={"extract_tables":true};type=application/json'`
* `file` - Specifies the file that you want to upload.
* `filename` - Specified as part of the file field with the file name that you want to associate with the uploaded file. For a curl example, use the following syntax: `'file=@/path/to/file/file.pdf;filename=desired_filename.pdf'`

For more detailed information, see this [File Upload API guide.](https://docs.vectara.com/docs/api-reference/indexing-apis/file-upload/file-upload)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.upload.file(corpus_key='my-corpus', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus of which to upload the file.
    
</dd>
</dl>

<dl>
<dd>

**file:** `from __future__ import annotations
core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Arbitrary object that will be attached as document metadata to the extracted document.
    
</dd>
</dl>

<dl>
<dd>

**chunking_strategy:** `typing.Optional[ChunkingStrategy]` 
    
</dd>
</dl>

<dl>
<dd>

**table_extraction_config:** `typing.Optional[TableExtractionConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — Optional multipart section to override the filename.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Documents
<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of documents stored in a specific corpus. This endpoint 
provides an overview of document metadata without returning the full content of 
each document.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.documents.list(corpus_key='my-corpus', )
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the queried corpus.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of documents to return at one time.
    
</dd>
</dl>

<dl>
<dd>

**metadata_filter:** `typing.Optional[str]` 

Filter documents by metadata. Uses the same expression as a query metadata filter, but only
allows filtering on document metadata.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of documents after the limit has been reached.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a document to a corpus. This endpoint supports two document formats, structured and core.

* **Structured** documents have a more conventional structure that provide document sections
and parts in a format created by Vectara's proprietary strategy automatically. You provide 
a logical document structure, and Vectara handles the partitioning.
* **Core** documents differ in that they follow an advanced, granular structure that 
explicitly defines each document part in an array. Each part becomes a distinct, 
searchable item in query results. You have precise control over the document structure 
and content.

For more details, see [Indexing](https://docs.vectara.com/docs/learn/select-ideal-indexing-api). 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
from vectara import StructuredDocument
from vectara import StructuredDocumentSection
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.documents.create(corpus_key='my-corpus-key', request=StructuredDocument(id='my-doc-id', sections=[StructuredDocumentSection(id=1, title='A nice title.', text="I'm a nice document section.", metadata={'section': '1.1'
}, ), StructuredDocumentSection(id=2, title='Another nice title.', text="I'm another document section on something else.", metadata={'section': '1.2'
}, )], metadata={'url': 'https://example.com'
}, ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the queried corpus.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateDocumentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the content and metadata of a specific document, identified by its 
unique `document_id` from a specific corpus.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.documents.get(corpus_key='my-corpus', document_id='document_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus containing the document to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 

The document ID of the document to retrieve.
This `document_id` must be percent encoded.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a document identified by its unique `document_id` from a specific 
corpus. This operation cannot be undone, so use it with caution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.documents.delete(corpus_key='my-corpus', document_id='document_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus with the document to delete.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 

The document ID of the document to delete.
This `document_id` must be percent encoded.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates document identified by its unique `document_id` from a specific 
corpus. The request body metadata is merged with the existing metadata, 
adding or modifying only the specified fields.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.documents.update(corpus_key='my-corpus', document_id='document_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus with the document to update.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 

The document ID of the document to update.
This `document_id` must be percent encoded.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 

The metadata for a document as an arbitrary object. Properties of this object
can be used by document level filter attributes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">update_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces metadata of a document identified by its unique `document_id` 
from a specific corpus.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.documents.update_metadata(corpus_key='my-corpus', document_id='document_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus with the document to update.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 

The document ID of the document to update.
This `document_id` must be percent encoded.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 

The metadata for a document as an arbitrary object. Properties of this object
can be used by document level filter attributes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">summarize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Summarize a document identified by its unique `document_id` from a specific corpus.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.documents.summarize(corpus_key='my-corpus', document_id='document_id', llm_name='llm_name', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `CorpusKey` — The unique key identifying the corpus containing the document to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 

The document ID of the document to retrieve.
This `document_id` must be percent encoded.
    
</dd>
</dl>

<dl>
<dd>

**llm_name:** `str` — The name of the LLM.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**prompt_template:** `typing.Optional[str]` 

The prompt template to use when generating the summary. 
Vectara manages both system and user roles and prompts for the generative
LLM out of the box by default. However, users can override the
`prompt_template` via this variable. The `prompt_template` is in the form of an
Apache Velocity template. For more details on how to configure the
`prompt_template`, see the [long-form documentation](https://docs.vectara.com/docs/prompts/vectara-prompt-engine).
    
</dd>
</dl>

<dl>
<dd>

**model_parameters:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Optional parameters for the specified model used when generating the summary.
    
</dd>
</dl>

<dl>
<dd>

**stream_response:** `typing.Optional[bool]` — Indicates whether the response should be streamed or not.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Chats
<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of previous chats in the Vectara account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.chats.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of chats after the limit has been reached.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">create_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a chat while specifying the default retrieval parameters used by the prompt.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
from vectara import SearchCorporaParameters
from vectara import KeyedSearchCorpus
from vectara import ContextConfiguration
from vectara import CustomerSpecificReranker
from vectara import GenerationParameters
from vectara import CitationParameters
from vectara import ChatParameters
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.chats.create_stream(query='What is a hallucination?', search=SearchCorporaParameters(corpora=[KeyedSearchCorpus(corpus_key='corpus_key', metadata_filter='', lexical_interpolation=0.005, )], context_configuration=ContextConfiguration(sentences_before=2, sentences_after=2, ), reranker=CustomerSpecificReranker(reranker_id='rnk_272725719', ), ), generation=GenerationParameters(response_language="eng", citations=CitationParameters(style="none", ), enable_factual_consistency_score=True, ), chat=ChatParameters(store=True, ), )
for chunk in response.data:
    yield chunk

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — The chat message or question.
    
</dd>
</dl>

<dl>
<dd>

**search:** `SearchCorporaParameters` 
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[GenerationParameters]` 
    
</dd>
</dl>

<dl>
<dd>

**chat:** `typing.Optional[ChatParameters]` 
    
</dd>
</dl>

<dl>
<dd>

**save_history:** `typing.Optional[bool]` — Indicates whether to save the chat in both the chat and query history. This overrides `chat.store`.
    
</dd>
</dl>

<dl>
<dd>

**intelligent_query_rewriting:** `typing.Optional[bool]` 

Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to
extract metadata filter and rewrite the query to improve search results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a chat while specifying the default retrieval parameters used by the prompt.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
from vectara import SearchCorporaParameters
from vectara import KeyedSearchCorpus
from vectara import ContextConfiguration
from vectara import CustomerSpecificReranker
from vectara import GenerationParameters
from vectara import CitationParameters
from vectara import ChatParameters
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.chats.create(query='What is a hallucination?', search=SearchCorporaParameters(corpora=[KeyedSearchCorpus(corpus_key='corpus_key', metadata_filter='', lexical_interpolation=0.005, )], context_configuration=ContextConfiguration(sentences_before=2, sentences_after=2, ), reranker=CustomerSpecificReranker(reranker_id='rnk_272725719', ), ), generation=GenerationParameters(response_language="eng", enable_factual_consistency_score=True, citations=CitationParameters(style="none", ), ), chat=ChatParameters(store=True, ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — The chat message or question.
    
</dd>
</dl>

<dl>
<dd>

**search:** `SearchCorporaParameters` 
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[GenerationParameters]` 
    
</dd>
</dl>

<dl>
<dd>

**chat:** `typing.Optional[ChatParameters]` 
    
</dd>
</dl>

<dl>
<dd>

**save_history:** `typing.Optional[bool]` — Indicates whether to save the chat in both the chat and query history. This overrides `chat.store`.
    
</dd>
</dl>

<dl>
<dd>

**intelligent_query_rewriting:** `typing.Optional[bool]` 

Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to
extract metadata filter and rewrite the query to improve search results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a chat summary to view what started the chat, but not subsequent turns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.chats.get(chat_id='chat_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The ID of the chat.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a chat and any turns it contains permanently.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.chats.delete(chat_id='chat_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The ID of the chat.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">list_turns</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all turns in a chat to see all message and response pairs that make up the dialog.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.chats.list_turns(chat_id='chat_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The ID of the chat.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">create_turns_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new turn in the chat. Each conversation has a series of `turn` objects, which are the sequence of message and response pairs that make up the dialog.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
from vectara import SearchCorporaParameters
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.chats.create_turns_stream(chat_id='chat_id', query='How can I use the Vectara platform?', search=SearchCorporaParameters(), )
for chunk in response.data:
    yield chunk

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The ID of the chat.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The chat message or question.
    
</dd>
</dl>

<dl>
<dd>

**search:** `SearchCorporaParameters` 
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[GenerationParameters]` 
    
</dd>
</dl>

<dl>
<dd>

**chat:** `typing.Optional[ChatParameters]` 
    
</dd>
</dl>

<dl>
<dd>

**save_history:** `typing.Optional[bool]` — Indicates whether to save the chat in both the chat and query history. This overrides `chat.store`.
    
</dd>
</dl>

<dl>
<dd>

**intelligent_query_rewriting:** `typing.Optional[bool]` 

Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to
extract metadata filter and rewrite the query to improve search results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">create_turns</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new turn in the chat. Each conversation has a series of `turn` objects, which are the sequence of message and response pairs that make up the dialog.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
from vectara import SearchCorporaParameters
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.chats.create_turns(chat_id='chat_id', query='How can I use the Vectara platform?', search=SearchCorporaParameters(), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The ID of the chat.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The chat message or question.
    
</dd>
</dl>

<dl>
<dd>

**search:** `SearchCorporaParameters` 
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[GenerationParameters]` 
    
</dd>
</dl>

<dl>
<dd>

**chat:** `typing.Optional[ChatParameters]` 
    
</dd>
</dl>

<dl>
<dd>

**save_history:** `typing.Optional[bool]` — Indicates whether to save the chat in both the chat and query history. This overrides `chat.store`.
    
</dd>
</dl>

<dl>
<dd>

**intelligent_query_rewriting:** `typing.Optional[bool]` 

Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to
extract metadata filter and rewrite the query to improve search results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">get_turn</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific turn from a chat, which is a message and response pair from the conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.chats.get_turn(chat_id='chat_id', turn_id='turn_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The ID of the chat.
    
</dd>
</dl>

<dl>
<dd>

**turn_id:** `str` — The ID of the turn.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">delete_turn</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a turn from a chat. This will delete all subsequent turns in the chat.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.chats.delete_turn(chat_id='chat_id', turn_id='turn_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The ID of the chat.
    
</dd>
</dl>

<dl>
<dd>

**turn_id:** `str` — The ID of the turn.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">update_turn</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a turn; used to disable or enable a chat.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.chats.update_turn(chat_id='chat_id', turn_id='turn_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chat_id:** `str` — The ID of the chat.
    
</dd>
</dl>

<dl>
<dd>

**turn_id:** `str` — The ID of the turn.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 

Indicates whether to disable a turn. It will disable this turn and all subsequent turns.
Enabling a turn is not implemented.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Llms
<details><summary><code>client.llms.<a href="src/vectara/llms/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List LLMs that can be used with query and chat endpoints. The LLM is not directly specified in a query,
but instead a `generation_preset_name` is used. The `generation_preset_name` property in generation parameters
can be found as the `name` property on the Generations Presets retrieved from `/v2/generation_presets`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.llms.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `typing.Optional[str]` — A regular expression to match names and descriptions of the LLMs.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` 

Used to retrieve the next page of LLMs after the limit has been reached.
This parameter is not needed for the first page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.llms.<a href="src/vectara/llms/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new LLM for use with query and chat endpoints
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.llms.create(name='name', model='model', uri='uri', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 

Name to reference the LLM.  This will be used in other endpoints (like query) when using this LLM.
If this name conflicts with a global LLM (a LLM that is precofnigured with the Vectara platform),
then it will override that LLM for all usages.
    
</dd>
</dl>

<dl>
<dd>

**model:** `str` — The model name to use with the API (e.g. gpt-4, claude-2, etc). This is used in the API request to the remote LLM provider.
    
</dd>
</dl>

<dl>
<dd>

**uri:** `str` — The URI endpoint for the API (can be OpenAI or any compatible API endpoint)
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the LLM.
    
</dd>
</dl>

<dl>
<dd>

**auth:** `typing.Optional[RemoteAuth]` 
    
</dd>
</dl>

<dl>
<dd>

**test_model_parameters:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Any additional parameters that are required for the LLM during the test call.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.llms.<a href="src/vectara/llms/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details about a specific LLM.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.llms.get(llm_id='llm_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**llm_id:** `str` — The name of the LLM to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.llms.<a href="src/vectara/llms/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a custom LLM connection. Built-in LLMs cannot be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.llms.delete(llm_id='llm_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**llm_id:** `str` — The name of the LLM to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Generation Presets
<details><summary><code>client.generation_presets.<a href="src/vectara/generation_presets/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List generation presets used for query or chat requests. Generation presets are
the build of properties used to configure generation for a request. This includes
the template that renders the prompt, and various generation settings like
`temperature`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.generation_presets.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**llm_name:** `typing.Optional[str]` — Filter presets by the LLM name.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` 

Used to retrieve the next page of generation presets after the limit has been reached.
This parameter is not needed for the first page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Encoders
<details><summary><code>client.encoders.<a href="src/vectara/encoders/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Encoders are used to store and retrieve from a corpus.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.encoders.list(filter='vectara.*', )
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `typing.Optional[str]` — A regular expression against encoder names and descriptions.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of encoders after the limit has been reached.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encoders.<a href="src/vectara/encoders/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new encoder.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.encoders.create(name='openai-text-encoder', description='description', uri='https://api.openai.com/v1/embeddings', model='text-embedding-ada-002', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — A unique name for the encoder
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — A description of what this encoder does
    
</dd>
</dl>

<dl>
<dd>

**uri:** `str` — The URI endpoint for the embedding API (can be OpenAI or any compatible embedding API endpoint)
    
</dd>
</dl>

<dl>
<dd>

**model:** `str` — The model name to use for embeddings
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**output_dimensions:** `typing.Optional[int]` 

The number of dimensions in the output embedding vector. If provided and the model supports truncation,
the response will be truncated to this number of dimensions.
    
</dd>
</dl>

<dl>
<dd>

**auth:** `typing.Optional[RemoteAuth]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Rerankers
<details><summary><code>client.rerankers.<a href="src/vectara/rerankers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rerankers are used to improve the ranking (ordering) of search results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.rerankers.list(filter='vectara.*', )
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `typing.Optional[str]` — A regular expression against reranker names and descriptions.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of rerankers to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of rerankers after the limit has been reached.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Table Extractors
<details><summary><code>client.table_extractors.<a href="src/vectara/table_extractors/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Table extractors are used to extract tabular data from documents during indexing.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.table_extractors.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Jobs
<details><summary><code>client.jobs.<a href="src/vectara/jobs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List jobs for the account. Jobs are background processes like replacing the filterable metadata attributes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.jobs.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `typing.Optional[typing.Union[CorpusKey, typing.Sequence[CorpusKey]]]` — The unique key identifying the corpus with the job.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[dt.datetime]` — Filter by jobs created after a particular date-time.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[typing.Union[JobState, typing.Sequence[JobState]]]` — Filter by jobs in particular states.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of jobs to return at one time.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of jobs after the limit has been reached.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/vectara/jobs/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a job by a specific ID. Jobs are background processes like replacing the filterable metadata attributes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.jobs.get(job_id='job_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — The ID of the job to get.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/vectara/users/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all users in the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.users.list(corpus_key='my-corpus', )
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of users to return at one time.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of users after the limit has been reached.
    
</dd>
</dl>

<dl>
<dd>

**corpus_key:** `typing.Optional[CorpusKey]` — Filter users by access to this corpus.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/vectara/users/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a user for the current customer account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.users.create(email='email', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — The email address for the user.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — The username for the user. The value defaults to the email.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the user.
    
</dd>
</dl>

<dl>
<dd>

**api_roles:** `typing.Optional[typing.Sequence[ApiRole]]` — The role names assigned to the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/vectara/users/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a user and view details like the email, username, and associated roles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.users.get(username='username', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` 

Specifies the user ID that to retrieve.
Note that the username must be percent encoded.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/vectara/users/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a user from the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.users.delete(username='username', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` 

Specifies the user ID to delete.
Note that the username must be percent encoded.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/vectara/users/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update details about a user such as role names.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.users.update(username='username', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` 

Specifies the user ID to update.
Note that the username must be percent encoded.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Indicates whether to enable or disable the user.
    
</dd>
</dl>

<dl>
<dd>

**api_roles:** `typing.Optional[typing.Sequence[ApiRole]]` — The new role names of the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/vectara/users/client.py">reset_password</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reset the password for a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.users.reset_password(username='username', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` 

Specifies the user ID to update.
Note that the username must be percent encoded and URI safe.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## API Keys
<details><summary><code>client.api_keys.<a href="src/vectara/api_keys/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of API keys for the customer account with optional filtering.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.api_keys.list(corpus_key='my-corpus', )
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max number of API keys to return at one time.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of API keys after the limit has been reached.
    
</dd>
</dl>

<dl>
<dd>

**corpus_key:** `typing.Optional[CorpusKey]` — Filters the API keys to only those with permissions on the specified corpus key.
    
</dd>
</dl>

<dl>
<dd>

**api_key_role:** `typing.Optional[ApiKeyRole]` — Filter API keys by their role.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/vectara/api_keys/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An API key is to authenticate when calling Vectara APIs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.api_keys.create(name='name', api_key_role="serving", )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The human-readable name of the API key.
    
</dd>
</dl>

<dl>
<dd>

**api_key_role:** `ApiKeyRole` 
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**corpus_keys:** `typing.Optional[typing.Sequence[CorpusKey]]` 

Corpora this API key has roles on if it is not a Personal API key.
This property should be null or missing if this `api_key_role` is
`personal`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/vectara/api_keys/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a specific API key by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.api_keys.get(api_key_id='api_key_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key_id:** `str` — The ID of the API key.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/vectara/api_keys/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete API keys to help you manage the security and lifecycle of API keys in your application.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.api_keys.delete(api_key_id='api_key_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key_id:** `str` — The ID of the API key.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/vectara/api_keys/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an API key such as the roles attached to the key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.api_keys.update(api_key_id='api_key_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key_id:** `str` — The ID of the API key.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Indicates whether to disable or enable an API key.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AppClients
<details><summary><code>client.app_clients.<a href="src/vectara/app_clients/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of application clients configured for the customer account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.app_clients.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of App Clients to return at one time.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — Regular expression to filter the names of the App Clients.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of App Clients after the limit has been reached.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_clients.<a href="src/vectara/app_clients/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An App Client is used for OAuth 2.0 authentication when calling Vectara APIs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.app_clients.create(name='name', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the client credentials.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the client credentials.
    
</dd>
</dl>

<dl>
<dd>

**api_roles:** `typing.Optional[typing.Sequence[ApiRole]]` — API roles that the client credentials will have.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_clients.<a href="src/vectara/app_clients/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a specific application client by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.app_clients.get(app_client_id='app_client_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_client_id:** `str` — The ID of the App Client.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_clients.<a href="src/vectara/app_clients/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove an application client configuration from the customer account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.app_clients.delete(app_client_id='app_client_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_client_id:** `str` — The ID of App Client.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_clients.<a href="src/vectara/app_clients/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the configuration or settings of an existing application client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.app_clients.update(app_client_id='app_client_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_client_id:** `str` — The name of App Client.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The new App Client description.
    
</dd>
</dl>

<dl>
<dd>

**api_roles:** `typing.Optional[typing.Sequence[ApiRole]]` — The new roles attached to the App Client. These roles will replace the current roles.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Query History
<details><summary><code>client.query_history.<a href="src/vectara/query_history/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a detailed history of previously executed query.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.query_history.get(query_id='query_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query_id:** `str` — The ID of the query history
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.query_history.<a href="src/vectara/query_history/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve query histories.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
response = client.query_history.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**corpus_key:** `typing.Optional[str]` — Specifies the `corpus_key` used in the query.
    
</dd>
</dl>

<dl>
<dd>

**started_after:** `typing.Optional[dt.datetime]` — Queries that started after a particular date-time.
    
</dd>
</dl>

<dl>
<dd>

**started_before:** `typing.Optional[dt.datetime]` — Queries that started before a particular date-time.
    
</dd>
</dl>

<dl>
<dd>

**chat_id:** `typing.Optional[str]` — Specifies the chat_id of the query, this will return all queries in the specified chat.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Specifies the maximum number of query history listed.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of query histories after the limit has been reached.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified seconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_timeout_millis:** `typing.Optional[int]` — The API will make a best effort to complete the request in the specified milliseconds or time out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Auth
<details><summary><code>client.auth.<a href="src/vectara/auth/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Obtain an OAuth2 access token using client credentials
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vectara import Vectara
client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
client.auth.get_token(client_id='client_id', client_secret='client_secret', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — The client ID of the application
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — The client secret of the application
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

