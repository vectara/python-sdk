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

List corpora in the account. The returned corpus objects contain less detail compared to those retrieved the direct corpus retrieval operation.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.corpora.list(
    filter="Vectara Content",
)
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

**corpus_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter corpora to only include corpora with these IDs.
    
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

Create a corpus, which is a container to store documents and associated metadata. Here, you define the unique `corpus_key` that identifies the corpus. The `corpus_key` can be custom-defined following your preferred naming convention, allowing you to easily manage the corpus's data and reference it in queries. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
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
from vectara import FilterAttribute, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.corpora.create(
    key="fin_esg_docs",
    name="EU Bank ESG Compliance",
    description="A corpus for storing and querying financial documents, such as annual reports and ESG compliance filings, for European banks in 2023.",
    save_history=True,
    encoder_name="boomerang-2023-q3",
    filter_attributes=[
        FilterAttribute(
            name="industry",
            level="part",
            description="The industry sector of the document (banking).",
            indexed=True,
            type="text",
        ),
        FilterAttribute(
            name="region",
            level="part",
            description="The geographical region of the document (EU).",
            indexed=True,
            type="text",
        ),
        FilterAttribute(
            name="year",
            level="part",
            description="The publication year of the document (2023).",
            indexed=True,
            type="integer",
        ),
        FilterAttribute(
            name="doc_type",
            level="part",
            description="The type of document (annual_report).",
            indexed=True,
            type="text",
        ),
    ],
)

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

**filter_attributes:** `typing.Optional[typing.Sequence[FilterAttribute]]` — The new filter attributes of the corpus. If unset then the corpus will not have filter attributes.
    
</dd>
</dl>

<dl>
<dd>

**custom_dimensions:** `typing.Optional[typing.Sequence[CorpusCustomDimension]]` — A custom dimension is an additional numerical field attached to a document part. You can then multiply this numerical field with a query time custom dimension of the same name. This allows boosting (or burying) document parts for arbitrary reasons. This feature is only enabled for Pro and Enterprise customers.
    
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

Get metadata about a corpus. This operation does not search the corpus contents. Specify the `corpus_key` to identify the corpus whose metadata you want to retrieve. The `corpus_key` is created when the corpus is set up, either through the Vectara Console UI or the Create Corpus API. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.corpora.get(
    corpus_key="my-corpus",
)

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

Permanently delete a corpus and all its associated data. The `corpus_key` uniquely identifies the corpus. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.corpora.delete(
    corpus_key="my-corpus",
)

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

Enable, disable, or update the name and description of a corpus. This lets you manage data availability without deleting the corpus, which is useful for maintenance and security purposes. The `corpus_key` uniquely identifies the corpus. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition). Consider updating the name and description of a corpus dynamically to help keep your data aligned with changing business needs.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.corpora.update(
    corpus_key="my-corpus",
)

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

Resets a corpus, which removes all documents and data from the specified corpus, while keeping the corpus itself. The `corpus_key` uniquely identifies the corpus. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.corpora.reset(
    corpus_key="my-corpus",
)

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

Replace the filter attributes of a corpus. This does not happen immediately, as this operation creates a job that completes asynchronously. These new filter attributes will not work until the job completes.
You can monitor the status of the filter change using the returned job ID. The `corpus_key` uniquely identifies the corpus. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
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
from vectara import FilterAttribute, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.corpora.replace_filter_attributes(
    corpus_key="my-corpus",
    filter_attributes=[
        FilterAttribute(
            name="jurisdiction",
            level="document",
            description="The legal jurisdiction of the contract (Delaware, California).",
            indexed=True,
            type="text",
        ),
        FilterAttribute(
            name="type",
            level="document",
            description="The type of legal document (employment_contract, nda).",
            indexed=True,
            type="text",
        ),
    ],
)

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

Compute the current size of a corpus, including number of documents, parts, and characters. The `corpus_key` uniquely identifies the corpus. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.corpora.compute_size(
    corpus_key="my-corpus",
)

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

* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is [created in the Vectara Console UI](https://docs.vectara.com/docs/console-ui/creating-a-corpus) or the [Create Corpus API definition](https://docs.vectara.com/docs/api-reference/admin-apis/create-corpus), and the corpus key is part of that process. When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
* Enter the search `query` string for the corpus, which is the question you want to ask.
* Set the maximum number of results (`limit`) to return. **Default**: 10, **minimum**: 1

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.corpora.search(
    corpus_key="my-corpus",
    query="query",
)

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

**limit:** `typing.Optional[int]` — The maximum number of top retrieval results to rerank and return.
    
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

**intelligent_query_rewriting:** `typing.Optional[bool]` — [Tech Preview] Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to extract metadata filter and rewrite the query to improve search results. Read [here](https://docs.vectara.com/docs/search-and-retrieval/intelligent-query-rewriting) for more details.
    
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

Perform an advanced query on a specific corpus to find relevant results, highlight relevant snippets, and use Retrieval Augmented Generation.

* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is [created in the Vectara Console UI](https://docs.vectara.com/docs/console-ui/creating-a-corpus) or the [Create Corpus API definition](https://docs.vectara.com/docs/api-reference/admin-apis/create-corpus), and the corpus key is part of that process. When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
* Customize your search by specifying the query text (`query`), pagination details (`offset` and `limit`), and metadata filters (`metadata_filter`) to tailor your search results. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#query-definition)
* Leverage advanced search capabilities like reranking (`reranker`) and Retrieval Augmented Generation (RAG) (`generation`) for enhanced query performance. Generation is opt in by setting the `generation` property. By excluding the property or by setting it to null, the response will not include generation. [Learn more](https://docs.vectara.com/docs/learn/grounded-generation/configure-query-summarization).
* Use hybrid search to achieve optimal results by setting different values for `lexical_interpolation` (e.g., `0.005`). [Learn more](https://docs.vectara.com/docs/learn/hybrid-search)
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
from vectara import (
    CitationParameters,
    ContextConfiguration,
    CustomerSpecificReranker,
    GenerationParameters,
    Vectara,
)
from vectara.corpora import SearchCorpusParameters

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.corpora.query_stream(
    corpus_key="my-corpus",
    query="How to configure OAuth2 for microservices in Kubernetes?",
    search=SearchCorpusParameters(
        limit=50,
        context_configuration=ContextConfiguration(
            sentences_before=2,
            sentences_after=2,
            start_tag="<em>",
            end_tag="</em>",
        ),
        reranker=CustomerSpecificReranker(
            reranker_name="Rerank_Multilingual_v1",
            limit=50,
            include_context=True,
        ),
        metadata_filter="doc.topic = 'authentication' and doc.platform = 'kubernetes'",
        lexical_interpolation=0.005,
    ),
    generation=GenerationParameters(
        generation_preset_name="vectara-summary-ext-24-05-med-omni",
        max_used_search_results=10,
        citations=CitationParameters(
            style="markdown",
            url_pattern="https://vectara.com/documents/{doc.id}",
            text_pattern="{doc.title}",
        ),
    ),
    save_history=True,
    intelligent_query_rewriting=True,
)
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

**intelligent_query_rewriting:** `typing.Optional[bool]` — [Tech Preview] Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to extract metadata filter and rewrite the query to improve search results. Read [here](https://docs.vectara.com/docs/search-and-retrieval/intelligent-query-rewriting) for more details.
    
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

Perform an advanced query on a specific corpus to find relevant results, highlight relevant snippets, and use Retrieval Augmented Generation.

* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is [created in the Vectara Console UI](https://docs.vectara.com/docs/console-ui/creating-a-corpus) or the [Create Corpus API definition](https://docs.vectara.com/docs/api-reference/admin-apis/create-corpus), and the corpus key is part of that process. When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
* Customize your search by specifying the query text (`query`), pagination details (`offset` and `limit`), and metadata filters (`metadata_filter`) to tailor your search results. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#query-definition)
* Leverage advanced search capabilities like reranking (`reranker`) and Retrieval Augmented Generation (RAG) (`generation`) for enhanced query performance. Generation is opt in by setting the `generation` property. By excluding the property or by setting it to null, the response will not include generation. [Learn more](https://docs.vectara.com/docs/learn/grounded-generation/configure-query-summarization).
* Use hybrid search to achieve optimal results by setting different values for `lexical_interpolation` (e.g., `0.005`). [Learn more](https://docs.vectara.com/docs/learn/hybrid-search)
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
from vectara import (
    CitationParameters,
    ContextConfiguration,
    CustomerSpecificReranker,
    GenerationParameters,
    Vectara,
)
from vectara.corpora import SearchCorpusParameters

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.corpora.query(
    corpus_key="my-corpus",
    query="How to configure OAuth2 for microservices in Kubernetes?",
    search=SearchCorpusParameters(
        limit=50,
        context_configuration=ContextConfiguration(
            sentences_before=2,
            sentences_after=2,
            start_tag="<em>",
            end_tag="</em>",
        ),
        reranker=CustomerSpecificReranker(
            reranker_name="Rerank_Multilingual_v1",
            limit=50,
            include_context=True,
        ),
        metadata_filter="doc.topic = 'authentication' and doc.platform = 'kubernetes'",
        lexical_interpolation=0.005,
    ),
    generation=GenerationParameters(
        generation_preset_name="vectara-summary-ext-24-05-med-omni",
        max_used_search_results=10,
        citations=CitationParameters(
            style="markdown",
            url_pattern="https://vectara.com/documents/{doc.id}",
            text_pattern="{doc.title}",
        ),
    ),
    save_history=True,
    intelligent_query_rewriting=True,
)

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

**intelligent_query_rewriting:** `typing.Optional[bool]` — [Tech Preview] Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to extract metadata filter and rewrite the query to improve search results. Read [here](https://docs.vectara.com/docs/search-and-retrieval/intelligent-query-rewriting) for more details.
    
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

Upload a file, such as a PDF or Word document, to the specified corpus for automatic text extraction and metadata parsing.  

This endpoint expects a `multipart/form-data` request with the following fields:  

- **metadata**: An optional JSON object containing additional metadata to associate with the document.  
  Example: `metadata={"key": "value"}`
- **chunking_strategy**: An optional JSON object that sets the chunking method for text extraction.  
  - By default, the platform uses sentence-based chunking (one chunk per sentence).
  - Example for explicit sentence chunking: `chunking_strategy={"type":"sentence_chunking_strategy"}`
  - Example for max chars chunking: `chunking_strategy={"type":"max_chars_chunking_strategy","max_chars_per_chunk":512}`
- **table_extraction_config**: An optional JSON object to control table extraction from supported file types (e.g., PDF).  
  Example: `table_extraction_config={"extract_tables": true}`
- **file**: The file to upload. Attach your file as the value for this field.
- **filename**: The desired name for the uploaded file. Specify as part of the file field in your request.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.upload.file(
    corpus_key="my-corpus",
)

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

Retrieve a list of documents stored in a specific corpus. This endpoint provides an overview of document metadata without returning the full content of each document.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.documents.list(
    corpus_key="my-corpus",
)
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

**metadata_filter:** `typing.Optional[str]` — Filter documents by metadata. Uses the same expression as a query metadata filter, but only allows filtering on document metadata.
    
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

Add a document to a corpus. This endpoint supports two document formats: structured and core.

* **Structured** documents have a conventional structure that provides document sections and parts in a format created by our proprietary strategy automatically. You provide a logical document structure, and Vectara handles the partitioning.
* **Core** documents differ in that they follow an advanced, granular structure that explicitly defines each document part in an array. Each part becomes a distinct, searchable item in query results. You have precise control over the document structure and content.

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
from vectara import StructuredDocument, StructuredDocumentSection, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.documents.create(
    corpus_key="my-corpus-key",
    request=StructuredDocument(
        id="my-doc-id",
        sections=[
            StructuredDocumentSection(
                id=1,
                title="A nice title.",
                text="I'm a nice document section.",
                metadata={"section": "1.1"},
            ),
            StructuredDocumentSection(
                id=2,
                title="Another nice title.",
                text="I'm another document section on something else.",
                metadata={"section": "1.2"},
            ),
        ],
        metadata={"url": "https://example.com"},
    ),
)

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

Returns a specific image that is embedded within a document. The `image_id` uniquely identifies the image within the document. Use this endpoint to fetch the raw image data and associated metadata.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.documents.get(
    corpus_key="my-corpus",
    document_id="document_id",
    image_id="image_id",
)

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

**corpus_key:** `CorpusKey` — A unique identifier for the corpus that contains the target document.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — The identifier of the document containing the image. This `document_id` must be percent encoded.
    
</dd>
</dl>

<dl>
<dd>

**image_id:** `str` — The identifier of the image to retrieve from the specified document. Each image within a document has a unique `image_id`. This value must be percent-encoded when passed in the request URL.
    
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

Permanently delete a document identified by its unique `document_id` from a specific corpus. This operation cannot be undone, so use it with caution.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.documents.delete(
    corpus_key="my-corpus",
    document_id="document_id",
)

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

**document_id:** `str` — The document ID of the document to delete. This `document_id` must be percent encoded.
    
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

Updates document identified by its unique `document_id` from a specific corpus. The request body metadata is merged with the existing metadata, adding or modifying only the specified fields.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.documents.update(
    corpus_key="my-corpus",
    document_id="document_id",
)

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

**document_id:** `str` — The document ID of the document to update. This `document_id` must be percent encoded.
    
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The metadata for a document as an arbitrary object. Properties of this object can be used by document level filter attributes.
    
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

Replaces metadata of a document identified by its unique `document_id` from a specific corpus.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.documents.update_metadata(
    corpus_key="my-corpus",
    document_id="document_id",
)

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

**document_id:** `str` — The document ID of the document to update. This `document_id` must be percent encoded.
    
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The metadata for a document as an arbitrary object. Properties of this object can be used by document level filter attributes.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.documents.summarize(
    corpus_key="my-corpus",
    document_id="document_id",
    llm_name="mockingbird-2.0",
    prompt_template="Summarize the key clauses of the employment contract in ${document.metadata.jurisdiction}, focusing on arbitration, confidentiality, and termination terms.",
    model_parameters={"max_tokens": 200, "temperature": 0.7},
    stream_response=False,
)

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

**document_id:** `str` — The document ID of the document to retrieve. This `document_id` must be percent encoded.
    
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

**prompt_template:** `typing.Optional[str]` — The prompt template to use when generating the summary. Vectara manages both system and user roles and prompts for the generative LLM out of the box by default. However, users can override the `prompt_template` via this variable. The `prompt_template` is in the form of an Apache Velocity template. For more details on how to configure the `prompt_template`, see the [long-form documentation](https://docs.vectara.com/docs/prompts/vectara-prompt-engine).
    
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

## Metadata
<details><summary><code>client.metadata.<a href="src/vectara/metadata/client.py">query_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query for documents in a specific corpus using fuzzy matching across specified metadata fields. The search first applies any exact metadata filters to narrow the results, then performs fuzzy matching on the remaining documents using the specified field queries.
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
from vectara import FieldQuery, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.metadata.query_metadata(
    corpus_key="my-corpus",
    queries=[
        FieldQuery(
            field="title",
            query="lease agreement",
            weight=2.0,
        ),
        FieldQuery(
            field="category",
            query="contract",
            weight=1.0,
        ),
    ],
)

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

**corpus_key:** `CorpusKey` — The unique key identifying the corpus to search for metadata.
    
</dd>
</dl>

<dl>
<dd>

**queries:** `typing.Sequence[FieldQuery]` — List of field-specific queries to apply fuzzy matching.
    
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

**level:** `typing.Optional[MetadataQueryRequestLevel]` — Whether to search document-level or part-level metadata. Document-level returns unique documents, part-level can return multiple parts from the same document.
    
</dd>
</dl>

<dl>
<dd>

**metadata_filter:** `typing.Optional[str]` 

Optional filter expression to narrow down results before fuzzy matching is applied. 
This uses the same expression format as document listing filters and applies exact matching.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Sets the maximum number of documents to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Starting position for pagination.
    
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

Perform a multipurpose query to retrieve relevant information from one or more corpora and generate a response using Retrieval Augmented Generation (RAG).

* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is [created in the Vectara Console UI](https://docs.vectara.com/docs/console-ui/creating-a-corpus) or the [Create Corpus API definition](https://docs.vectara.com/docs/api-reference/admin-apis/create-corpus), and the corpus key is part of that process. When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
* Customize your search by specifying the query text (`query`), pagination details (`offset` and `limit`), and metadata filters (`metadata_filter`) to tailor your search results. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#query-definition)
* Leverage advanced search capabilities like reranking (`reranker`) and opt-in Retrieval Augmented Generation (RAG) (`generation`) for enhanced query performance. Generation is opt-in by setting the `generation` property. By excluding the property or by setting it to null, the response will not include generation. [Learn more](https://docs.vectara.com/docs/learn/grounded-generation/configure-query-summarization)
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
from vectara import (
    ContextConfiguration,
    CustomerSpecificReranker,
    GenerationParameters,
    KeyedSearchCorpus,
    SearchCorporaParameters,
    Vectara,
)

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.queries.query_stream(
    query="What is a hallucination?",
    search=SearchCorporaParameters(
        corpora=[
            KeyedSearchCorpus(
                corpus_key="corpus_key",
                metadata_filter="",
                lexical_interpolation=0.005,
            )
        ],
        context_configuration=ContextConfiguration(
            sentences_before=2,
            sentences_after=2,
        ),
        reranker=CustomerSpecificReranker(
            reranker_id="rnk_272725719",
        ),
    ),
    generation=GenerationParameters(
        response_language="eng",
        enable_factual_consistency_score=True,
    ),
)
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

**intelligent_query_rewriting:** `typing.Optional[bool]` — [Tech Preview] Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to extract metadata filter and rewrite the query to improve search results. Read [here](https://docs.vectara.com/docs/search-and-retrieval/intelligent-query-rewriting) for more details.
    
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

Perform a multipurpose query to retrieve relevant information from one or more corpora and generate a response using Retrieval Augmented Generation (RAG).

* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is [created in the Vectara Console UI](https://docs.vectara.com/docs/console-ui/creating-a-corpus) or the [Create Corpus API definition](https://docs.vectara.com/docs/api-reference/admin-apis/create-corpus), and the corpus key is part of that process. When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests. For more information, see [Corpus Key Definition](https://docs.vectara.com/docs/api-reference/search-apis/search#corpus-key-definition).
* Customize your search by specifying the query text (`query`), pagination details (`offset` and `limit`), and metadata filters (`metadata_filter`) to tailor your search results. [Learn more](https://docs.vectara.com/docs/api-reference/search-apis/search#query-definition)
* Leverage advanced search capabilities like reranking (`reranker`) and opt-in Retrieval Augmented Generation (RAG) (`generation`) for enhanced query performance. Generation is opt-in by setting the `generation` property. By excluding the property or by setting it to null, the response will not include generation. [Learn more](https://docs.vectara.com/docs/learn/grounded-generation/configure-query-summarization)
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
from vectara import (
    ContextConfiguration,
    CustomerSpecificReranker,
    GenerationParameters,
    KeyedSearchCorpus,
    SearchCorporaParameters,
    Vectara,
)

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.queries.query(
    query="What is a hallucination?",
    search=SearchCorporaParameters(
        corpora=[
            KeyedSearchCorpus(
                corpus_key="corpus_key",
                metadata_filter="",
                lexical_interpolation=0.005,
            )
        ],
        context_configuration=ContextConfiguration(
            sentences_before=2,
            sentences_after=2,
        ),
        reranker=CustomerSpecificReranker(
            reranker_id="rnk_272725719",
        ),
    ),
    generation=GenerationParameters(
        response_language="eng",
        enable_factual_consistency_score=True,
    ),
)

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

**intelligent_query_rewriting:** `typing.Optional[bool]` — [Tech Preview] Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to extract metadata filter and rewrite the query to improve search results. Read [here](https://docs.vectara.com/docs/search-and-retrieval/intelligent-query-rewriting) for more details.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.query_history.get(
    query_id="qry_123456789",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.query_history.list(
    corpus_key="my_corpus_key",
    chat_id="cht_123456789",
)
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

**started_after:** `typing.Optional[dt.datetime]` — Queries that started after a particular ISO date-time.
    
</dd>
</dl>

<dl>
<dd>

**started_before:** `typing.Optional[dt.datetime]` — Queries that started before a particular ISO date-time.
    
</dd>
</dl>

<dl>
<dd>

**chat_id:** `typing.Optional[str]` — Specifies the chat_id of the query, this will return all queries in the specified chat.
    
</dd>
</dl>

<dl>
<dd>

**history_id:** `typing.Optional[str]` — Specifies the history_id of the query that you want to use as a filter.
    
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
from vectara import (
    ChatParameters,
    CitationParameters,
    ContextConfiguration,
    CustomerSpecificReranker,
    GenerationParameters,
    KeyedSearchCorpus,
    SearchCorporaParameters,
    Vectara,
)

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.chats.create_stream(
    query="What is a hallucination?",
    search=SearchCorporaParameters(
        corpora=[
            KeyedSearchCorpus(
                corpus_key="corpus_key",
                metadata_filter="",
                lexical_interpolation=0.005,
            )
        ],
        context_configuration=ContextConfiguration(
            sentences_before=2,
            sentences_after=2,
        ),
        reranker=CustomerSpecificReranker(
            reranker_id="rnk_272725719",
        ),
    ),
    generation=GenerationParameters(
        response_language="eng",
        citations=CitationParameters(
            style="none",
        ),
        enable_factual_consistency_score=True,
    ),
    chat=ChatParameters(
        store=True,
    ),
)
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

**intelligent_query_rewriting:** `typing.Optional[bool]` — [Tech Preview] Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to extract metadata filter and rewrite the query to improve search results. Read [here](https://docs.vectara.com/docs/search-and-retrieval/intelligent-query-rewriting) for more details.
    
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
from vectara import (
    ChatParameters,
    CitationParameters,
    ContextConfiguration,
    CustomerSpecificReranker,
    GenerationParameters,
    KeyedSearchCorpus,
    SearchCorporaParameters,
    Vectara,
)

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.chats.create(
    query="What is a hallucination?",
    search=SearchCorporaParameters(
        corpora=[
            KeyedSearchCorpus(
                corpus_key="corpus_key",
                metadata_filter="",
                lexical_interpolation=0.005,
            )
        ],
        context_configuration=ContextConfiguration(
            sentences_before=2,
            sentences_after=2,
        ),
        reranker=CustomerSpecificReranker(
            reranker_id="rnk_272725719",
        ),
    ),
    generation=GenerationParameters(
        response_language="eng",
        enable_factual_consistency_score=True,
        citations=CitationParameters(
            style="none",
        ),
    ),
    chat=ChatParameters(
        store=True,
    ),
)

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

**intelligent_query_rewriting:** `typing.Optional[bool]` — [Tech Preview] Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to extract metadata filter and rewrite the query to improve search results. Read [here](https://docs.vectara.com/docs/search-and-retrieval/intelligent-query-rewriting) for more details.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.chats.get(
    chat_id="chat_id",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.chats.delete(
    chat_id="chat_id",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.chats.list_turns(
    chat_id="cht_1234567890",
)

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
from vectara import SearchCorporaParameters, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.chats.create_turns_stream(
    chat_id="chat_id",
    query="What are the carbon reduction efforts by EU banks in 2023?",
    search=SearchCorporaParameters(),
)
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

**intelligent_query_rewriting:** `typing.Optional[bool]` — [Tech Preview] Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to extract metadata filter and rewrite the query to improve search results. Read [here](https://docs.vectara.com/docs/search-and-retrieval/intelligent-query-rewriting) for more details.
    
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
from vectara import SearchCorporaParameters, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.chats.create_turns(
    chat_id="chat_id",
    query="What are the carbon reduction efforts by EU banks in 2023?",
    search=SearchCorporaParameters(),
)

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

**intelligent_query_rewriting:** `typing.Optional[bool]` — [Tech Preview] Indicates whether to enable intelligent query rewriting. When enabled, the platform will attempt to extract metadata filter and rewrite the query to improve search results. Read [here](https://docs.vectara.com/docs/search-and-retrieval/intelligent-query-rewriting) for more details.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.chats.get_turn(
    chat_id="chat_id",
    turn_id="turn_id",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.chats.delete_turn(
    chat_id="chat_id",
    turn_id="turn_id",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.chats.update_turn(
    chat_id="cht_1234567890",
    turn_id="trn_987654321",
)

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

**enabled:** `typing.Optional[bool]` — Indicates whether to disable a turn. It will disable this turn and all subsequent turns. Enabling a turn is not implemented.
    
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

List LLMs that can be used with query and chat endpoints. The LLM is not directly specified in a query, but instead a `generation_preset_name` is used. The `generation_preset_name` property in generation parameters can be found as the `name` property on the Generations Presets retrieved from `/v2/generation_presets`.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
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

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of LLMs after the limit has been reached. This parameter is not needed for the first page of results.
    
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
from vectara import CreateOpenAillmRequest, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.llms.create(
    request=CreateOpenAillmRequest(
        name="Claude 3.7 Sonnet",
        model="model",
        uri="https://api.anthropic.com/v1/chat/completions",
    ),
)

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

**request:** `CreateLlmRequest` 
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.llms.get(
    llm_id="llm_id",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.llms.delete(
    llm_id="llm_id",
)

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

## Llm
<details><summary><code>client.llm.<a href="src/vectara/llm/client.py">chat_completion</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

OpenAI-compatible endpoint for chat completions. Creates a response for the given chat conversation. The chat completion API allows you to chat with Vectara's language models in a way that's compatible with OpenAI's specification. This makes it easy to integrate with applications already designed for OpenAI's API.
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
from vectara import ChatCompletionRequestMessage, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.llm.chat_completion(
    model="model",
    messages=[
        ChatCompletionRequestMessage(
            role="role",
            content="content",
        )
    ],
)

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

**model:** `str` — The ID of the model to use. This field is required.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[ChatCompletionRequestMessage]` — An ordered array of messages that represent the full context of the conversation to date. Each message includes a `role` and `content`.
    
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

**stream:** `typing.Optional[bool]` — Optional. When set to `true`, the API streams partial message deltas as they become available, similar to ChatGPT's streaming mode.
    
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

List generation presets used for query or chat requests. Generation presets are the build of properties used to configure generation for a request. This includes the template that renders the prompt, and various generation settings like `temperature`.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.generation_presets.list(
    llm_name="mockingbird-2.0",
)
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

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of generation presets after the limit has been reached. This parameter is not needed for the first page of results.
    
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

## FactualConsistency
<details><summary><code>client.factual_consistency.<a href="src/vectara/factual_consistency/client.py">evaluate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Evaluate the factual consistency of a generated text (like a summary) against source documents. This determines how accurately the generated text reflects the information in the source documents, helping identify potential hallucinations or misrepresentations.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.factual_consistency.evaluate(
    generated_text="generated_text",
    source_texts=["source_texts"],
)

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

**generated_text:** `str` — The generated text (e.g., summary or answer) to evaluate for factual consistency.
    
</dd>
</dl>

<dl>
<dd>

**source_texts:** `typing.Sequence[str]` — The source documents or text snippets against which to evaluate factual consistency.
    
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

**model_parameters:** `typing.Optional[EvaluateFactualConsistencyRequestModelParameters]` — The model parameters for the evaluation.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.encoders.list(
    filter="vectara.*",
)
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encoders.create(
    name="openai-text-encoder",
    description="description",
    uri="https://api.openai.com/v1/embeddings",
    model="text-embedding-ada-002",
)

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

**output_dimensions:** `typing.Optional[int]` — The number of dimensions in the output embedding vector. If provided and the model supports truncation, the response will be truncated to this number of dimensions.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.rerankers.list(
    filter="vectara.*",
)
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
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

## Hallucination Correctors
<details><summary><code>client.hallucination_correctors.<a href="src/vectara/hallucination_correctors/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of available hallucination correctors used for detecting and correcting hallucinations in AI-generated content. This endpoint supports filtering by name or description, pagination, and metadata for navigating large result sets.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.hallucination_correctors.list()
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

**filter:** `typing.Optional[str]` — A regular expression applied to the name and description fields. Use this to return only hallucination correctors that match specific keywords or naming conventions.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of hallucination correctors to return in the list. Defaults to 10. Range is between 1 and 100.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Retrieves the next page of hallucination correctors after reaching the limit.
    
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

<details><summary><code>client.hallucination_correctors.<a href="src/vectara/hallucination_correctors/client.py">hallucination_correction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint identifies information in generated text that is not supported by the provided source documents and offers corrections with minimal changes. This can be used standalone or as part of a RAG workflow where the HHEM score indicates potential hallucinations.
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
from vectara import HcmSourceDocument, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.hallucination_correctors.hallucination_correction(
    generated_text="generated_text",
    documents=[
        HcmSourceDocument(
            text="text",
        )
    ],
    model_name="vhc-large-1.0",
)

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

**generated_text:** `str` — The generated text to be evaluated. The hallucination corrector reviews this text and applies corrections based on the provided source documents.
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.Sequence[HcmSourceDocument]` — The source documents that were used to generate the text.
    
</dd>
</dl>

<dl>
<dd>

**model_name:** `str` — The name of the LLM model to use for hallucination correction.
    
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

**query:** `typing.Optional[str]` — Optional query that provides context for the expected response format and factual information. When provided, enables query-aware hallucination correction that considers the specific response format and factual context expected for the query.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.jobs.get(
    job_id="job_id",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.users.list(
    corpus_key="my-corpus",
)
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.create(
    email="email",
)

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

**api_roles:** `typing.Optional[typing.Sequence[ApiRole]]` — The customer-level role names assigned to the user.
    
</dd>
</dl>

<dl>
<dd>

**corpus_roles:** `typing.Optional[typing.Sequence[CorpusRole]]` — Corpus-specific role assignments for the user.
    
</dd>
</dl>

<dl>
<dd>

**agent_roles:** `typing.Optional[typing.Sequence[AgentRole]]` — Agent-specific role assignments for the user.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.get(
    username="username",
)

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

**username:** `str` — Specifies the user ID that to retrieve. Note that the username must be percent encoded.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.delete(
    username="username",
)

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

**username:** `str` — Specifies the user ID to delete. Note that the username must be percent encoded.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.update(
    username="username",
)

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

**username:** `str` — Specifies the user ID to update. Note that the username must be percent encoded.
    
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

**api_roles:** `typing.Optional[typing.Sequence[ApiRole]]` — The new customer-level role names of the user.
    
</dd>
</dl>

<dl>
<dd>

**corpus_roles:** `typing.Optional[typing.Sequence[CorpusRole]]` — New corpus-specific role assignments for the user.
    
</dd>
</dl>

<dl>
<dd>

**agent_roles:** `typing.Optional[typing.Sequence[AgentRole]]` — New agent-specific role assignments for the user.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the user.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.users.reset_password(
    username="username",
)

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

**username:** `str` — Specifies the user ID to update. Note that the username must be percent encoded and URI safe.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.api_keys.list(
    corpus_key="my-corpus",
)
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

**corpus_keys:** `typing.Optional[typing.Sequence[CorpusKey]]` — Corpora this API key has roles on if it is not a Personal API key. This property should be null or missing if this `api_key_role` is `personal`.
    
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.api_keys.get(
    api_key_id="api_key_id",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.api_keys.delete(
    api_key_id="api_key_id",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.api_keys.update(
    api_key_id="api_key_id",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.app_clients.create(
    name="name",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.app_clients.get(
    app_client_id="app_client_id",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.app_clients.delete(
    app_client_id="app_client_id",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.app_clients.update(
    app_client_id="app_client_id",
)

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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.auth.get_token(
    client_id="client_id",
    client_secret="client_secret",
)

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

## Tool Servers
<details><summary><code>client.tool_servers.<a href="src/vectara/tool_servers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of available tool servers that expose various tools.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.tool_servers.list(
    filter="rag.*",
    enabled=True,
)
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

**filter:** `typing.Optional[str]` — A regular expression against tool server names and descriptions to filter the results.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Literal["mcp"]]` — Filter tool servers by type.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Filter tool servers by enabled status.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of tool servers to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of tool servers after the limit has been reached.
    
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

<details><summary><code>client.tool_servers.<a href="src/vectara/tool_servers/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new tool server to expose tools for use by agents.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tool_servers.create(
    name="RAG Search Server",
    uri="https://api.example.com/rag_search",
    transport="sse",
)

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

**name:** `ToolServerName` 
    
</dd>
</dl>

<dl>
<dd>

**uri:** `str` — The URI of the tool server.
    
</dd>
</dl>

<dl>
<dd>

**transport:** `ToolServerTransport` 
    
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

**description:** `typing.Optional[str]` — A detailed description of what this tool server does.
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, str]]` — Optional HTTP headers to include when connecting to the server.
    
</dd>
</dl>

<dl>
<dd>

**auth:** `typing.Optional[RemoteAuth]` — Authentication configuration for connecting to the tool server.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the tool server is currently enabled and available for use.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Arbitrary metadata associated with the tool server.
    
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

<details><summary><code>client.tool_servers.<a href="src/vectara/tool_servers/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details about a specific tool server by its Id.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tool_servers.get(
    tool_server_id="tsr_rag_search",
)

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

**tool_server_id:** `str` — The unique identifier of the tool server to retrieve.
    
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

<details><summary><code>client.tool_servers.<a href="src/vectara/tool_servers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a tool server and all its associated configuration and tools. This action cannot be undone.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tool_servers.delete(
    tool_server_id="tsr_rag_search",
)

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

**tool_server_id:** `str` — The unique identifier of the tool server to delete.
    
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

<details><summary><code>client.tool_servers.<a href="src/vectara/tool_servers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the configuration of a specific tool server.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tool_servers.update(
    tool_server_id="tsr_rag_search",
)

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

**tool_server_id:** `str` — The unique identifier of the tool server to update.
    
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

**name:** `typing.Optional[ToolServerName]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A detailed description of what this tool server does.
    
</dd>
</dl>

<dl>
<dd>

**uri:** `typing.Optional[str]` — The URI of the tool server.
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, str]]` — Optional HTTP headers to include when connecting to the server.
    
</dd>
</dl>

<dl>
<dd>

**transport:** `typing.Optional[ToolServerTransport]` 
    
</dd>
</dl>

<dl>
<dd>

**auth:** `typing.Optional[RemoteAuth]` — Authentication configuration for connecting to the tool server.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the tool server is currently enabled and available for use.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Arbitrary metadata associated with the tool server.
    
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

<details><summary><code>client.tool_servers.<a href="src/vectara/tool_servers/client.py">sync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger a synchronization of the tool server to ensure it is up-to-date with the latest tools.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tool_servers.sync(
    tool_server_id="tsr_rag_search",
)

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

**tool_server_id:** `str` — The unique identifier of the tool server to synchronize.
    
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

## Tools
<details><summary><code>client.tools.<a href="src/vectara/tools/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all tools available to the authenticated user, with optional filtering and pagination.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.tools.list(
    filter="rag.*",
    enabled=True,
    tool_server_id="tsr_rag_search",
)
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

**filter:** `typing.Optional[str]` — A regular expression against tool names and descriptions to filter the results.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ToolsListRequestType]` — Filter tools by type.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Filter tools by enabled status.
    
</dd>
</dl>

<dl>
<dd>

**tool_server_id:** `typing.Optional[str]` — Filter tools by the tool server they belong to.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of tools to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of tools after the limit has been reached.
    
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

<details><summary><code>client.tools.<a href="src/vectara/tools/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new tool that agents can use. Currently supports Lambda tools for user-defined functions.
Lambda tools allow you to write custom code that agents can execute in a secure sandbox.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tools.create(
    name="calculate_customer_score",
    title="Customer Score Calculator",
    description="Calculate a customer score based on order history and revenue. Returns a score between 0-100.",
    code="def process(order_count: int, total_revenue: float, days_active: int = 1) -> dict:\n    score = (order_count * 10 + total_revenue * 0.1) / days_active\n    return {'score': round(score, 2)}\n",
)

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

**name:** `str` — The unique name of the tool (used as the function identifier).
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — Human-readable title of the tool displayed in the UI.
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — A detailed description of what the function does, when to use it, and what it returns.
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` 

The Python 3.12 code for the function.

**Required**: Must define a `process()` entry point function. Use type annotations on parameters for automatic schema discovery.

**Parameters**: Passed as keyword arguments matched to the function signature.

**Return types**: Can return any JSON-serializable type (strings, numbers, booleans, lists, or objects).

**Example: Returning a number**
```python
def process(x: int, y: int) -> int:
    return x + y
```

**Example: Returning a string**
```python
def process(name: str) -> str:
    return f"Hello, {name}!"
```

**Example: Returning a boolean**
```python
def process(value: int, threshold: int) -> bool:
    return value > threshold
```

**Example: Returning a list**
```python
from typing import List

def process(items: List[str]) -> List[str]:
    return sorted(items)
```

**Example: Returning an object (dict)**
```python
def process(order_count: int, total_revenue: float, days_active: int = 1) -> dict:
    score = (order_count * 10 + total_revenue * 0.1) / days_active
    return {'score': round(score, 2), 'rating': 'high' if score > 100 else 'low'}
```

For complex types, use the `typing` module:

```python
from typing import List, Dict

def process(items: List[str], config: Dict[str, float]) -> dict:
    count = len(items)
    multiplier = config.get('multiplier', 1.0)
    return {'count': count, 'adjusted': count * multiplier}
```
    
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

**language:** `typing.Optional[typing.Literal["python"]]` — The programming language. Currently only 'python' (Python 3.12) is supported.
    
</dd>
</dl>

<dl>
<dd>

**execution_configuration:** `typing.Optional[ExecutionConfiguration]` 
    
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

<details><summary><code>client.tools.<a href="src/vectara/tools/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the details of a specific tool by its ID, including its configuration and capabilities.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tools.get(
    tool_id="tol_rag_search",
)

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

**tool_id:** `str` — The unique identifier of the tool to retrieve.
    
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

<details><summary><code>client.tools.<a href="src/vectara/tools/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a tool and all its associated configuration. This action cannot be undone.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tools.delete(
    tool_id="tol_rag_search",
)

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

**tool_id:** `str` — The unique identifier of the tool to delete.
    
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

<details><summary><code>client.tools.<a href="src/vectara/tools/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing tool's configuration.
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
from vectara import UpdateMcpToolRequest, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tools.update(
    tool_id="tol_rag_search",
    request=UpdateMcpToolRequest(),
)

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

**tool_id:** `str` — The unique identifier of the tool to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateToolRequest` 
    
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

<details><summary><code>client.tools.<a href="src/vectara/tools/client.py">test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a Lambda tool with test inputs to verify it works correctly.
This endpoint allows users to test their functions before using them with agents.
The function is executed in a secure sandbox environment with the same constraints as production.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.tools.test(
    tool_id="tol_python_function_123",
    input={"number": 42, "text": "Hello, world!"},
)

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

**tool_id:** `str` — The unique identifier of the Lambda tool to test.
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Dict[str, typing.Optional[typing.Any]]` — The input parameters to pass to the function. Must match the tool's input schema.
    
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

**timeout_seconds:** `typing.Optional[int]` — Maximum execution time in seconds. If not specified, uses the tool's configured timeout.
    
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

## Instructions
<details><summary><code>client.instructions.<a href="src/vectara/instructions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all instructions available to the authenticated user, with optional filtering and pagination.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.instructions.list(
    filter="support.*",
    enabled=True,
)
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

**filter:** `typing.Optional[str]` — A regular expression against instruction names and descriptions to filter the results.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Literal["initial"]]` — Filter instructions by type.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Filter instructions by enabled status.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of instructions to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of instructions after the limit has been reached.
    
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

<details><summary><code>client.instructions.<a href="src/vectara/instructions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new instruction that can guide agent behavior.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.instructions.create(
    name="Customer Support Initial Instruction",
    template="You are a helpful customer support agent for Acme Corp. Today's date is ${currentDate}. You have access to the following tools: #foreach($tool in $tools)${tool.name}#if($foreach.hasNext), #end#end",
)

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

**name:** `InstructionName` 
    
</dd>
</dl>

<dl>
<dd>

**template:** `str` — The instruction template content using the specified template engine.
    
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

**description:** `typing.Optional[str]` — A detailed description of what this instruction does.
    
</dd>
</dl>

<dl>
<dd>

**template_type:** `typing.Optional[TemplateType]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Arbitrary metadata associated with the instruction.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the instruction should be enabled upon creation.
    
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

<details><summary><code>client.instructions.<a href="src/vectara/instructions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the details of a specific instruction by its ID, including its template and configuration.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.instructions.get(
    instruction_id="ins_customer_support_init",
    version=1,
)

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

**instruction_id:** `InstructionId` — The unique identifier of the instruction to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — The specific version of the instruction to retrieve. If not specified, the latest version will be returned.
    
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

<details><summary><code>client.instructions.<a href="src/vectara/instructions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete an instruction and all its associated configuration. This action cannot be undone.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.instructions.delete(
    instruction_id="ins_customer_support_init",
)

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

**instruction_id:** `InstructionId` — The unique identifier of the instruction to delete.
    
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

<details><summary><code>client.instructions.<a href="src/vectara/instructions/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing instruction's template, metadata, and configuration.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.instructions.update(
    instruction_id="ins_customer_support_init",
)

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

**instruction_id:** `InstructionId` — The unique identifier of the instruction to update.
    
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

**name:** `typing.Optional[InstructionName]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A detailed description of what this instruction does.
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[str]` — The instruction template content using the specified template engine.
    
</dd>
</dl>

<dl>
<dd>

**template_type:** `typing.Optional[TemplateType]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Arbitrary metadata associated with the instruction.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the instruction is enabled.
    
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

<details><summary><code>client.instructions.<a href="src/vectara/instructions/client.py">test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Test an instruction by rendering its template with provided context data and tools.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.instructions.test(
    instruction_id="ins_customer_support_init",
    version=1,
)

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

**instruction_id:** `InstructionId` — The unique identifier of the instruction to test.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — The specific version of the instruction to test. If not specified, the latest version will be used.
    
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

**context:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Context data to use when rendering the instruction template.
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.Sequence[Tool]]` — List of tools to include in the instruction context for testing.
    
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

<details><summary><code>client.instructions.<a href="src/vectara/instructions/client.py">delete_version</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete the specified version of the instruction. This action cannot be undone.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.instructions.delete_version(
    instruction_id="ins_customer_support_init",
    version=1,
)

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

**instruction_id:** `InstructionId` — The unique identifier of the instruction to delete.
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` — The specific version of the instruction to delete.
    
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

## Agents
<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all agents available to the authenticated user, with optional filtering and pagination.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.agents.list(
    filter="support.*",
    enabled=True,
)
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

**filter:** `typing.Optional[str]` — A regular expression against agent names and descriptions to filter the results.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Filter agents by enabled status.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of agents to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of agents after the limit has been reached.
    
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

<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new agent. An agent is compromised as 3 main things of functionality:
  1. The instructions an agent follows. Known as a system in prompt in other platforms.
  2. The steps an agent follows when receiving an input.
  3. The tools an agent can use to resolve those steps and instructions.
Instructions are tied to each step, and should be well crafted so that the agent can perform the desired actions when given an input.

To use an agent, create a new session (called thread or chat in other platforms), and send new inputs to the agent to get responses.

Note: Only a single step is supported with no follow up steps. So the `first_step` will be only the only step. We will add multiple steps and step types to execute complex workflows, but many agents can work well with a single step.
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
from vectara import (
    AgentModel,
    ConversationalAgentStep,
    CorporaSearchQueryConfiguration,
    CorporaSearchToolParameters,
    DefaultOutputParser,
    InlineCorporaSearchToolConfiguration,
    ReferenceInstruction,
    SearchCorporaParameters,
    Vectara,
)

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.agents.create(
    name="Customer Support Agent",
    tool_configurations={
        "customer_search": InlineCorporaSearchToolConfiguration(
            argument_override=CorporaSearchToolParameters(
                query="customer support documentation",
            ),
            query_configuration=CorporaSearchQueryConfiguration(
                search=SearchCorporaParameters(),
            ),
        )
    },
    model=AgentModel(
        name="gpt-4",
    ),
    first_step=ConversationalAgentStep(
        instructions=[
            ReferenceInstruction(
                id="ins_customer_support_init",
            )
        ],
        output_parser=DefaultOutputParser(),
    ),
)

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

**name:** `AgentName` 
    
</dd>
</dl>

<dl>
<dd>

**tool_configurations:** `typing.Dict[str, AgentToolConfiguration]` — A map of tool configurations available to the agent. The key is the name of the tool configuration and the value is the AgentToolConfiguration.
    
</dd>
</dl>

<dl>
<dd>

**model:** `AgentModel` 
    
</dd>
</dl>

<dl>
<dd>

**first_step:** `ComponentsSchemasConversationalAgentStep` 
    
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

**key:** `typing.Optional[AgentKey]` — A user provided key that uniquely identifies this agent. If not provided, one will be auto-generated based on the agent name.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A detailed description of the agent's purpose and capabilities.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Arbitrary metadata associated with the agent for customization and configuration.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the agent should be enabled upon creation.
    
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

<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the details of a specific agent by its ID, including its configuration, capabilities, and associated resources.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.agents.get(
    agent_key="customer_support",
)

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

**agent_key:** `AgentKey` — The unique key of the agent to retrieve.
    
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

<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">replace</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Completely replace an existing agent's configuration, including its corpora, tools, and generation presets.
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
from vectara import (
    AgentModel,
    ConversationalAgentStep,
    CorporaSearchQueryConfiguration,
    CorporaSearchToolParameters,
    DefaultOutputParser,
    InlineCorporaSearchToolConfiguration,
    ReferenceInstruction,
    SearchCorporaParameters,
    Vectara,
)

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.agents.replace(
    agent_key="customer_support",
    name="Customer Support Agent",
    tool_configurations={
        "customer_search": InlineCorporaSearchToolConfiguration(
            argument_override=CorporaSearchToolParameters(
                query="customer support documentation",
            ),
            query_configuration=CorporaSearchQueryConfiguration(
                search=SearchCorporaParameters(),
            ),
        )
    },
    model=AgentModel(
        name="gpt-4",
    ),
    first_step=ConversationalAgentStep(
        instructions=[
            ReferenceInstruction(
                id="ins_customer_support_init",
            )
        ],
        output_parser=DefaultOutputParser(),
    ),
)

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

**agent_key:** `AgentKey` — The unique key of the agent to replace.
    
</dd>
</dl>

<dl>
<dd>

**name:** `AgentName` 
    
</dd>
</dl>

<dl>
<dd>

**tool_configurations:** `typing.Dict[str, AgentToolConfiguration]` — A map of tool configurations available to the agent. The key is the name of the tool configuration and the value is an agent tool configuration.
    
</dd>
</dl>

<dl>
<dd>

**model:** `AgentModel` 
    
</dd>
</dl>

<dl>
<dd>

**first_step:** `ComponentsSchemasConversationalAgentStep` 
    
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

**description:** `typing.Optional[str]` — A detailed description of the agent's purpose and capabilities.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Arbitrary metadata associated with the agent for customization and configuration.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the agent is enabled.
    
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

<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete an agent and all its associated configuration. This action cannot be undone.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.agents.delete(
    agent_key="customer_support",
)

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

**agent_key:** `AgentKey` — The unique key of the agent to delete.
    
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

<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing agent's configuration, including its corpora, tools, and generation presets.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.agents.update(
    agent_key="customer_support",
)

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

**agent_key:** `AgentKey` — The unique key of the agent to update.
    
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

**name:** `typing.Optional[AgentName]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A detailed description of the agent's purpose and capabilities.
    
</dd>
</dl>

<dl>
<dd>

**tool_configurations:** `typing.Optional[typing.Dict[str, AgentToolConfiguration]]` — A map of tool configurations available to the agent. The key is the name of the tool configuration and the value is an agent tool configuration.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[AgentModel]` 
    
</dd>
</dl>

<dl>
<dd>

**first_step:** `typing.Optional[ComponentsSchemasConversationalAgentStep]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Arbitrary metadata associated with the agent for customization and configuration.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the agent is enabled.
    
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

## Agent Sessions
<details><summary><code>client.agent_sessions.<a href="src/vectara/agent_sessions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all agent sessions for a specific agent, with optional filtering and pagination.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.agent_sessions.list(
    agent_key="customer_support",
    filter="support.*",
)
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

**agent_key:** `AgentKey` — The unique identifier of the agent to list sessions for.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — A regular expression against session names and descriptions to filter the results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of sessions to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of sessions after the limit has been reached.
    
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

<details><summary><code>client.agent_sessions.<a href="src/vectara/agent_sessions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new session for interacting with an agent. Sessions maintain conversation context.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.agent_sessions.create(
    agent_key="customer_support",
)

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

**agent_key:** `AgentKey` — The unique key of the agent to create a session for.
    
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

**key:** `typing.Optional[AgentSessionKey]` — A user provided key that uniquely identifies this session. If not provided, one will be auto-generated based on the session name.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Human-readable name for the session.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the session purpose or context.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Arbitrary metadata associated with the session.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the session should be enabled upon creation.
    
</dd>
</dl>

<dl>
<dd>

**tti_minutes:** `typing.Optional[int]` — Time-to-idle in minutes for the session. If no events occur in the session for this duration, the session will be automatically deleted. If set to 0, the session will not expire.
    
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

<details><summary><code>client.agent_sessions.<a href="src/vectara/agent_sessions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the details of a specific agent session by its ID, including session configuration.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.agent_sessions.get(
    agent_key="customer_support",
    session_key="customer_support_chat",
)

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

**agent_key:** `AgentKey` — The unique identifier of the agent.
    
</dd>
</dl>

<dl>
<dd>

**session_key:** `AgentSessionKey` — The unique key of the session to retrieve.
    
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

<details><summary><code>client.agent_sessions.<a href="src/vectara/agent_sessions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete an agent session. This action cannot be undone.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.agent_sessions.delete(
    agent_key="customer_support",
    session_key="customer_support_chat",
)

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

**agent_key:** `AgentKey` — The unique identifier of the agent.
    
</dd>
</dl>

<dl>
<dd>

**session_key:** `AgentSessionKey` — The unique key of the session to delete.
    
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

<details><summary><code>client.agent_sessions.<a href="src/vectara/agent_sessions/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing agent session's configuration and metadata.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.agent_sessions.update(
    agent_key="customer_support",
    session_key="customer_support_chat",
)

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

**agent_key:** `AgentKey` — The unique identifier of the agent.
    
</dd>
</dl>

<dl>
<dd>

**session_key:** `AgentSessionKey` — The unique key of the session to update.
    
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

**name:** `typing.Optional[str]` — Human-readable name for the session.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the session purpose or context.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Arbitrary metadata associated with the session.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the session is enabled.
    
</dd>
</dl>

<dl>
<dd>

**tti_minutes:** `typing.Optional[int]` — Time-to-idle in minutes for the session. If no events occur in the session for this duration, the session will be automatically deleted. If set to 0, the session will not expire.
    
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

## AgentEvents
<details><summary><code>client.agent_events.<a href="src/vectara/agent_events/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all events in a specific agent session, with optional pagination.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.agent_events.list(
    agent_key="customer_support",
    session_key="customer_support_chat",
)
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

**agent_key:** `AgentKey` — The unique identifier of the agent.
    
</dd>
</dl>

<dl>
<dd>

**session_key:** `AgentSessionKey` — The unique key of the session to list events for.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of events to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of events after the limit has been reached.
    
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

<details><summary><code>client.agent_events.<a href="src/vectara/agent_events/client.py">create_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new input to an agent to interact with it.
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
from vectara import AgentTextInput, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.agent_events.create_stream(
    agent_key="customer_support",
    session_key="customer_support_chat",
    messages=[
        AgentTextInput(
            content="I need help with my widget installation",
        )
    ],
)
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

**agent_key:** `AgentKey` — The unique identifier of the agent.
    
</dd>
</dl>

<dl>
<dd>

**session_key:** `AgentSessionKey` — The unique key of the session to create an input in.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[ComponentsSchemasAgentTextInput]` — List of inputs that make up this event.
    
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

<details><summary><code>client.agent_events.<a href="src/vectara/agent_events/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new input to an agent to interact with it.
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
from vectara import AgentTextInput, Vectara

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.agent_events.create(
    agent_key="customer_support",
    session_key="customer_support_chat",
    messages=[
        AgentTextInput(
            content="I need help with my widget installation",
        )
    ],
)

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

**agent_key:** `AgentKey` — The unique identifier of the agent.
    
</dd>
</dl>

<dl>
<dd>

**session_key:** `AgentSessionKey` — The unique key of the session to create an input in.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[ComponentsSchemasAgentTextInput]` — List of inputs that make up this event.
    
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

<details><summary><code>client.agent_events.<a href="src/vectara/agent_events/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the details of a specific event within an agent session.
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

client = Vectara(
    api_key="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.agent_events.get(
    agent_key="customer_support",
    session_key="customer_support_chat",
    event_id="aev_user_001",
)

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

**agent_key:** `AgentKey` — The unique identifier of the agent.
    
</dd>
</dl>

<dl>
<dd>

**session_key:** `AgentSessionKey` — The unique key of the session.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` — The unique identifier of the event to retrieve.
    
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

