# Reference
## Corpora
<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">list</a>(...) -> ListCorporaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The List Corpora API lets you retrieve a list of corpora in your account. This endpoint returns a paginated list of corpora objects, which contain basic information about each corpus. The returned corpus objects contain less detail compared to those retrieved the direct corpus retrieval operation.

You can specify optional parameters to control the pagination and filtering of the results. The limit parameter determines the maximum number of corpora to return, with a default value of 10 and a maximum value of 100.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.corpora.list(
    filter="Vectara Content",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">create</a>(...) -> Corpus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Create Corpus API lets you create a corpus to store and manage your documents. A corpus is a container for documents and their associated metadata. When creating a corpus, you can specify various settings such as the corpus key, name, description, encoder, and filter attributes.

## Corpus object

When you create a `corpus` object, the `corpus_key` property is required to uniquely identify the corpus. The `name` parameter is optional and defaults to the value of `key`. The optional `description` properties lets you provide additional information about the corpus. When creating a new corpus, you also have the flexibility to specify a custom `corpus_key` that follows a naming convention of your choice. This allows you to assign easily identifiable keys to your corpora, making it easier to manage and reference them in your application.

You can specify whether to treat queries or documents in the corpus as questions or answers using the `queries_are_answers` and `documents_are_questions` boolean properties. These settings affect the semantics of the encoder used at query time and indexing time.

## Add metadata as filter attributes

When creating a corpus with this endpoint or the Vectara Console, you define metadata fields using the `filter_attributes` object. This ensures the corpus supports filtering on specific metadata attributes, either at the document level or the part level.

Filter attributes enable you to attach metadata to your data at the document (`doc`) or `part` level, which you can use later in filter expressions to narrow the scope of your queries. A filter attribute must specify a unique `name` (up to 64 characters long), and a `level` which indicates whether it exists in the `doc` or `part` level metadata. At indexing time, metadata with this name is extracted and made available for filter expressions to operate on. [Learn more](https://docs.vectara.com/docs/build/prepare-data/metadata-filters)

### Doc and part filter levels

The `doc` attribute applies to the entire document. Use this for metadata that is consistent across the whole document, such as author, publication date, and document ID.

The `part` attribute applies to specific sections or chunks within a document. Use for metadata that may vary within different parts of the document, such as sections, page numbers, and sentiment scores.

If `indexed` is true, the system will build an index on the extracted values to further improve the performance of filter expressions involving the attribute.

Filter attributes must specify a `type`, which is validated when documents are indexed. The four supported types are `integer`, which stores signed whole-number values up to eight bytes in length; `real`, for storing floating point values in [IEEE 754 8-byte format]; `text` for storing textual strings in [UTF-8 encoding], and `boolean` for storing true/false values.

After you define filter attributes, you can use them within your queries. For example:
* Document-level attribute: `doc.publication_year > 2020`
* Part-level attribute: `part.sentiment_score > 0.7`

## Custom dimensions 
Custom dimensions let you add additional context to your data that contain user-defined values in addition to what Vectara automatically extracts and stores from the text. For example, *upvotes* can be a custom dimension. For example, see [Add custom dimensions to boost content](/docs/tutorials/add-custom-dimensions)."
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
from vectara import Vectara, FilterAttribute
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**key:** `CorpusKey` 
    
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

**filter_attributes:** `typing.Optional[typing.List[FilterAttribute]]` — The new filter attributes of the corpus. If unset then the corpus will not have filter attributes.
    
</dd>
</dl>

<dl>
<dd>

**custom_dimensions:** `typing.Optional[typing.List[CorpusCustomDimension]]` — A custom dimension is an additional numerical field attached to a document part. You can then multiply this numerical field with a query time custom dimension of the same name. This allows boosting (or burying) document parts for arbitrary reasons. This feature is only enabled for Pro and Enterprise customers.
    
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

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">get</a>(...) -> Corpus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Get Corpus API lets you view metadata about a specific corpus. This is useful for getting information about a corpus without performing a search. This operation does not search the corpus contents. Specify the `corpus_key` to identify the corpus whose metadata you want to retrieve.

This endpoint helps administrators understand the access control details and monitor the size of corpora to understand information like the amount of quota consumed. You can also use this information for optimizing search and storage utilization.

For example, you can track the read and write activity of a specific corpus which can help you change your security strategy proactively. You noticed a corpus with an API key with read/write access that is only being used for high volume reads. You may decide to switch to a read-only key.

In another case, you might respond to a security incident by disabling a specific corpus because of information returned by this endpoint.

## Get the number of documents or document parts in a corpus

Tracking the usage of documents in a corpus enables adminstrators to manage resource allocation efficiently. Monitoring corpus metrics also helps data usage stay within allocated quotas and identify trends in document growth and document segmentation.

The `limit` object in the response provides comprehensive information about the current usage and limits of a corpus including the number of stored documents, document parts, and character count.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

Permanently delete a corpus and all its associated data. The `corpus_key` uniquely identifies the corpus. 

Upon successful completion, space quota consumed by the corpus will be freed, and the corpus will no longer be useable for future indexing or querying.

:::note
The corpus_key assigned to the corpus will be released and can be reused.
:::
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">update</a>(...) -> Corpus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Update Corpus API lets you enable, disable, or update the name and description of a corpus. This is useful to manage the availability of data within the system, such as when you need to take the corpus offline without having to delete the corpus.

This lets you utilize automated scripts to programmatically control the availability of corpora based on certain conditions. For example, quickly disable a corpus for maintenance updates or in response to security incidents.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

Resets a corpus, which removes all documents and data from the specified corpus, while keeping the corpus itself. The `corpus_key` uniquely identifies the corpus. For more information, see [Create a corpus](https://docs.vectara.com/docs/rest-api/create-corpus).
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">replace_filter_attributes</a>(...) -> ReplaceFilterAttributesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace the filter attributes of a corpus. This does not happen immediately, as this operation creates a job that completes asynchronously. These new filter attributes will not work until the job completes.

You can monitor the status of the filter change using the returned job ID. The `corpus_key` uniquely identifies the corpus.
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
from vectara import Vectara, FilterAttribute
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**corpus_key:** `CorpusKey` — The unique key identifying the corpus having its filters replaced.
    
</dd>
</dl>

<dl>
<dd>

**filter_attributes:** `typing.List[FilterAttribute]` — The new filter attributes.
    
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

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">compute_size</a>(...) -> ComputeCorpusSizeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the current size of a corpus, including number of documents, parts, and characters. The `corpus_key` uniquely identifies the corpus.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">get_filter_attribute_stats</a>(...) -> GetFilterAttributeStatsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve statistics and value distributions for filter attributes in a corpus. This endpoint provides insights into the metadata structure and content distribution, enabling users to understand available filter values and build effective metadata queries.

This endpoint analyzes document and part metadata fields defined as filter attributes and returns:
- **Value distributions**: Top occurring values with their counts
- **Statistics**: Min, max, average, and sum for numeric fields

By default, statistics are computed across all filter attributes at both document and part levels. You can optionally:
- Request statistics for specific fields only
- Apply metadata filters to analyze a subset of the corpus
- Limit the number of distinct values returned per field

**Performance and Caching**: Results may be cached for improved performance, with cache duration varying by corpus size. Cached results can take up to 1 hour to refresh for large corpora. Smaller corpora with faster query times have shorter cache durations (2-15 minutes) to ensure fresher data.

The `corpus_key` uniquely identifies the corpus. For more information, see [Create a corpus](https://docs.vectara.com/docs/rest-api/create-corpus).
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.corpora.get_filter_attribute_stats(
    corpus_key="my-corpus",
    fields="doc.category,doc.year,part.status",
    metadata_filter="doc.year >= 2020 AND doc.category = \'financial\'",
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

**corpus_key:** `CorpusKey` — The unique key identifying the corpus to retrieve filter attribute statistics for.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of qualified field names to retrieve statistics for (e.g., 'doc.category,part.status'). If omitted, returns statistics for all filter attributes in the corpus. Field names must match the qualified format 'level.fieldname' where level is either 'doc' or 'part'.
    
</dd>
</dl>

<dl>
<dd>

**metadata_filter:** `typing.Optional[str]` — Optional metadata filter expression to pre-filter documents or parts before computing statistics. Uses the same SQL-style filter syntax as query operations. When provided, statistics reflect only the filtered subset of the corpus.
    
</dd>
</dl>

<dl>
<dd>

**max_values:** `typing.Optional[int]` — Maximum number of distinct values to return per field in the 'values' array, ordered by occurrence count (descending).
    
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

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">search</a>(...) -> QueryFullResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The [**Query APIs**](/docs/rest-api/queries) enable Retrieval Augmented Generation (RAG), allowing you to search your data and generate AI-powered summaries. Vectara provides three query types to match different search needs:

* [**Single corpus query**](/docs/rest-api/search-corpus): For a simple search within a single data source.
* [**Advanced single corpus query**](/docs/rest-api/query-corpus): For full-featured search and RAG within one corpus, supporting advanced features like table summarization, metadata filtering, and reranking.
* [**Multiple corpora query**](/docs/rest-api/query): For searching across one or more corpora with full RAG capabilities.

Search a single corpus with a straightforward query request, specifying the corpus key and query parameters.

* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is created in the Vectara Console or the [Create Corpus API](https://docs.vectara.com/docs/rest-api/create-corpus), and the corpus key is part of that process. When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests.
* Enter the search `query` string for the corpus, which is the question you want to ask.
* Set the maximum number of results (`limit`) to return. **Default**: 10, **minimum**: 1
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.corpora.search(
    corpus_key="my-corpus",
    query="Explain changes in VaR metrics over last quarter",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">query_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform an advanced query on a specific corpus to find relevant results, generate summaries, highlight relevant snippets, and use Retrieval Augmented Generation.

This endpoint expands on the simple GET version by allowing full customization of:
- **Search parameters**: Control pagination (`offset`, `limit`), apply metadata filters, and specify lexical interpolation to balance neural and keyword-based retrieval.
- **Hybrid search**: Adjust the `lexical_interpolation` value between `0.0` (purely neural) and `1.0` (purely lexical). Typical best results are between `0.01` and `0.1`.
- **Reranking**: Apply advanced rerankers such as Multilingual, MMR, Chain, or User Defined Function rerankers to improve result relevance.
- **Generation (RAG)**: Include a `generation` object to enable grounded summarization with your own data, citations, and factual consistency scoring.
- **Streaming**: Optionally stream results or generated summaries in real time with `stream_response`.

Each query must include the `corpus_key` path parameter that identifies the target corpus. The response contains one or more subdocuments representing the most relevant passages, along with any generated summaries or citations.

**Typical use cases**
- Perform a semantically rich search over a large, domain-specific corpus.
- Retrieve relevant text passages and apply reranking for better result diversity.
- Generate contextually grounded answers or summaries using Retrieval Augmented Generation.

## Basic query

This basic query example has a minimal configuration:

```json
{
  "query": "What are black holes?",
  "search": {
    "corpora": [{
      "corpus_key": "my-corpus" 
    }],
  },
  "generation": {
    "generation_preset_name": "mockingbird-2.0",
    "max_used_search_results": 20 
  }
}
```

## Request body parameters

The request body is a JSON object containing the `query`, `search`, and optional `generation` objects.

`query` (string, required) - (Required) The search query text.
`search` (string, required) - (Required) An object that controls the retrieval and reranking process.

`search.corpora` - An array specifying which corpus to search. For this endpoint, the array will contain a single object.

* `corpus_key` (string, required): The unique ID of the corpus to search.
* `metadata_filter` (string, optional): A SQL-like filter to narrow results. For syntax and examples, see the Filters guide.
* `lexical_interpolation` (float, optional): A value between 0.0 (pure neural search) and 1.0 (pure keyword search) to enable hybrid search. A recommended starting point is 0.025.
* `custom_dimensions` (object, optional): An object to boost or bury results based on custom dimensions. See the Custom Dimensions guide for details.

`search.limit` (integer, optional) - The maximum number of results to retrieve before reranking. **Default**: 10

`search.offset` (integer, optional) - The number of results to skip for pagination. **Default**: 0

`search.context_configuration` (object, optional) - Configuration for surrounding context to include with each search result.
* `sentences_before` (integer): Number of sentences to include before the matching text.
* `sentences_after` (integer): Number of sentences to include after the matching text.
* `characters_before` (integer): Number of characters to include before the matching text.
* `characters_after` (integer): Number of characters to include after the matching text.
* `start_tag` (string): HTML-style tag to wrap the beginning of the retrieved context (e.g., `<b>`).
* `end_tag` (string): HTML-style tag to wrap the end of the retrieved context (e.g., `</b>`).
:::note
You can only use sentences before/after OR characters before/after, but not both.
:::

Example:

```json
{
  "context_configuration": {
    "sentences_before": 2,
    "sentences_after": 2,
    "start_tag": "<mark>",
    "end_tag": "</mark>"
  }
}
```

`search.reranker` (object, optional) - Configures a reranker to improve result quality by reordering search results to place the most relevant content first. For more details, see [Reranking overview](/docs/search-and-retrieval/rerankers/reranking-overview).
* `type` (string): The reranker type. Options include customer_reranker (default multilingual reranker), mmr (for result diversity), or none.
* `reranker_name` (string): The specific reranker model to use (e.g., Rerank_Multilingual_v1).
* `limit` (integer): Maximum number of results to return after reranking.
* `cutoff` (float): Minimum relevance score (between 0.0 and 1.0) for a result to be included. A typical range is 0.3-0.7.
* `include_context` (boolean): If true, uses surrounding context text for more accurate reranking.

**Example:**

```json
{
  "reranker": {
    "type": "customer_reranker",
    "reranker_name": "Rerank_Multilingual_v1",
    "limit": 50,
  }
}
```

`generation` (object, optional) - An object that controls how the agent creates natural language responses. If this object is excluded, summarization is disabled.

`generation.generation_preset_name` (string, optional) - The name of the pre-configured prompt and LLM bundle.

**Recommended Presets:**

* `mockingbird-2.0`: Vectara's cutting-edge LLM for RAG.
* `vectara-summary-ext-24-05-med-omni`: (gpt-4o, optimized for citations)
* `vectara-summary-ext-24-05-large`: (gpt-4.0-turbo, optimized for citations)
* `vectara-summary-ext-24-05-sml`: (gpt-3.5-turbo, optimized for citations)


**For Tabular data:**

`vectara-summary-table-query-ext-dec-2024-gpt-4o`

`generation.prompt_template` (string, optional) - A custom prompt template in JSON format that defines the system and user messages for the LLM. Use this to customize the behavior of the model beyond the preset. The template can include Velocity templates with variables such as `$vectaraQueryResults` to reference retrieved search results. For more information, see [Custom prompts](/docs/prompts/vectara-prompt-engine).

`generation.max_used_search_results` (integer, optional) - The maximum number of top search results to send for summarization. The number of top search results to send to the LLM for summarization. Increasing this can create a more comprehensive summary but may increase response time. **Default limit**: 25.

:::caution
Setting this value too high may prevent the model from generating a response.
:::

`generation.response_language` (string, optional) - The language code for the response (e.g. `eng`, `spa`, `deu`). Set this to `auto` to have Vectara guess the language, but we recommend specifying your preferred language for best results.

`generation.citations` (object, optional) - Configuration for including citations in the generated summary.
* `style` (string): Citation style. Options are `markdown`, `html`, or `none`.
* `url_pattern` (string): A URL template for citation links, where `{doc.id}` will be replaced with the document ID.
* `text_pattern` (string): A text template for citation display, where `{doc.title}` will be replaced with the document title.

**Example:**

```json
{
  "citations": {
    "style": "markdown",
    "url_pattern": "https://docs.example.com/documents/{doc.id}",
    "text_pattern": "{doc.title}"
  }
}
```

`generation.model_parameters` (object, optional) - Custom parameters for the underlying LLM that overwrites the defaults of `generation_preset_name`.
* `temperature` (float): Controls randomness in the output. Higher values (e.g., 0.8) produce more creative results, while lower values (e.g., 0.2) yield more focused and deterministic outputs.
* `max_tokens` (integer): The maximum number of tokens to generate in the response.
* `frequency_penalty` (float): Decreases the use of repeating words, reducing repetition. **Default**: `0.0` to `1.0`.
* `presence_penalty` (float): Increases the chance for the model to introduce new topics. **Default**: `0.0` to `1.0`.

**Example:**

```json
{
  "model_parameters": {
    "temperature": 0.7,
    "max_tokens": 500,
    "frequency_penalty": 0.5,
    "presence_penalty": 0.3
  }
}
```

`generation.enable_factual_consistency_score` (boolean): If true, includes a factual consistency score in the response to indicate how well the generated summary aligns with the retrieved documents.
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
from vectara import Vectara, ContextConfiguration, SearchReranker_CustomerReranker, GenerationParameters, CitationParameters
from vectara.environment import VectaraEnvironment
from vectara.corpora import QueryCorporaStreamRequestSearch

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.corpora.query_stream(
    corpus_key="my-corpus",
    query="How to configure OAuth2 for microservices in Kubernetes?",
    search=QueryCorporaStreamRequestSearch(
        limit=50,
        context_configuration=ContextConfiguration(
            sentences_before=2,
            sentences_after=2,
            start_tag="<em>",
            end_tag="</em>",
        ),
        reranker=SearchReranker_CustomerReranker(),
        metadata_filter="doc.topic = \'authentication\' and doc.platform = \'kubernetes\'",
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

**stream_response:** `typing.Literal` — Indicates whether the response should be streamed or not.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[QueryCorporaStreamRequestSearch]` — The parameters to search one corpus.
    
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

<details><summary><code>client.corpora.<a href="src/vectara/corpora/client.py">query</a>(...) -> QueryCorporaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform an advanced query on a specific corpus to find relevant results, generate summaries, highlight relevant snippets, and use Retrieval Augmented Generation.

This endpoint expands on the simple GET version by allowing full customization of:
- **Search parameters**: Control pagination (`offset`, `limit`), apply metadata filters, and specify lexical interpolation to balance neural and keyword-based retrieval.
- **Hybrid search**: Adjust the `lexical_interpolation` value between `0.0` (purely neural) and `1.0` (purely lexical). Typical best results are between `0.01` and `0.1`.
- **Reranking**: Apply advanced rerankers such as Multilingual, MMR, Chain, or User Defined Function rerankers to improve result relevance.
- **Generation (RAG)**: Include a `generation` object to enable grounded summarization with your own data, citations, and factual consistency scoring.
- **Streaming**: Optionally stream results or generated summaries in real time with `stream_response`.

Each query must include the `corpus_key` path parameter that identifies the target corpus. The response contains one or more subdocuments representing the most relevant passages, along with any generated summaries or citations.

**Typical use cases**
- Perform a semantically rich search over a large, domain-specific corpus.
- Retrieve relevant text passages and apply reranking for better result diversity.
- Generate contextually grounded answers or summaries using Retrieval Augmented Generation.

## Basic query

This basic query example has a minimal configuration:

```json
{
  "query": "What are black holes?",
  "search": {
    "corpora": [{
      "corpus_key": "my-corpus" 
    }],
  },
  "generation": {
    "generation_preset_name": "mockingbird-2.0",
    "max_used_search_results": 20 
  }
}
```

## Request body parameters

The request body is a JSON object containing the `query`, `search`, and optional `generation` objects.

`query` (string, required) - (Required) The search query text.
`search` (string, required) - (Required) An object that controls the retrieval and reranking process.

`search.corpora` - An array specifying which corpus to search. For this endpoint, the array will contain a single object.

* `corpus_key` (string, required): The unique ID of the corpus to search.
* `metadata_filter` (string, optional): A SQL-like filter to narrow results. For syntax and examples, see the Filters guide.
* `lexical_interpolation` (float, optional): A value between 0.0 (pure neural search) and 1.0 (pure keyword search) to enable hybrid search. A recommended starting point is 0.025.
* `custom_dimensions` (object, optional): An object to boost or bury results based on custom dimensions. See the Custom Dimensions guide for details.

`search.limit` (integer, optional) - The maximum number of results to retrieve before reranking. **Default**: 10

`search.offset` (integer, optional) - The number of results to skip for pagination. **Default**: 0

`search.context_configuration` (object, optional) - Configuration for surrounding context to include with each search result.
* `sentences_before` (integer): Number of sentences to include before the matching text.
* `sentences_after` (integer): Number of sentences to include after the matching text.
* `characters_before` (integer): Number of characters to include before the matching text.
* `characters_after` (integer): Number of characters to include after the matching text.
* `start_tag` (string): HTML-style tag to wrap the beginning of the retrieved context (e.g., `<b>`).
* `end_tag` (string): HTML-style tag to wrap the end of the retrieved context (e.g., `</b>`).
:::note
You can only use sentences before/after OR characters before/after, but not both.
:::

Example:

```json
{
  "context_configuration": {
    "sentences_before": 2,
    "sentences_after": 2,
    "start_tag": "<mark>",
    "end_tag": "</mark>"
  }
}
```

`search.reranker` (object, optional) - Configures a reranker to improve result quality by reordering search results to place the most relevant content first. For more details, see [Reranking overview](/docs/search-and-retrieval/rerankers/reranking-overview).
* `type` (string): The reranker type. Options include customer_reranker (default multilingual reranker), mmr (for result diversity), or none.
* `reranker_name` (string): The specific reranker model to use (e.g., Rerank_Multilingual_v1).
* `limit` (integer): Maximum number of results to return after reranking.
* `cutoff` (float): Minimum relevance score (between 0.0 and 1.0) for a result to be included. A typical range is 0.3-0.7.
* `include_context` (boolean): If true, uses surrounding context text for more accurate reranking.

**Example:**

```json
{
  "reranker": {
    "type": "customer_reranker",
    "reranker_name": "Rerank_Multilingual_v1",
    "limit": 50,
  }
}
```

`generation` (object, optional) - An object that controls how the agent creates natural language responses. If this object is excluded, summarization is disabled.

`generation.generation_preset_name` (string, optional) - The name of the pre-configured prompt and LLM bundle.

**Recommended Presets:**

* `mockingbird-2.0`: Vectara's cutting-edge LLM for RAG.
* `vectara-summary-ext-24-05-med-omni`: (gpt-4o, optimized for citations)
* `vectara-summary-ext-24-05-large`: (gpt-4.0-turbo, optimized for citations)
* `vectara-summary-ext-24-05-sml`: (gpt-3.5-turbo, optimized for citations)


**For Tabular data:**

`vectara-summary-table-query-ext-dec-2024-gpt-4o`

`generation.prompt_template` (string, optional) - A custom prompt template in JSON format that defines the system and user messages for the LLM. Use this to customize the behavior of the model beyond the preset. The template can include Velocity templates with variables such as `$vectaraQueryResults` to reference retrieved search results. For more information, see [Custom prompts](/docs/prompts/vectara-prompt-engine).

`generation.max_used_search_results` (integer, optional) - The maximum number of top search results to send for summarization. The number of top search results to send to the LLM for summarization. Increasing this can create a more comprehensive summary but may increase response time. **Default limit**: 25.

:::caution
Setting this value too high may prevent the model from generating a response.
:::

`generation.response_language` (string, optional) - The language code for the response (e.g. `eng`, `spa`, `deu`). Set this to `auto` to have Vectara guess the language, but we recommend specifying your preferred language for best results.

`generation.citations` (object, optional) - Configuration for including citations in the generated summary.
* `style` (string): Citation style. Options are `markdown`, `html`, or `none`.
* `url_pattern` (string): A URL template for citation links, where `{doc.id}` will be replaced with the document ID.
* `text_pattern` (string): A text template for citation display, where `{doc.title}` will be replaced with the document title.

**Example:**

```json
{
  "citations": {
    "style": "markdown",
    "url_pattern": "https://docs.example.com/documents/{doc.id}",
    "text_pattern": "{doc.title}"
  }
}
```

`generation.model_parameters` (object, optional) - Custom parameters for the underlying LLM that overwrites the defaults of `generation_preset_name`.
* `temperature` (float): Controls randomness in the output. Higher values (e.g., 0.8) produce more creative results, while lower values (e.g., 0.2) yield more focused and deterministic outputs.
* `max_tokens` (integer): The maximum number of tokens to generate in the response.
* `frequency_penalty` (float): Decreases the use of repeating words, reducing repetition. **Default**: `0.0` to `1.0`.
* `presence_penalty` (float): Increases the chance for the model to introduce new topics. **Default**: `0.0` to `1.0`.

**Example:**

```json
{
  "model_parameters": {
    "temperature": 0.7,
    "max_tokens": 500,
    "frequency_penalty": 0.5,
    "presence_penalty": 0.3
  }
}
```

`generation.enable_factual_consistency_score` (boolean): If true, includes a factual consistency score in the response to indicate how well the generated summary aligns with the retrieved documents.
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
from vectara import Vectara, ContextConfiguration, SearchReranker_CustomerReranker, GenerationParameters, CitationParameters
from vectara.environment import VectaraEnvironment
from vectara.corpora import QueryCorporaStreamRequestSearch

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.corpora.query_stream(
    corpus_key="my-corpus",
    query="How to configure OAuth2 for microservices in Kubernetes?",
    search=QueryCorporaStreamRequestSearch(
        limit=50,
        context_configuration=ContextConfiguration(
            sentences_before=2,
            sentences_after=2,
            start_tag="<em>",
            end_tag="</em>",
        ),
        reranker=SearchReranker_CustomerReranker(),
        metadata_filter="doc.topic = \'authentication\' and doc.platform = \'kubernetes\'",
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

**stream_response:** `typing.Literal` — Indicates whether the response should be streamed or not.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[QueryCorporaRequestSearch]` — The parameters to search one corpus.
    
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
<details><summary><code>client.upload.<a href="src/vectara/upload/client.py">file</a>(...) -> Document</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a file to a corpus for automatic text extraction, chunking, and indexing. This endpoint is designed for unstructured documents where you want Vectara to handle parsing for you. Each uploaded file can be up to **10 MB**.

Supported file types include:
- Markdown (`.md`)
- PDF/A (`.pdf`)
- OpenOffice documents (`.odt`)
- Microsoft Word (`.doc`, `.docx`)
- Microsoft PowerPoint (`.ppt`, `.pptx`)
- Plain text (`.txt`)
- HTML (`.html`)
- LXML (`.lxml`)
- RTF (`.rtf`)
- EPUB (`.epub`)
- Email files (RFC 822)   

:::note
For semi-structured documents that require more control over fields or metadata, use the [**Create Corpus Document API**](/docs/rest-api/create-corpus-document) instead.
:::

## Additional format support through Vectara Ingest

If you need to ingest additional file types or data sources, you can use the open-source [**Vectara Ingest**](https://github.com/vectara/vectara-ingest) Python framework. It supports connectors for websites, RSS feeds, CSV, Confluence, HubSpot, ServiceNow, Jira, Notion, Slack, MediaWiki, GitHub, SharePoint, Twitter/X, YouTube, and more.

:::caution
Vectara Ingest is provided as an open-source example and is not officially supported.
:::

## Multipart form fields

This endpoint expects a `multipart/form-data` request with the following fields:

- **metadata** (optional): JSON metadata to attach to the parsed document.  
  Example: `metadata={"key":"value"}`
- **chunking_strategy** (optional): Controls how extracted text is chunked.  
  Defaults to sentence-based chunking (one chunk per sentence).  
  Example: `{"type":"sentence_chunking_strategy"}`. 
  Example for max character chunking: `{"type":"max_chars_chunking_strategy","max_chars_per_chunk":512}`
- **table_extraction_config** (optional): Enables extraction of tables from supported file types such as PDFs.  
  Example: `{"extract_tables": true}`
- **file** (required): The file to upload.
- **filename** (required): The desired document ID, specified within the file upload field.

Apart from these parameters, the servers expect a valid JWT Token in the HTTP headers:

```curl
\$ curl -L -X POST 'https://api.vectara.io/v2/corpora/:corpus_key/upload_file' \
-H 'Content-Type: multipart/form-data' \
-H 'Accept: application/json' \
-H 'x-api-key: zwt_123456' \
-F 'metadata=\{"key": "value"\};type=application/json' \
-F 'file=@/path/to/file/file.pdf;filename=desired_filename.pdf'

```

## Filenames with non-ASCII characters

When uploading files with non-ASCII (non-English) characters, such as Russian or Chinese, ensure that the filename is URL encoded. The Vectara REST API follows web standards which require URL-encoded file names.

## Set the document ID
  
To set a custom Document ID, pass it as the filename in the `Content-Disposition` header:

`Content-Disposition: form-data; name="file"; filename="your_document_id"`

For more information about Content-Disposition, see the [Mozilla documentation on headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition).

## Attach additional metadata

You can attach additional metadata to the file by specifying a metadata form field, which can contain a JSON string:

`{ "filesize": 1234 }`

## Tabular data extraction and summarization

Setting `table_extraction_config.extract_tables = true` enables extraction of tabular data (such as financial filings such as 10-K, 10-Q, S-1). You can also apply custom prompt templates to summarize table content during upload.

:::caution
Table extraction does not support scanned images of tables.
:::

## Custom table summarization with prompt templates

Vectara supports [table summarization using custom prompt templates](https://docs.vectara.com/docs/build/working-with-tables#summarize-tables-with-custom-prompts) during document upload. This lets you define custom prompt templates that control how the LLM interprets and summarizes table data during extraction. By customizing the prompt_template, you can tailor summaries for domain-specific language, analytical perspectives, or formatting preferences.

## Image support
You can include images in structured documents using the [Indexing API](/docs/rest-api/create-corpus-document) with Base64 encoding. You cannot send images directly with individual query requests. If you want to retrieve a specific image that is embedded within a document, use the [Retrieve image API](/docs/rest-api/get-image)
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.upload.file(
    corpus_key="my-corpus",
    file="example_file",
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

**file:** `core.File` — Binary file contents. The file name of the file will be used as the document ID.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arbitrary object that will be attached as document metadata to the extracted document.
    
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
<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">list</a>(...) -> ListDocumentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The List Documents API enables you to retrieve a list of documents stored in a specific corpus. This endpoint provides an overview of document metadata, including document IDs, tables (if table extraction is enabled), and pagination details. 

Use this API for viewing documents indexed so far and helping you decide to remove documents that are no longer needed. It helps you manage the document lifecycle in your environment.

This information enables you to catalog and inventory large amounts of data while also retrieving lists of documents for further analysis. For example, developers can utilize the metadata to to build custom search and filtering capabilities into their applications. If you enabled tabled extraction, this endpoint also returns the tables that this document contains.

Currently Document Admin APIs do not allow you to access the text of your documents.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.documents.list(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">create</a>(...) -> Document</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a document to a corpus for indexing, making its content available for search, retrieval, and generation. This endpoint supports two ingestion modes: **structured** documents and **core** documents. These modes offer different levels of control over document structure and chunking.

Each document becomes part of a corpus. You can use this API directly or with [Vectara Ingest](https://github.com/vectara/vectara-ingest) or the [File Upload API](/docs/rest-api/upload-file).

## Structured documents

Structured documents provide a natural hierarchy where Vectar handles chunking and metadata automatically. Structured documents are ideal when you want to index documents that have logical organization (titles, sections, paragraphs, and optionally tables or images) but prefer Vectara to manage how the content is split into search-optimized units.

Each structured document contains:
- A unique `id` and optional `title`, `description`, and `metadata`.
- An array of `sections`, each with its own title, text, and optional nested sections, tables, or images.
- Optional `custom_dimensions` that can influence ranking during search.

When indexed, Vectara partitions the text into document parts automatically using an intelligent sentence- or character-based chunking strategy. This lets you ingest data with minimal pre-processing while maintaining semantic integrity across context boundaries.

Structured documents are recommended for content with well-defined sections such as reports, articles, FAQs, or documentation.

## Core documents

Core documents offer fine-grained, explicit control of every part of a document that becomes searchable. Instead of providing a hierarchical structure, you specify each **document part** directly as unit that maps 1:1 to a search result or embedding.

A core document includes:
- A unique `id` and optional `metadata`.
- A list of `document_parts`, where each part includes `text`, optional `context`, `metadata`, and `custom_dimensions`.
- Optional `tables` and `images`, allowing you to represent complex structured data like spreadsheets or charts.

Core documents are designed for advanced use cases such as precise chunk-level optimization or experimental corpus structures, and applications where metadata-driven retrieval or ranking must be explicitly controlled.

## Chunking strategies    

By default, Vectara uses **sentence-based chunking**, which provides optimal retrieval accuracy for most datasets.

For larger documents or performance-tuned ingestion, you can explicitly set a `chunking_strategy`:
- `sentence_chunking_strategy` — creates one chunk per sentence (default).
- `max_chars_chunking_strategy` — creates larger chunks up to a specified character limit (`max_chars_per_chunk`), balancing retrieval speed with contextual coherence.
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
from vectara import Vectara, CreateDocumentRequest_Structured, StructuredDocumentSection
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.documents.create(
    corpus_key="my-corpus-key",
    request=CreateDocumentRequest_Structured(
        id="my-doc-id",
        sections=[
            StructuredDocumentSection(
                id=1,
                title="A nice title.",
                text="I\'m a nice document section.",
                metadata={
                    "section": "1.1"
                },
            ),
            StructuredDocumentSection(
                id=2,
                title="Another nice title.",
                text="I\'m another document section on something else.",
                metadata={
                    "section": "1.2"
                },
            )
        ],
        metadata={
            "url": "https://example.com"
        },
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

**wait_for:** `typing.Optional[CreateDocumentsRequestWaitFor]` 

Controls how long the request waits before returning a response.
- `searchable` (default): Waits until the document is fully indexed and immediately searchable. Use this when you need to query the document immediately after indexing.
- `indexed`: Waits until the document is durably stored and will be included in future search results. This is faster but the document may not appear in search results for a brief period after the response.

Both modes return a successful response once the specified condition is met.
    
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

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">bulk_delete</a>(...) -> BulkDeleteDocumentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates an asynchronous bulk delete operation for documents in a corpus.
This operation accepts a metadata filter, a list of specific document IDs, or both.

**Important**: This is a best-effort operation.
See the response schema documentation for details on the behavior differences between `metadata_filter` and `document_ids` parameters.

The operation runs as a background workflow.
Use the returned `job_id` to track progress via the Jobs API.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.documents.bulk_delete(
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

**corpus_key:** `CorpusKey` — The unique key identifying the corpus containing documents to delete.
    
</dd>
</dl>

<dl>
<dd>

**metadata_filter:** `typing.Optional[str]` 

Filter documents by metadata. Uses the same expression as a query metadata filter.
Example: `doc.status = 'archived' AND doc.year < 2020`
    
</dd>
</dl>

<dl>
<dd>

**document_ids:** `typing.Optional[str]` — Comma-separated list of document IDs to delete. Maximum 10,000 IDs per request.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` 

Whether to perform the deletion asynchronously.
- `true` (default): Returns immediately with job_id to track progress (HTTP 202)
- `false`: Waits for completion and returns deletion results (HTTP 200)

When `async=false`, the operation will wait for the deletion to complete up to the timeout specified in the `Request-Timeout` or `Request-Timeout-Millis` header.
If no timeout header is provided, defaults to 7 days.
If the operation times out, returns HTTP 504 with job_id to track via Jobs API.

The workflow continues running in the background even if the API wait times out.
    
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

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">get</a>(...) -> Document</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Retrieve Document API enables you to fetch the content and metadata of a specific document from a corpus, identified by its unique `document_id` from a specific corpus. Use this endpoint to view the full details of a document, including its text, metadata, and associated tables, if table extraction is enabled.

This information is particularly useful when you need to analyze the details of a specific document or integrate document content into your application workflows.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.documents.get(
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">update</a>(...) -> Document</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request:** `UpdateDocumentRequest` 
    
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

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">update_metadata</a>(...) -> Document</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request:** `UpdateDocumentRequest` 
    
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

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">summarize</a>(...) -> SummarizeDocumentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Organizations often struggle with extracting relevant insights from extensive documentation, such as vendor quotes, financial statements, and technical reports. Manually reviewing these documents is both time-consuming and prone to errors. 

The tech preview of the Documentation Summarization API enables users to generate concise summaries that capture essential insights from single documents without having to process entire documents manually. Efficiently process large documents, extract key insights, and interact with real-time data summaries.

* Enable streaming for large documents to receive summaries incrementally.
* Customize `prompt_template` to fine-tune summary output for specific domains.
* Use standard responses for small documents where streaming is unnecessary.
* Monitor streaming events to track the progress of real-time summarization.

:::note
The documentation length is limited by the context window of your selected LLM.
:::

## Response formats

The API supports two response modes:

* **Standard**: Provides a complete summary in one response.
* **Streaming** Provides incremental responses using Server-Sent Events (SSE).

### Non-streaming response

In standard mode, the API returns a structured response containing the complete summary of the document. The summary field contains the generated text, enabling users to extract essential information quickly.

### Streaming response

For streaming responses, the API returns Server-Sent Events (SSE). The first event begins streaming partial results as soon as they are available, while the final event marks the end of the summarization process.

The streamed response consists of multiple events:

* `generation_info`: Contains the `rendered_prompt` which is the compiled prompt sent to the LLM for document summarization.
* `generation_chunk`: Returns partial chunk of the generated summary.
* `generation_end`: Marks the completion of the summary generation.
* `error`: Returns an error message if summarization fails.
* `end`: Indicates the end of the streaming session.

## Prompt template example

When crafting a prompt, you can access your document with the `$vectaraDocument` field. This example shows a simple prompt:

```json
{
  "role": "user",
  "content": "Summarize the document: \$vectaraDocument.json()"
}
```
The document also has the following methods to support custom prompts. 

* `$vectaraDocument.json()`: Provides a JSON representation of the whole document.
* `$vectaraDocument.id()`: Specifies the unique identifier of the document (`document_id`)
* `$vectaraDocument.metadata()`: Specifies metadata from the document.  
  For example, 
  `$vectaraDocument.metadata().get("key")` retrieves a specific metadata value by key.
* `$vectaraDocument.parts()`: Returns an array of document parts which you can look through.  
  For example, `#foreach ($part in $vectaraDocument.parts())`.  
* `$part.text()`: Retrieves the text of the part.
* `$part.metadata()`: Retrieves metadata of a part.
* `$part.hasTable()`: Determines if the part contains a table.
* `$part.table()`: Provides access to the table within the part. For example, use `$part.table().json()` to retrieve the table in JSON format.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.documents.summarize(
    corpus_key="my-corpus",
    document_id="document_id",
    llm_name="mockingbird-2.0",
    prompt_template="Summarize the key clauses of the employment contract in ${document.metadata.jurisdiction}, focusing on arbitration, confidentiality, and termination terms.",
    model_parameters={
        "max_tokens": 200,
        "temperature": 0.7
    },
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

**prompt_template:** `typing.Optional[str]` — The prompt template to use when generating the summary. Vectara manages both system and user roles and prompts for the generative LLM out of the box by default. However, users can override the `prompt_template` via this variable. The `prompt_template` is in the form of an Apache Velocity template. For more details on how to configure the `prompt_template`, see the [long-form documentation](https://docs.vectara.com/docs/prompts/vectara-prompt-engine).
    
</dd>
</dl>

<dl>
<dd>

**model_parameters:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional parameters for the specified model used when generating the summary.
    
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

<details><summary><code>client.documents.<a href="src/vectara/documents/client.py">get_image</a>(...) -> Image</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.documents.get_image(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Metadata
<details><summary><code>client.metadata.<a href="src/vectara/metadata/client.py">query_metadata</a>(...) -> MetadataQueryResponse</code></summary>
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
from vectara import Vectara, FieldQuery
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.metadata.query_metadata(
    corpus_key="my-corpus",
    queries=[
        FieldQuery(
            field="title",
            query="lease agreement",
            weight=2,
        ),
        FieldQuery(
            field="category",
            query="contract",
            weight=1,
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

**corpus_key:** `CorpusKey` — The unique key identifying the corpus to search for metadata.
    
</dd>
</dl>

<dl>
<dd>

**queries:** `typing.List[FieldQuery]` — List of field-specific queries to apply fuzzy matching.
    
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
<details><summary><code>client.queries.<a href="src/vectara/queries/client.py">query_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform a multipurpose query to retrieve relevant information from one or more corpora and generate a response using Retrieval Augmented Generation (RAG). Similar to the [advanced corpora search](https://docs.vectara.com/docs/rest-api/query-corpus).

* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is created in the Vectara Console or the [Create Corpus API](https://docs.vectara.com/docs/rest-api/create-corpus), and the corpus key is part of that process. When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests.
* Customize your search by specifying the query text (`query`), pagination details (`offset` and `limit`), and metadata filters (`metadata_filter`) to tailor your search results.
* Leverage advanced search capabilities like reranking (`reranker`) and opt-in Retrieval Augmented Generation (RAG) (`generation`) for enhanced query performance. Generation is opt-in by setting the `generation` property. By excluding the property or by setting it to null, the response will not include generation. [Learn more](https://docs.vectara.com/docs/learn/grounded-generation/configure-query-summarization)
* Specify Vectara's RAG-focused LLM (Mockingbird) for the `generation_preset_name`. [Learn more](https://docs.vectara.com/docs/learn/mockingbird-llm)
* Use advanced summarization options that utilize detailed summarization parameters such as `max_response_characters`, `temperature`, and `frequency_penalty` for generating precise and relevant summaries. [Learn more](https://docs.vectara.com/docs/search-and-retrieval#advanced-summarization-customization-options)
* Customize citation formats in summaries using the `citations` object to include numeric, HTML, or Markdown links. [Learn more](https://docs.vectara.com/docs/search-and-retrieval#citations)
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
from vectara import Vectara, SearchCorporaParameters, KeyedSearchCorpus, ContextConfiguration, SearchReranker_CustomerReranker, GenerationParameters
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.queries.query_stream(
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
        reranker=SearchReranker_CustomerReranker(
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

**stream_response:** `typing.Literal` — Indicates whether the response should be streamed or not.
    
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

<details><summary><code>client.queries.<a href="src/vectara/queries/client.py">query</a>(...) -> QueryQueriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform a multipurpose query to retrieve relevant information from one or more corpora and generate a response using Retrieval Augmented Generation (RAG). Similar to the [advanced corpora search](https://docs.vectara.com/docs/rest-api/query-corpus).

* Specify the unique `corpus_key` identifying the corpus to query. The `corpus_key` is created in the Vectara Console or the [Create Corpus API](https://docs.vectara.com/docs/rest-api/create-corpus), and the corpus key is part of that process. When creating a new corpus, you have the option to assign a custom `corpus_key` following your preferred naming convention. This key serves as a unique identifier for the corpus, allowing it to be referenced in search requests.
* Customize your search by specifying the query text (`query`), pagination details (`offset` and `limit`), and metadata filters (`metadata_filter`) to tailor your search results.
* Leverage advanced search capabilities like reranking (`reranker`) and opt-in Retrieval Augmented Generation (RAG) (`generation`) for enhanced query performance. Generation is opt-in by setting the `generation` property. By excluding the property or by setting it to null, the response will not include generation. [Learn more](https://docs.vectara.com/docs/learn/grounded-generation/configure-query-summarization)
* Specify Vectara's RAG-focused LLM (Mockingbird) for the `generation_preset_name`. [Learn more](https://docs.vectara.com/docs/learn/mockingbird-llm)
* Use advanced summarization options that utilize detailed summarization parameters such as `max_response_characters`, `temperature`, and `frequency_penalty` for generating precise and relevant summaries. [Learn more](https://docs.vectara.com/docs/search-and-retrieval#advanced-summarization-customization-options)
* Customize citation formats in summaries using the `citations` object to include numeric, HTML, or Markdown links. [Learn more](https://docs.vectara.com/docs/search-and-retrieval#citations)
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
from vectara import Vectara, SearchCorporaParameters, KeyedSearchCorpus, ContextConfiguration, SearchReranker_CustomerReranker, GenerationParameters
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.queries.query_stream(
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
        reranker=SearchReranker_CustomerReranker(
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

**stream_response:** `typing.Literal` — Indicates whether the response should be streamed or not.
    
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
<details><summary><code>client.query_history.<a href="src/vectara/query_history/client.py">get</a>(...) -> QueryHistory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Get Query History API allows you to retrieve detailed history about a specific query that was made against a corpus. The response includes detailed information about the query, such as latency, the time it was executed, and the various stages in the query pipeline.

You specify the `query_id` and the response includes the `id` of the query, the `query` object, the `chat_id`, the time information about the query, and the `spans` object.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.query_history.<a href="src/vectara/query_history/client.py">list</a>(...) -> ListQueryHistoriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The List Query Histories API allows you to retrieve, update, and manage query history for a specific corpus. This API is particularly useful for tracking query performance, debugging individual queries, and retrieving detailed information such as the call stack of a query execution.

You can specify the `corpus_key`, `chat_id`, and the `limit` which is the maximum number of historical queries to list.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.query_history.list(
    corpus_key="my_corpus_key",
    chat_id="cht_123456789",
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

**corpus_key:** `typing.Optional[str]` — Specifies the `corpus_key` used in the query.
    
</dd>
</dl>

<dl>
<dd>

**started_after:** `typing.Optional[datetime.datetime]` — Queries that started after a particular ISO date-time.
    
</dd>
</dl>

<dl>
<dd>

**started_before:** `typing.Optional[datetime.datetime]` — Queries that started before a particular ISO date-time.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Chats
<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">list</a>(...) -> ListChatsResponse</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.chats.list()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">create_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
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
from vectara import Vectara, SearchCorporaParameters, KeyedSearchCorpus, ContextConfiguration, SearchReranker_CustomerReranker, GenerationParameters, CitationParameters, ChatParameters
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.chats.create_stream(
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
        reranker=SearchReranker_CustomerReranker(
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

**stream_response:** `typing.Literal` — Indicates whether the response should be streamed or not.
    
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

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">create</a>(...) -> CreateChatsResponse</code></summary>
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
from vectara import Vectara, SearchCorporaParameters, KeyedSearchCorpus, ContextConfiguration, SearchReranker_CustomerReranker, GenerationParameters, CitationParameters, ChatParameters
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.chats.create_stream(
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
        reranker=SearchReranker_CustomerReranker(
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

**stream_response:** `typing.Literal` — Indicates whether the response should be streamed or not.
    
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

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">get</a>(...) -> Chat</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">list_turns</a>(...) -> ListChatTurnsResponse</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">create_turns_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
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
from vectara import Vectara, SearchCorporaParameters, KeyedSearchCorpus
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.chats.create_turns_stream(
    chat_id="chat_id",
    query="What are the carbon reduction efforts by EU banks in 2023?",
    search=SearchCorporaParameters(
        corpora=[
            KeyedSearchCorpus(
                corpus_key="my-corpus",
            )
        ],
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

**stream_response:** `typing.Literal` — Indicates whether the response should be streamed or not.
    
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

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">create_turns</a>(...) -> CreateTurnsChatsResponse</code></summary>
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
from vectara import Vectara, SearchCorporaParameters, KeyedSearchCorpus
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.chats.create_turns_stream(
    chat_id="chat_id",
    query="What are the carbon reduction efforts by EU banks in 2023?",
    search=SearchCorporaParameters(
        corpora=[
            KeyedSearchCorpus(
                corpus_key="my-corpus",
            )
        ],
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

**stream_response:** `typing.Literal` — Indicates whether the response should be streamed or not.
    
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

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">get_turn</a>(...) -> Turn</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chats.<a href="src/vectara/chats/client.py">update_turn</a>(...) -> Turn</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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
<details><summary><code>client.llms.<a href="src/vectara/llms/client.py">list</a>(...) -> ListLlMsResponse</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.llms.list()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.llms.<a href="src/vectara/llms/client.py">create</a>(...) -> Llm</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Integrate external Large Language Models (LLMs) into Vectara for Retrieval Augmented Generation (RAG) and chat. Connect OpenAI API-compatible models from providers like Anthropic, Azure, Google, or custom-hosted endpoints. Once created, reference your custom LLM by name in query generation parameters.
- Connect external LLMs using OpenAI-compatible API format
- Configure multiple LLM providers for different use cases
- Override Vectara's built-in LLMs with your own models
- Use custom models for RAG, chat, and document summarization

**Example providers:**

### OpenAI

**Type:** `openai-compatible`
**Models:** GPT-4o, GPT-5
**Auth:** Bearer token

```json
{
  "type": "openai-compatible",
  "name": "my-gpt5",
  "model": "gpt-5",
  "uri": "https://api.openai.com/v1/chat/completions",
  "auth": {
    "type": "bearer",
    "token": "sk-..."
  }
}
```

### OpenAI Responses API

**Type**: openai-responses
**Models**: o1-preview, o1-mini, o3-mini (reasoning models)
**Auth**: Bearer token
**Note**: For reasoning models that don't support streaming

```json
{
  "type": "openai-responses",
  "name": "my-o1",
  "model": "o1-preview",
  "uri": "https://api.openai.com/v1/chat/completions",
  "auth": {
    "type": "bearer",
    "token": "sk-..."
  }
}
```

### Anthropic Claude

**Type:** `openai-compatible`
**Models:** claude-4-opus, claude-4-5-haiku, claude-4-5-sonnet
**Auth:** Bearer token with header

```json
{
  "type": "openai-compatible",
  "name": "my-claude",
  "model": "claude-sonnet-4-5-20250929",
  "uri": "https://api.anthropic.com/v1/messages",
  "auth": {
    "type": "bearer",
    "token": "sk-ant-..."
  },
  "headers": {
    "anthropic-version": "2023-06-01"
  }
}
```

### Azure OpenAI

**Type:** `openai-compatible`
**Models:** GPT-3.5, GPT-4 (Azure-deployed versions)
**Auth:** Custom header (api-key)

```json
{
  "type": "openai-compatible",
  "name": "my-azure-gpt4",
  "model": "gpt-4",
  "uri": "https://YOUR-RESOURCE.openai.azure.com/openai/deployments/YOUR-DEPLOYMENT/chat/completions?api-version=2024-02-15-preview",
  "auth": {
    "type": "header",
    "header": "api-key",
    "value": "your-azure-key"
  }
}
```

### Google Vertex AI (Gemini) — Service Account

**Type:** `vertex-ai`
**Models:** gemini-2.5-pro, gemini-2.5-flash
**Auth:** Service account

```json
{
  "type": "vertex-ai",
  "name": "my-gemini",
  "model": "gemini-2.5-flash",
  "uri": "https://us-central1-aiplatform.googleapis.com/v1/projects/YOUR-PROJECT/locations/us-central1",
  "auth": {
    "type": "service_account",
    "key_json": "{...service account JSON...}"
  }
}
```

### Google AI Studio (Gemini) — API Key

**Type:** `vertex-ai`
**Models:** gemini-2.5-pro, gemini-2.5-flash
**Auth:** API key

```json
{
  "type": "vertex-ai",
  "name": "my-gemini",
  "model": "gemini-2.5-flash",
  "uri": "https://generativelanguage.googleapis.com/v1beta",
  "auth": {
    "type": "api_key",
    "api_key": "your-google-api-key"
  }
}
```

The `uri` field is flexible — you can provide a base URI or a full URL copied from Google docs
(including model path and `:generateContent` suffix). The system normalizes it automatically.

### Custom OpenAI-Compatible

**Type:** `openai-compatible`
**Models:** Any self-hosted or custom LLM, such as OpenRouter.
**Auth:** Bearer or custom header

```json
{
  "type": "openai-compatible",
  "name": "my-custom-llm",
  "model": "llama-3-70b",
  "uri": "https://my-llm-endpoint.com/v1/chat/completions",
  "auth": {
    "type": "bearer",
    "token": "custom-token"
  }
}
```
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
from vectara import Vectara, CreateLlmRequest_OpenaiCompatible
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.llms.create(
    request=CreateLlmRequest_OpenaiCompatible(
        name="Claude 3.7 Sonnet",
        model="claude-3-7-sonnet-20250219",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.llms.<a href="src/vectara/llms/client.py">get</a>(...) -> Llm</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Get LLM API allows users to retrieve details about a specific Large Language Model (LLM) that has been configured within the Vectara platform. This API provides metadata about the LLM, including its name, description, model type, API endpoint, and authentication method.

Use this API to verify model configurations, confirm connectivity details, and ensure that the correct LLM is being utilized within their workflows.

## Authentication methods
The request requires authentication details, and you can provide them either as a Bearer token or custom header-based authentication.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

The Delete LLM API enables users to remove a previously configured custom Large Language Model (LLM) from their Vectara account. This functionality is essential for managing active LLM configurations and ensuring that only relevant models are available for use. Built-in LLMs cannot be deleted, ensuring that core system models remain accessible.

By providing an LLM identifier, users can permanently delete a model configuration, freeing up resources and maintaining an organized list of available LLMs.

If successful, the API responds with `HTTP 204 No Content` status, confirming the LLM deletion.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.llms.<a href="src/vectara/llms/client.py">update</a>(...) -> Llm</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing LLM's configuration. This endpoint allows partial updates - only provide fields you want to change. Only the name field is immutable.

The updated LLM will be tested before saving to ensure credentials are valid.

**Updatable fields:**
- `description` - LLM description
- `type` - LLM type (openai-compatible, vertex-ai, etc.)
- `model` - Model identifier
- `uri` - API endpoint
- `auth` - Authentication credentials (including service account key_json)
- `headers` - Additional HTTP headers (for openai-compatible and anthropic types)
- `enabled` - Whether the LLM is enabled
- `capabilities` - Model capabilities (image support, context limit, tool calling)

**Immutable fields:**
- `id` - System-generated identifier
- `name` - LLM name

Built-in LLMs (system-provided models) cannot be updated.
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
from vectara import Vectara, UpdateLlmRequest_OpenaiCompatible
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.llms.update(
    llm_id="llm_id",
    request=UpdateLlmRequest_OpenaiCompatible(),
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

**llm_id:** `str` — The ID of the LLM to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateLlmRequest` 
    
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
<details><summary><code>client.llm.<a href="src/vectara/llm/client.py">chat_completion</a>(...) -> CreateChatCompletionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Chat Completions API provides an OpenAI-compatible interface for generating model responses in multi-turn chat conversations. This API enables you to integrate our language models directly into applications designed to work with the OpenAI Chat Completions format, making it easy to leverage Vectara capabilities with minimal changes to existing tools or code.

Use this API to enable interactive chat experiences that support context-aware responses, streaming output, and token usage tracking.

The request includes a series of chat messages and optional parameters that control the behavior and structure of the model response. The request body must include the `messages` parameter, an array of message objects (role, content) representing the full conversation so far.

### Streaming responses

If the `stream` parameter is set to `true`, the response appears as a series of text/event-stream parts (also known as chunks). Each chunk includes a `delta` field showing the incremental message update.

### Example request

This example sends a simple chat conversation to the API, asking the assistant for the capital of France. The request includes a system prompt, a user message, and a temperature setting for response variability.
```json
{
  "model": "chat-model-001","messages": [{ "role": "system", "content": "You are a helpful assistant." },
  { "role": "user", "content": "What is the capital of France?" }
],
"temperature": 0.7,
"stream": false
}
```

### Example response
The response includes a generated reply from the assistant, along with token usage statistics. In this example, the model returns a direct answer to a user question.
```json
{
"id": "chatcmpl-abc123",}
"object": "chat.completion",
"created": 1712454830,
"model": "chat-model-001",
"choices": [
  {
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "The capital of France is Paris."
  },
    "finish_reason": "stop"
  }
],
"usage": {
  "prompt_tokens": 21,
  "completion_tokens": 9,
  "total_tokens": 30
  } 
} 
```
If the input summary is accurate, the `corrected_summary` matches the `original_summary`.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.llm.chat_completion(
    model="model",
    messages=[],
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

**messages:** `typing.List[ChatCompletionRequestMessage]` — An ordered array of messages that represent the full context of the conversation to date. Each message includes a `role` and `content`.
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` — Optional. When set to `true`, the API streams partial message deltas as they become available, similar to ChatGPT's streaming mode.
    
</dd>
</dl>

<dl>
<dd>

**response_format:** `typing.Optional[ResponseFormat]` — Specifies the output format for the model response.
    
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
<details><summary><code>client.generation_presets.<a href="src/vectara/generation_presets/client.py">list</a>(...) -> ListGenerationPresetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Organizations often struggle to fine-tune query responses and maintain consistency across different use cases. Vectara creates and maintains predefined generation presets for our users which provides a flexible and powerful way to utilize generation parameters. Each preset includes a complete Velocity template for the prompt along with other generation parameters. Presets are typically associated with a single LLM.

The List Generation Presets API lets you view the generation presets used for [query](/docs/rest-api/queries) requests. Generation presets group several properties that configure generation for a request. These presets provide more flexibility in how generation parameters are configured, enabling more fine-tuned control over query responses.

This includes the `prompt_template`, the Large Language Model (LLM), and other generation settings like `max_tokens` and `temperature`. Users specify a generation preset in their query or chat requests using the `generation_preset_name` field.

## Generation presets object

The `generation_presets` object contains the `name`, `description`, `llm_name`, `prompt_template`, and other fields make up the preset.

If your account has access to a preset, then `enabled` is set to `true`. A preset can also be set as a `default`.\n\n### Example generation presets response\n\n```json\n{\n  \"generation_presets\": [\n    {\n      \"name\": \"vectara-summary-ext-24-05-med-omni\",\n      \"description\": \"Generate summary with controllable citations, Uses GPT-4o with 2,048 max tokens\",\n      \"llm_name\": \"gpt-4o\",\n      \"prompt_template\": \"[\\n    {\\\"role\\\": \\\"system\\\", \\\"content\\\": \\\"Follow these detailed step-by-step\",\n      \"max_used_search_results\": 25,\n      \"max_tokens\": 2048,\n      \"temperature\": 0,\n      \"frequency_penalty\": 0,\n      \"presence_penalty\": 0,\n      \"enabled\": true,\n      \"default\": false\n    },\n    // More presets appear here\n}\n```\n"
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.generation_presets.list(
    llm_name="mockingbird-2.0",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.generation_presets.<a href="src/vectara/generation_presets/client.py">create</a>(...) -> GenerationPreset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a custom generation preset for use in query and chat requests. A generation preset bundles a prompt template, an LLM, and model parameters into a reusable configuration.

The created preset can be referenced by name using the `generation_preset_name` field in query or chat requests.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.generation_presets.create()

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

**request:** `CreateGenerationPresetRequest` 
    
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

<details><summary><code>client.generation_presets.<a href="src/vectara/generation_presets/client.py">replace</a>(...) -> GenerationPreset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace an existing custom generation preset. This performs a full replacement of the preset configuration.
The preset must have been created by the customer (platform presets cannot be replaced).
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.generation_presets.replace(
    generation_preset_id="generation_preset_id",
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

**generation_preset_id:** `str` — The ID of the generation preset to replace.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateGenerationPresetRequest` 
    
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

<details><summary><code>client.generation_presets.<a href="src/vectara/generation_presets/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an existing custom generation preset.
The preset must have been created by the customer (platform presets cannot be deleted).
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.generation_presets.delete(
    generation_preset_id="generation_preset_id",
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

**generation_preset_id:** `str` — The ID of the generation preset to delete.
    
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
<details><summary><code>client.factual_consistency.<a href="src/vectara/factual_consistency/client.py">evaluate</a>(...) -> EvaluateFactualConsistencyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Evaluate the factual consistency of a generated text (like a summary) against source documents. This determines how accurately the generated text reflects the information in the source documents, helping identify potential hallucinations or misrepresentations.

Use this API to programmatically validate generated content against trusted source materials—an essential capability for applications in high-integrity environments such as legal, healthcare, scientific publishing, and enterprise knowledge systems.

The request body must include the following parameters:
* `model_parameters:` Optionally specifies the evaluation model to use. Default is `hhem_v2.2`.
* `generated_text`: The output text you want to evaluate, such as a model-generated summary, answer, or response.
* `source_texts`: An array of source documents or passages used to verify the accuracy of the generated text.
* `language`: The ISO 639-3 code representing the language of the provided texts (`eng` for English, `fra` for French).

### Example request

This example evaluates whether a generated statement about the Eiffel Tower is factually accurate based on two reference documents.

```json
{
  "generated_text": "The Eiffel Tower is located in Berlin.",
  "source_texts": [
    "The Eiffel Tower is a famous landmark located in Paris, France.",
    "It was built in 1889 and remains one of the most visited monuments in the world."
  ],
  "language": "eng"
}
```
### Example response

The response includes a factual consistency score and probability estimates.

```json
{
  "score": 0.23,
  "p_consistent": 0.12,
  "p_inconsistent": 0.88
}
```
* `score`: A normalized value between `0.0` and `1.0` that reflects the overall factual alignment between the generated text and the source texts. Higher scores indicate stronger consistency.
* `p_consistent`: The estimated probability that the generated text is factually consistent with the sources.
* `p_inconsistent`: The estimated probability that the generated text contains factual inaccuracies relative to the source documents.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.factual_consistency.evaluate(
    generated_text="generated_text",
    source_texts=[
        "source_texts"
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

**generated_text:** `str` — The generated text (e.g., summary or answer) to evaluate for factual consistency.
    
</dd>
</dl>

<dl>
<dd>

**source_texts:** `typing.List[str]` — The source documents or text snippets against which to evaluate factual consistency.
    
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
<details><summary><code>client.encoders.<a href="src/vectara/encoders/client.py">list</a>(...) -> ListEncodersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The List Encoders API retrieves a list of available encoders used for embedding documents and queries.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.encoders.list(
    filter="vectara.*",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encoders.<a href="src/vectara/encoders/client.py">create</a>(...) -> Encoder</code></summary>
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
from vectara import Vectara, CreateEncoderRequest_OpenaiCompatible
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.encoders.create(
    request=CreateEncoderRequest_OpenaiCompatible(
        name="openai-text-encoder",
        description="description",
        uri="https://api.openai.com/v1/embeddings",
        model="text-embedding-ada-002",
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

**request:** `CreateEncoderRequest` 
    
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
<details><summary><code>client.rerankers.<a href="src/vectara/rerankers/client.py">list</a>(...) -> ListRerankersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The List Rerankers API retrieves a list of available rerankers used to improve the ranking and ordering of search results.

For more information about the available rerankers, see [Reranking overview](https://docs.vectara.com/docs/search-and-retrieval/rerankers/reranking-overview).
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.rerankers.list(
    filter="vectara.*",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Table Extractors
<details><summary><code>client.table_extractors.<a href="src/vectara/table_extractors/client.py">list</a>() -> ListTableExtractorsResponse</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Hallucination Correctors
<details><summary><code>client.hallucination_correctors.<a href="src/vectara/hallucination_correctors/client.py">list</a>(...) -> ListHallucinationCorrectorsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The List Hallucination Correctors API enables users to list available hallucination correctors used for detecting and correcting hallucinations in AI-generated content. Vectara provides these models as part of its broader hallucination evaluation framework, and the Hallucination Correctors endpoint uses these models to propose factual corrections to summaries and other generative outputs.

Use this API to inspect available correctors, filter results, and determine which hallucination corrector to reference in downstream workflows or evaluation pipelines.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.hallucination_correctors.list()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hallucination_correctors.<a href="src/vectara/hallucination_correctors/client.py">hallucination_correction</a>(...) -> HallucinationCorrectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Hallucination Correctors API enables users to automatically detect and correct factual inaccuracies, commonly referred to as hallucinations, in generated summaries or responses. By comparing a user-provided summary against one or more source documents, the API returns a corrected version of the summary with minimal necessary edits.

Use this API to validate and improve the factual accuracy of summaries generated by LLMs in Retrieval Augmented Generation (RAG) pipelines, ensuring that the output remains grounded in trusted source content. If HCM does not detect hallucination, it preserves the original summary.

The response corrects the original summary. If the input summary is accurate, the `corrected_summary` matches the `original_summary`.

## Interpreting empty corrections

In some cases, the `corrected_text` field in the response may be an empty string. This indicates VHC determined that the entire input text was hallucinated, and VHC recommends removing it completely.

This outcome is valid and typically occurs when none of the content in the `generated_text` is supported by the provided source documents or query. The response still includes an explanation of why VHC removed the text.
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
from vectara import Vectara, HcmSourceDocument
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**documents:** `typing.List[HcmSourceDocument]` — The source documents that were used to generate the text.
    
</dd>
</dl>

<dl>
<dd>

**model_name:** `str` — The name of the LLM model to use for hallucination correction.
    
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
<details><summary><code>client.jobs.<a href="src/vectara/jobs/client.py">list</a>(...) -> ListJobsResponse</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.jobs.list(
    corpus_key=[
        "my-corpus"
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

**corpus_key:** `typing.Optional[typing.Union[CorpusKey, typing.Sequence[CorpusKey]]]` — The unique key identifying the corpus with the job.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[datetime.datetime]` — Filter by jobs created after a particular date-time.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/vectara/jobs/client.py">get</a>(...) -> Job</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a job by a specific `job_id`. Jobs are background processes like replacing the filterable metadata attributes.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/vectara/users/client.py">list</a>(...) -> ListUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The List Users API lets you list all users on your team and also their corpus access and customer-level authorizations.

Other activities such as adding, deleting, enabling, disabling, resetting passwords, and editing user roles are performed by the [Update User](/docs/rest-api/update-user) endpoint.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.users.list(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/vectara/users/client.py">create</a>(...) -> CreateUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a user for the current customer account. For example, a company wants to onboard new team members efficiently and this endpoint lets you streamline the process by adding new users programmatically, assigning appropriate roles, and setting up access permissions.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**api_roles:** `typing.Optional[typing.List[ApiRole]]` — The customer-level role names assigned to the user.
    
</dd>
</dl>

<dl>
<dd>

**corpus_roles:** `typing.Optional[typing.List[CorpusRole]]` — Corpus-specific role assignments for the user.
    
</dd>
</dl>

<dl>
<dd>

**agent_roles:** `typing.Optional[typing.List[AgentRole]]` — Agent-specific role assignments for the user.
    
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

<details><summary><code>client.users.<a href="src/vectara/users/client.py">get</a>(...) -> User</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/vectara/users/client.py">update</a>(...) -> User</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**enabled:** `typing.Optional[bool]` — Indicates whether to enable or disable the user.
    
</dd>
</dl>

<dl>
<dd>

**api_roles:** `typing.Optional[typing.List[ApiRole]]` — The new customer-level role names of the user.
    
</dd>
</dl>

<dl>
<dd>

**corpus_roles:** `typing.Optional[typing.List[CorpusRole]]` — New corpus-specific role assignments for the user.
    
</dd>
</dl>

<dl>
<dd>

**agent_roles:** `typing.Optional[typing.List[AgentRole]]` — New agent-specific role assignments for the user.
    
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

<details><summary><code>client.users.<a href="src/vectara/users/client.py">reset_password</a>(...) -> ResetPasswordUsersResponse</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## API Keys
<details><summary><code>client.api_keys.<a href="src/vectara/api_keys/client.py">list</a>(...) -> ListApiKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The List API Keys API lists all existing API keys for a customer ID. It also shows what corpora are accessed by these keys and with what permissions. This capability can provide insights into key usage and status and help you manage the lifecycle and security of your API keys.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.api_keys.list(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/vectara/api_keys/client.py">create</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Create API Key API lets you create new API keys, which you can bind to one or multiple corpora. You can also decide whether to designate each key for specific access like personal API keys, only querying (read-only) or both querying and indexing (read-write).

This capability is useful in scenarios where you have applications that require different levels of access to corpora data. For example, you might create a read-only API key for an application that only needs to query data.

:::note
For more information about the different types of API keys, see [API Key Management](/docs/deploy-and-scale/authentication/api-key-management).
:::
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.api_keys.create(
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

**name:** `str` — The human-readable name of the API key.
    
</dd>
</dl>

<dl>
<dd>

**api_roles:** `typing.Optional[typing.List[ApiRole]]` — Customer-level roles for this API key.
    
</dd>
</dl>

<dl>
<dd>

**api_key_role:** `typing.Optional[ApiKeyRole]` — Deprecated: Use api_roles instead. Legacy role of the API key.
    
</dd>
</dl>

<dl>
<dd>

**corpus_keys:** `typing.Optional[typing.List[CorpusKey]]` — Deprecated: Use corpus_roles instead. Corpora this API key has roles on.
    
</dd>
</dl>

<dl>
<dd>

**corpus_roles:** `typing.Optional[typing.List[CorpusRole]]` — Corpus-specific role assignments for this API key.
    
</dd>
</dl>

<dl>
<dd>

**agent_roles:** `typing.Optional[typing.List[AgentRole]]` — Agent-specific role assignments for this API key.
    
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

<details><summary><code>client.api_keys.<a href="src/vectara/api_keys/client.py">get</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Get API Key API lists all existing API keys for a customer ID. It also shows what corpora are accessed by these keys and with what permissions.

This capability can provide insights into key usage and status and help you manage the lifecycle and security of your API keys.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

The Delete API Key API lets you delete one or more existing API keys. 
This capability is useful for managing the lifecycle and security of 
API keys such as when they are no longer needed or when a key is compromised.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/vectara/api_keys/client.py">update</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Update API Key API lets you enable or disable specific API keys. You can use this endpoint to temporarily disable access without deleting the key.

This capability is useful for scenarios like maintenance windows, or when your team no longer requires access to a specific corpus.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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
<details><summary><code>client.app_clients.<a href="src/vectara/app_clients/client.py">list</a>(...) -> ListAppClientsResponse</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.app_clients.list()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_clients.<a href="src/vectara/app_clients/client.py">create</a>(...) -> AppClient</code></summary>
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
from vectara import Vectara, CreateAppClientRequest_ClientCredentials
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.app_clients.create(
    request=CreateAppClientRequest_ClientCredentials(
        name="name",
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

**request:** `CreateAppClientRequest` 
    
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

<details><summary><code>client.app_clients.<a href="src/vectara/app_clients/client.py">get</a>(...) -> AppClient</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_clients.<a href="src/vectara/app_clients/client.py">update</a>(...) -> AppClient</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**description:** `typing.Optional[str]` — The new App Client description.
    
</dd>
</dl>

<dl>
<dd>

**api_roles:** `typing.Optional[typing.List[ApiRole]]` — The new roles attached to the App Client. These roles will replace the current roles.
    
</dd>
</dl>

<dl>
<dd>

**corpus_roles:** `typing.Optional[typing.List[CorpusRole]]` — The new corpus role assignments. These will replace the current corpus roles.
    
</dd>
</dl>

<dl>
<dd>

**agent_roles:** `typing.Optional[typing.List[AgentRole]]` — The new agent role assignments. These will replace the current agent roles.
    
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
<details><summary><code>client.auth.<a href="src/vectara/auth/client.py">get_token</a>(...) -> GetTokenResponse</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**grant_type:** `typing.Literal` 
    
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
<details><summary><code>client.tool_servers.<a href="src/vectara/tool_servers/client.py">list</a>(...) -> ListToolServersResponse</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.tool_servers.list(
    filter="rag.*",
    enabled=True,
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

**filter:** `typing.Optional[str]` — A regular expression against tool server names and descriptions to filter the results.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListToolServersRequestType]` — Filter tool servers by type.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tool_servers.<a href="src/vectara/tool_servers/client.py">create</a>(...) -> ToolServer</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.tool_servers.create(
    name="RAG Search Server",
    type="mcp",
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

**type:** `ToolServerType` 
    
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arbitrary metadata associated with the tool server.
    
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

<details><summary><code>client.tool_servers.<a href="src/vectara/tool_servers/client.py">get</a>(...) -> ToolServer</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tool_servers.<a href="src/vectara/tool_servers/client.py">update</a>(...) -> ToolServer</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arbitrary metadata associated with the tool server.
    
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tools
<details><summary><code>client.tools.<a href="src/vectara/tools/client.py">list</a>(...) -> ListToolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all tools available to the authenticated user, with optional filtering and pagination. Tools represent capabilities that agents can invoke during conversation, including built-in system tools and user-defined Lambda tools. Use filters to locate tools by name, type, status, or tool server.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.tools.list(
    filter="rag.*",
    enabled=True,
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

**filter:** `typing.Optional[str]` — A regular expression against tool names and descriptions to filter the results.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListToolsRequestType]` — Filter tools by type.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Filter tools by enabled status.
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter tools by category. Pass one or more category values to include only those categories. When omitted, tools in the "experimental" category are excluded by default. To include experimental tools, explicitly pass `category=experimental`.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/vectara/tools/client.py">create</a>(...) -> Tool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new tool that agents can use during conversation. Tools give agents capabilities to interact with external systems, process data, query corpora, or run custom logic. Agents select and invoke tools dynamically based on their instructions and the conversational context.

Vectara provides several built-in tools, but you can also create your own. This endpoint currently supports creating **Lambda tools**, which run user-defined Python functions in a secure sandbox.

Each tool is defined by:
- A unique tool ID
- A description of its purpose
- An input schema describing accepted parameters
- Optional metadata
- Enabled/disabled runtime availability

 ## Artifact-based tools
Some built-in tools work with artifacts stored in a session:
- **Document conversion tool**: Converts file artifacts (PDF, Word, PowerPoint, images with OCR support) to markdown and produces new artifacts containing the extracted content.

These built-in tools operate on artifact references rather than file content, supporting multi-step workflows where agents process or index user-uploaded documents.
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
from vectara import Vectara, CreateToolRequest_Lambda
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.tools.create(
    request=CreateToolRequest_Lambda(
        name="calculate_customer_score",
        title="Customer Score Calculator",
        description="Calculate a customer score based on order history and revenue. Returns a score between 0-100.",
        code="def process(order_count: int, total_revenue: float, days_active: int = 1) -> dict:\n    score = (order_count * 10 + total_revenue * 0.1) / days_active\n    return {\'score\': round(score, 2)}\n",
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

**request:** `CreateToolRequest` 
    
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

<details><summary><code>client.tools.<a href="src/vectara/tools/client.py">test_without_creation</a>(...) -> TestLambdaToolResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Test a Lambda tool without creating it first. This endpoint allows you to validate code, discover schemas, and test execution before committing to tool creation.

Use this to:
- Validate Python code syntax and security constraints
- Discover input/output schemas from type annotations
- Test execution with sample input
- Verify schema compatibility

The function is executed in the same secure sandbox environment as production tools.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.tools.test_without_creation(
    code="def process(order_count: int, total_revenue: float) -> dict:\n    score = order_count * 10 + total_revenue * 0.1\n    return {\'score\': round(score, 2)}\n",
    test_input={
        "order_count": 10,
        "total_revenue": 500
    },
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

**code:** `str` 

The Python 3.12 code for the function. Must define a `process()` entry point.
Object parameters must use `TypedDict`; bare `dict` and `Dict[K, V]` parameters are rejected.
See the `code` field on `CreateLambdaToolRequest` for full details and examples.
    
</dd>
</dl>

<dl>
<dd>

**test_input:** `typing.Dict[str, typing.Any]` — The input parameters to test the function with. Will be validated against the discovered input schema.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[TestLambdaToolRequestLanguage]` — The programming language. Currently only 'python' (Python 3.12) is supported.
    
</dd>
</dl>

<dl>
<dd>

**execution_configuration:** `typing.Optional[ExecutionConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**timeout_seconds:** `typing.Optional[int]` — Maximum execution time in seconds for this test. Overrides execution_configuration if specified.
    
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

<details><summary><code>client.tools.<a href="src/vectara/tools/client.py">get</a>(...) -> Tool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the full details of a specific tool, including its description, input schema, metadata, and capabilities. Tools may represent structured search functions, document-processing workflows, or user-defined Lambda functions. Some tools work with artifacts stored in a session, while others operate on structured inputs defined by their JSON schema.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

Permanently delete a tool and its configuration. This action cannot be undone. Agents attempting to use a deleted tool will fail, so ensure that agent configurations are updated before removing a tool.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/vectara/tools/client.py">update</a>(...) -> Tool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing tool’s configuration, including its metadata, enabled status, or other properties. Updating a tool modifies how agents can invoke it during conversation.
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
from vectara import Vectara, UpdateToolRequest_Mcp
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.tools.update(
    tool_id="tol_rag_search",
    request=UpdateToolRequest_Mcp(),
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/vectara/tools/client.py">test</a>(...) -> TestToolResponse</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.tools.test(
    tool_id="tol_python_function_123",
    input={
        "number": 42,
        "text": "Hello, world!"
    },
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

**input:** `typing.Dict[str, typing.Any]` — The input parameters to pass to the function. Must match the tool's input schema.
    
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
<details><summary><code>client.instructions.<a href="src/vectara/instructions/client.py">list</a>(...) -> ListInstructionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all instructions available to the authenticated user, with optional filtering and pagination. This endpoint returns high-level information about each instruction, including name, status, and version details.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.instructions.list(
    filter="support.*",
    enabled=True,
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

**filter:** `typing.Optional[str]` — A regular expression against instruction names and descriptions to filter the results.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListInstructionsRequestType]` — Filter instructions by type.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.instructions.<a href="src/vectara/instructions/client.py">create</a>(...) -> Instruction</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new instruction that defines how an agent should behave, reason, and respond. Instructions act as system-level guidelines that shape the agent's tone, style, constraints, and tool usage.

Instructions support dynamic content using the Apache Velocity templating engine. Velocity variables allow instructions to reference runtime context:

- `\$\tools`: The list of tools available to the agent.
- `\$\{session.metadata.field}`: Session-level metadata (user context, permissions, preferences).
- `\$\{agent.metadata.field}`: Agent-level metadata (configuration or environment).

Example tool iteration:
```velocity
You have access to the following tools:
\#foreach(\$\tool in $tools)
  - \$\{tool.name}: \$\{tool.description}
#end
```
:::tip Tips for effective instruction design
Instructions are one of the most critical parts of an agent's design. Best practices vary by model, but at a minimum you should provide clear guidance on what tools are available, what output format is desired, and what steps to follow for common queries. Instructions typically need to be iterated on and tested over time.

For guidance on writing effective instructions, see:
- [Claude Prompt Engineering](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
:::

Metadata can personalize behavior at runtime. For example:

```velocity
Hello ${session.metadata.user_name}, how can I help with ${session.metadata.department} today?
```

**Example request:**
```json
{
  "name": "Customer Support Tone and Style Guide",
  "description": "Defines tone and behavior for customer interactions.",
  "template": "You are a customer support agent for the ${session.metadata.department} department.",
  "enabled": true,
  "metadata": {
    "owner": "customer-support-team",
    "version": "1.0.0"
  }
}
```
A successful response returns the full instruction definition, including its unique ID, version, and timestamps.
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
from vectara import Vectara, CreateInstructionRequest_Initial
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.instructions.create(
    request=CreateInstructionRequest_Initial(
        name="Customer Support Initial Instruction",
        template="You are an expert customer support agent for $agent.name. Available tools: #foreach($tool in $tools)${tool.name}#if($foreach.hasNext), #end#end",
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

**request:** `CreateInstructionRequest` 
    
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

<details><summary><code>client.instructions.<a href="src/vectara/instructions/client.py">get</a>(...) -> Instruction</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the full definition of a specific instruction, including its template, metadata, enabled status, and version. Instruction templates may contain Velocity expressions that reference tools and metadata. If no version is specified, the latest version is returned.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

Permanently delete an instruction and all its associated configuration.

:::warning
This action cannot be undone. Agents currently using this instruction may fail or behave unexpectedly. Update agents to use different instructions before deleting.
:::
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.instructions.<a href="src/vectara/instructions/client.py">update</a>(...) -> Instruction</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing instruction's template, metadata, and configuration. Updated templates may include Velocity variables such as `$tools` or metadata references. Each update creates a new version, allowing agents to continue using existing versions until explicitly changed.

::info Version Management
Agents referencing a specific version continue to use it until updated. Agents without a pinned version always use the latest.
:::

## Disable an instruction

This endpoint can also be used to disable an instruction without deleting it.

:::warning
Disabling an instruction prevents it from being added to new agents, but agents already using it continue to operate normally.
:::
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
from vectara import Vectara, UpdateInstructionRequest_Initial
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.instructions.update(
    instruction_id="ins_customer_support_init",
    request=UpdateInstructionRequest_Initial(),
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

**request:** `UpdateInstructionRequest` 
    
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

<details><summary><code>client.instructions.<a href="src/vectara/instructions/client.py">test</a>(...) -> TestInstructionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Test an instruction template using supplied context and available tools. This endpoint evaluates Velocity expressions such as `$tools`, `${session.metadata.field}`, or `${agent.metadata.field}`, and returns the fully rendered template output. Use this operation to validate formatting, logic, or metadata-dependent behavior before deploying instructions to agents.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**context:** `typing.Optional[typing.Dict[str, typing.Any]]` 

Context data to use when rendering the instruction template. This will be merged into `$session.metadata` for template access.

Example: If you provide `{"currentDate": "2024-01-15"}`, you can access it in the template as `$session.metadata.currentDate`.
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[Tool]]` — List of tools to include in the instruction context for testing.
    
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents
<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">list</a>(...) -> ListAgentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The List Agents API enables you to retrieve a paginated list of all agents available to the authenticated user. This is useful for managing and monitoring agent deployments across use cases and environments.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agents.list(
    filter="support.*",
    enabled=True,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">create</a>(...) -> Agent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new agent. An agent is compromised as 3 main things of functionality:
  1. The **instructions** an agent follows. Known as a system in prompt in other platforms.
  2. The **steps** an agent follows when receiving an input.
  3. The **tools** an agent can use to resolve those steps and instructions.

Instructions are tied to each step, and should be precisely crafted so that the agent can perform the desired actions when given an input. 

:::tip Creating more precise instructions
Be specific to exactly what you want the agent to do. For emphasis, use CAPS if you want the agent to follow a specific format. Negative prompts also help with precision such as saying **DO NOT DO THIS**.
:::

To use an agent, create a new session (called thread or chat in other platforms), and send new inputs to the agent to get responses.

:::note
Only a single step is supported with no follow up steps. So the `first_step` will be only the only step. We will add multiple steps and step types to execute complex workflows, but many agents can work well with a single step.
:::

## LLM configuration

Agents use LLMs for reasoning and response generation. You can configure the following:
- **Model**: Choose from available models like GPT-4o.
- **Parameters**: Adjust temperature, max tokens, and other model-specific settings.
- **Cost optimization**: Balance performance with token usage.
- **Retry configuration**: Configure automatic retry behavior for transient failures.

## Using retries to improve user experience

When agents interact with LLMs, transient failures like network interruptions can disrupt communication between the agent and the LLM. You can configure your agent to resume disrupted communication to ensure a smooth user experience.
- `max_retries`: After an error, the agent will retry its request to the LLM this many times.
- `initial_backoff_ms`: This is how many milliseconds the agent will wait before retrying, to give the cause of the error time to resolve.
- `backoff_factor`: Every time the agent retries, it can multiply the last retry delay by this number, increasing the wait between retries. This is like giving a toddler a longer and longer timeout if it continues to misbehave.
- `max_backoff_ms`: The maximum time you want the agent to wait between retries, so the backoff_factor does not create an unreasonably long delay for your users.
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
from vectara import Vectara, AgentToolConfiguration_CorporaSearch, AgentCorporaSearchQueryConfiguration, AgentModel
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agents.create(
    name="Customer Support Agent",
    tool_configurations={
        "customer_search": AgentToolConfiguration_CorporaSearch(
            query_configuration=AgentCorporaSearchQueryConfiguration(),
        )
    },
    model=AgentModel(
        name="gpt-4",
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

**request:** `CreateAgentRequest` 
    
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

<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">get</a>(...) -> Agent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Get Agent API enables you to retrieve the complete configuration and operational details of a specific AI agent, providing comprehensive visibility into agent capabilities, tool integrations, behavioral instructions, and metadata.

Use this API to inspect agent configurations before creating sessions, troubleshoot agent behavior issues, clone agent configurations for new deployments, and maintain documentation of agent capabilities across your enterprise AI infrastructure.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">replace</a>(...) -> Agent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Replace Agent API enables you to completely replace an existing agent configuration, including its corpora, tools, and generation presets. This endpoint performs a full replacement of the agent definition, unlike the Update Agent API which only modifies specified fields.
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
from vectara import Vectara, AgentToolConfiguration_CorporaSearch, AgentCorporaSearchQueryConfiguration, AgentModel
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agents.replace(
    agent_key="customer_support",
    name="Customer Support Agent",
    tool_configurations={
        "customer_search": AgentToolConfiguration_CorporaSearch(
            query_configuration=AgentCorporaSearchQueryConfiguration(),
        )
    },
    model=AgentModel(
        name="gpt-4",
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

**request:** `CreateAgentRequest` 
    
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

The Delete Agent API enables you to permanently remove an AI agent and its configuration from the Vectara platform, supporting agent lifecycle management and resource cleanup in enterprise environments.

Use this API for decommissioning outdated agents, cleaning up development and testing environments, removing agents that are no longer needed, and maintaining organized agent inventories as your AI deployments evolve. The permanent nature of deletion makes this API critical for environments where data governance and resource management are essential.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">update</a>(...) -> Agent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Update Agent API enables you to modify an existing agent configuration, including tool assignments, behavioral instructions, model parameters, and operational metadata.

Use this API to evolve agent capabilities over time, adding new tools as they become available, refining behavioral instructions based on user feedback, adjusting model parameters for optimal performance, and updating metadata for better organization across your agent ecosystem.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**name:** `typing.Optional[AgentName]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A detailed description of the agent's purpose and capabilities. Set to null to clear.
    
</dd>
</dl>

<dl>
<dd>

**tool_configurations:** `typing.Optional[typing.Dict[str, typing.Optional[AgentToolConfiguration]]]` 

A map of tool configurations available to the agent. Set to null to clear all tools.
Individual map values set to null will delete that tool configuration.
    
</dd>
</dl>

<dl>
<dd>

**skills:** `typing.Optional[typing.Dict[str, typing.Optional[AgentSkill]]]` 

A map of skills available to the agent. Set to null to clear all skills.
Individual map values set to null will delete that skill.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[AgentModel]` 
    
</dd>
</dl>

<dl>
<dd>

**first_step:** `typing.Optional[UpdateFirstAgentStep]` 

Deprecated: prefer updating steps directly via the steps map.
Partial update to the current first step. Can be combined with first_step_name
only if first_step_name equals first_step.name.
    
</dd>
</dl>

<dl>
<dd>

**first_step_name:** `typing.Optional[str]` 

Reassign the entry point to an existing step by name. This is the preferred way
to change the entry point. The named step must exist in the steps map.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arbitrary metadata associated with the agent. Set to null to clear.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the agent is enabled. Set to null to reset to default (true).
    
</dd>
</dl>

<dl>
<dd>

**compaction:** `typing.Optional[CompactionConfig]` — Configuration for automatic context compaction. Set to null to clear.
    
</dd>
</dl>

<dl>
<dd>

**tool_output_offloading:** `typing.Optional[ToolOutputOffloadingConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**steps:** `typing.Optional[typing.Dict[str, typing.Optional[UpdateAgentStep]]]` 

A map of additional named steps keyed by step name for partial update.
Only provided keys are modified; missing keys are preserved.
Set a key's value to null to delete that step.
    
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

<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">get_identity</a>(...) -> AgentIdentity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the identity associated with an agent. The identity is the service account the agent uses when executing tools.

In `auto` mode (the default), the platform keeps the identity's roles in sync with the agent's tool configuration.

In `manual` mode, the roles are frozen and the platform will not modify them when the agent is updated.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agents.get_identity(
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

**agent_key:** `AgentKey` — The unique key of the agent.
    
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

<details><summary><code>client.agents.<a href="src/vectara/agents/client.py">update_identity</a>(...) -> AgentIdentity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the agent's identity role management mode and/or roles.

Setting mode to `manual` freezes the current roles. The platform will no longer recompute roles when the agent's tool configuration changes. This is useful when you need to grant the agent additional permissions beyond what its tools require.

Setting mode to `auto` resumes platform-managed roles. The platform will immediately resync the roles to match the current tool configuration.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agents.update_identity(
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

**agent_key:** `AgentKey` — The unique key of the agent.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[AgentIdentityMode]` 
    
</dd>
</dl>

<dl>
<dd>

**api_roles:** `typing.Optional[typing.List[ApiRole]]` — Customer-level roles to assign. Only applied in `manual` mode.
    
</dd>
</dl>

<dl>
<dd>

**corpus_roles:** `typing.Optional[typing.List[CorpusRole]]` — Corpus-specific roles to assign. Only applied in `manual` mode.
    
</dd>
</dl>

<dl>
<dd>

**agent_roles:** `typing.Optional[typing.List[AgentRole]]` — Agent-specific roles to assign. Only applied in `manual` mode.
    
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
<details><summary><code>client.agent_sessions.<a href="src/vectara/agent_sessions/client.py">list</a>(...) -> ListAgentSessionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all agent sessions for the specified agent. This endpoint returns high-level information about each session, with optional filtering and pagination. Use this operation to browse existing sessions or to locate a specific session key for further inspection or updates.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_sessions.list(
    agent_key="customer_support",
    filter="support.*",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_sessions.<a href="src/vectara/agent_sessions/client.py">create</a>(...) -> AgentSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new session for interacting with an agent. A session is the conversation container that maintains state across all messages, events, tool use, and agent responses.

This endpoint initializes the session and enables you to configure its initial properties, including optional metadata. Metadata can influence agent behavior, personalize responses, or apply access controls. Instructions and tools can also reference metadata using `${\session.metadata.field}` or `$\ref` syntax.

A session also serves as the workspace for artifacts, enabling file uploads and multi-step workflows. For more information, see [Working with artifacts in sessions](https://docs.vectara.com/docs/agent-os/sessions#working-with-artifacts-in-sessions).

## Example request

```json
\$ curl -X POST https://api.vectara.io/v2/agents/support-agent/sessions \
-H "Authorization: Bearer YOUR_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "key": "user_12345_session",
  "name": "Customer Support Session",
  "metadata": {
    "user_role": "premium",
    "language": "en"
  }
}'
```
A successful response includes the unique session key, configuration metadata, and timestamps for creation and last update.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arbitrary metadata associated with the session.
    
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

**from_session:** `typing.Optional[CreateAgentSessionRequestFromSession]` 

Create a new session by forking an existing one. By default, copies all visible events
and artifacts from the source session without compaction. Optionally specify exactly one of
include_up_to_event_id or compact_up_to_event_id to control which events are included
and whether they are compacted. These two fields are mutually exclusive.
    
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

<details><summary><code>client.agent_sessions.<a href="src/vectara/agent_sessions/client.py">get</a>(...) -> AgentSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the full details of a specific agent session using its unique session key. The response includes the session's configuration, metadata, timestamps, and other stored properties. Use this endpoint to inspect the current state of a session or verify its configuration.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_sessions.<a href="src/vectara/agent_sessions/client.py">update</a>(...) -> AgentSession</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the configuration of an existing agent session. This endpoint enables you to modify fields such as the name, description, or metadata.

Updated metadata immediately influences agent behavior and becomes available to instructions and tools for the remainder of the session. For more details about configuring the agent session, see [Create agent session](https://docs.vectara.com/docs/rest-api/create-agent-session).
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arbitrary metadata associated with the session.
    
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
<details><summary><code>client.agent_events.<a href="src/vectara/agent_events/client.py">list</a>(...) -> ListAgentEventsResponse</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_events.list(
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

**include_hidden:** `typing.Optional[bool]` — Include hidden events (compacted or manually hidden) in the response. Defaults to false.
    
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

<details><summary><code>client.agent_events.<a href="src/vectara/agent_events/client.py">create_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
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
from vectara import Vectara, AgentInput_Text
from vectara.environment import VectaraEnvironment
from vectara.agent_events import CreateAgentEventsStreamRequestBody_InputMessage

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_events.create_stream(
    agent_key="customer_support",
    session_key="customer_support_chat",
    request=CreateAgentEventsStreamRequestBody_InputMessage(
        stream_response=True,
        messages=[
            AgentInput_Text(
                content="I need help with my widget installation",
            )
        ],
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

**request:** `CreateAgentEventsStreamRequestBody` — A request to create input for an agent session.
    
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

<details><summary><code>client.agent_events.<a href="src/vectara/agent_events/client.py">create</a>(...) -> AgentResponse</code></summary>
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
from vectara import Vectara, AgentInput_Text
from vectara.environment import VectaraEnvironment
from vectara.agent_events import CreateAgentEventsStreamRequestBody_InputMessage

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_events.create_stream(
    agent_key="customer_support",
    session_key="customer_support_chat",
    request=CreateAgentEventsStreamRequestBody_InputMessage(
        stream_response=False,
        messages=[
            AgentInput_Text(
                content="I need help with my widget installation",
            )
        ],
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

**request:** `CreateAgentEventsRequestBody` — A request to create input for an agent session.
    
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

<details><summary><code>client.agent_events.<a href="src/vectara/agent_events/client.py">get</a>(...) -> AgentEvent</code></summary>
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_events.<a href="src/vectara/agent_events/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete an event from a session. Removes the event from both the metadata database and the encrypted event store.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_events.delete(
    agent_key="customer_support",
    session_key="customer_support_chat",
    event_id="event_id",
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

**agent_key:** `AgentKey` 
    
</dd>
</dl>

<dl>
<dd>

**session_key:** `AgentSessionKey` 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` 
    
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

<details><summary><code>client.agent_events.<a href="src/vectara/agent_events/client.py">hide</a>(...) -> AgentEvent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manually hide an event in a session. Sets hide_reason to 'manual'.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_events.hide(
    agent_key="customer_support",
    session_key="customer_support_chat",
    event_id="event_id",
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

**agent_key:** `AgentKey` 
    
</dd>
</dl>

<dl>
<dd>

**session_key:** `AgentSessionKey` 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` 
    
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

<details><summary><code>client.agent_events.<a href="src/vectara/agent_events/client.py">unhide</a>(...) -> AgentEvent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unhide a hidden event in a session. Clears the hide_reason.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_events.unhide(
    agent_key="customer_support",
    session_key="customer_support_chat",
    event_id="event_id",
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

**agent_key:** `AgentKey` 
    
</dd>
</dl>

<dl>
<dd>

**session_key:** `AgentSessionKey` 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` 
    
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

## AgentArtifacts
<details><summary><code>client.agent_artifacts.<a href="src/vectara/agent_artifacts/client.py">list</a>(...) -> ListSessionArtifactsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all artifacts stored in a specific agent session, with cursor-based pagination. Artifacts are files either uploaded by the user, or generated within a session. This endpoint shows you what files exist in a session, but does not include the file content.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_artifacts.list(
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

**session_key:** `AgentSessionKey` — The unique key of the session to list the associated artifacts.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of artifacts to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of artifacts after the limit has been reached.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListAgentArtifactsRequestSortBy]` — The field to sort results by.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ListAgentArtifactsRequestOrderBy]` — The ordering direction of the results.
    
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

<details><summary><code>client.agent_artifacts.<a href="src/vectara/agent_artifacts/client.py">get</a>(...) -> SessionArtifact</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific artifact by its unique `artifact_id`, including metadata and base64-encoded file content.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_artifacts.get(
    agent_key="customer_support",
    session_key="customer_support_chat",
    artifact_id="art_report_pdf_a3f2",
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

**artifact_id:** `str` — The unique identifier of the artifact to retrieve.
    
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

## Agent Schedules
<details><summary><code>client.agent_schedules.<a href="src/vectara/agent_schedules/client.py">list</a>(...) -> ListAgentSchedulesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all schedules for the specified agent. This endpoint returns high-level information about each schedule including execution status and next scheduled execution time.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_schedules.list(
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

**agent_key:** `AgentKey` — The unique identifier of the agent to list schedules for.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of schedules to return in the list.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of schedules after the limit has been reached.
    
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

<details><summary><code>client.agent_schedules.<a href="src/vectara/agent_schedules/client.py">create</a>(...) -> AgentSchedule</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new schedule for automatically executing an agent at specified intervals. Each execution creates a new session with the configured message and metadata.

Schedules enable automated agent workflows such as daily reports, periodic monitoring, or regular data processing. The schedule will create sessions tagged with metadata to identify them as scheduled executions.

## Example request

```json
\$ curl -X POST https://api.vectara.io/v2/agents/support-agent/schedules \
-H "Authorization: Bearer YOUR_API_KEY" \c
-H "Content-Type: application/json" \
-d '{
  "key": "daily-report",
  "name": "Daily Summary Report",
  "message": [{"type": "text", "content": "Generate a summary of today's activities"}],
  "schedule": {
    "type": "interval",
    "interval": "PT24H"
  },
  "session_metadata": {
    "report_type": "daily"
  }
}'
```
A successful response includes the unique schedule key, configuration, and creation timestamp.
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
from vectara import Vectara, AgentInput_Text, ScheduleConfiguration_Interval
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_schedules.create(
    agent_key="customer_support",
    name="Daily Summary Report",
    message=[
        AgentInput_Text(
            content="I need help with my widget installation",
        )
    ],
    schedule=ScheduleConfiguration_Interval(
        interval="PT24H",
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

**agent_key:** `AgentKey` — The unique key of the agent to create a schedule for.
    
</dd>
</dl>

<dl>
<dd>

**name:** `AgentScheduleName` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.List[AgentInput]` — The input message to send to the agent on each scheduled execution.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `ScheduleConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[AgentScheduleKey]` — Optional unique key for the schedule. If not provided, will be auto-generated.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional detailed description of the schedule's purpose.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the schedule should be active upon creation.
    
</dd>
</dl>

<dl>
<dd>

**session_metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arbitrary metadata to include in each session created by this schedule.
    
</dd>
</dl>

<dl>
<dd>

**max_executions_to_keep:** `typing.Optional[int]` — Maximum number of past execution records to keep. Defaults to 10.
    
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

<details><summary><code>client.agent_schedules.<a href="src/vectara/agent_schedules/client.py">get</a>(...) -> AgentSchedule</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the full details of a specific agent schedule using its unique schedule key. The response includes the schedule's configuration, execution history, and timestamps.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_schedules.get(
    agent_key="customer_support",
    schedule_key="daily-report",
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

**agent_key:** `AgentKey` — The unique key of the agent.
    
</dd>
</dl>

<dl>
<dd>

**schedule_key:** `AgentScheduleKey` — The unique key of the schedule.
    
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

<details><summary><code>client.agent_schedules.<a href="src/vectara/agent_schedules/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an agent schedule. This stops all future executions of the schedule.

Sessions that were previously created by this schedule are not deleted and remain accessible.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_schedules.delete(
    agent_key="customer_support",
    schedule_key="daily-report",
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

**agent_key:** `AgentKey` — The unique key of the agent.
    
</dd>
</dl>

<dl>
<dd>

**schedule_key:** `AgentScheduleKey` — The unique key of the schedule to delete.
    
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

<details><summary><code>client.agent_schedules.<a href="src/vectara/agent_schedules/client.py">update</a>(...) -> AgentSchedule</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing agent schedule. All fields are optional - only provided fields will be updated (PATCH semantics).

You can pause/resume a schedule by setting the `enabled` field to `false`/`true`. Updating the schedule configuration (interval or cron) will reschedule future executions but will not affect executions currently in progress.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_schedules.update(
    agent_key="customer_support",
    schedule_key="daily-report",
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

**agent_key:** `AgentKey` — The unique key of the agent.
    
</dd>
</dl>

<dl>
<dd>

**schedule_key:** `AgentScheduleKey` — The unique key of the schedule to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[AgentScheduleName]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Updated description of the schedule's purpose.
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[typing.List[AgentInput]]` — Updated input message to send to the agent on each scheduled execution.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[ScheduleConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Updated enabled status for the schedule.
    
</dd>
</dl>

<dl>
<dd>

**session_metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Updated metadata to include in each session created by this schedule.
    
</dd>
</dl>

<dl>
<dd>

**max_executions_to_keep:** `typing.Optional[int]` — Updated maximum number of past execution records to keep.
    
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

<details><summary><code>client.agent_schedules.<a href="src/vectara/agent_schedules/client.py">list_executions</a>(...) -> ListAgentScheduleExecutionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all execution attempts for a schedule, ordered by most recent first.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.agent_schedules.list_executions(
    agent_key="customer_support",
    schedule_key="daily-report",
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

**agent_key:** `AgentKey` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_key:** `AgentScheduleKey` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` 
    
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

## Pipelines
<details><summary><code>client.pipelines.<a href="src/vectara/pipelines/client.py">list</a>(...) -> ListPipelinesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all pipelines with optional filtering by source type, status, or enabled state.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipelines.list()

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

**source_type:** `typing.Optional[ListPipelinesRequestSourceType]` — Filter pipelines by source type.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PipelineStatus]` — Filter pipelines by status.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Filter pipelines by enabled state.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — A regex filter on pipeline name and description.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of pipelines to return.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of pipelines after the limit has been reached.
    
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

<details><summary><code>client.pipelines.<a href="src/vectara/pipelines/client.py">create</a>(...) -> Pipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new pipeline that continuously ingests data from a source system and sends each record to an agent for processing. A new agent session is created per source record. A pipeline is distinct from an agent schedule (which is a recurring single execution of an agent) and from a connector (which is a bidirectional chat integration like Slack). A pipeline is an automated, one-directional flow of all source data through an agent.
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
from vectara import Vectara, PipelineSource_S3, PipelineTrigger_Cron, PipelineTransform_Agent
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipelines.create(
    name="SharePoint Legal Docs Ingest",
    source=PipelineSource_S3(
        type="string",
    ),
    trigger=PipelineTrigger_Cron(
        expression="0 */6 * * *",
    ),
    transform=PipelineTransform_Agent(
        agent_key="customer_support",
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

**request:** `CreatePipelineRequest` 
    
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

<details><summary><code>client.pipelines.<a href="src/vectara/pipelines/client.py">get</a>(...) -> Pipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a pipeline by its key, including its current status, watermark, and configuration.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipelines.get(
    pipeline_key="sharepoint-legal-ingest",
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

**pipeline_key:** `PipelineKey` — The unique key of the pipeline.
    
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

<details><summary><code>client.pipelines.<a href="src/vectara/pipelines/client.py">replace</a>(...) -> Pipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace a pipeline's configuration. The full pipeline definition must be provided.
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
from vectara import Vectara, PipelineSource_S3, PipelineTrigger_Cron, PipelineTransform_Agent
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipelines.replace(
    pipeline_key="sharepoint-legal-ingest",
    name="SharePoint Legal Docs Ingest",
    source=PipelineSource_S3(
        type="string",
    ),
    trigger=PipelineTrigger_Cron(
        expression="0 */6 * * *",
    ),
    transform=PipelineTransform_Agent(
        agent_key="customer_support",
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

**pipeline_key:** `PipelineKey` — The unique key of the pipeline to replace.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreatePipelineRequest` 
    
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

<details><summary><code>client.pipelines.<a href="src/vectara/pipelines/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a pipeline and its run history. This cancels any in-progress runs. Agent sessions created by this pipeline are not deleted.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipelines.delete(
    pipeline_key="sharepoint-legal-ingest",
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

**pipeline_key:** `PipelineKey` — The unique key of the pipeline to delete.
    
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

<details><summary><code>client.pipelines.<a href="src/vectara/pipelines/client.py">update</a>(...) -> Pipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a pipeline's configuration. Omitted fields are preserved.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipelines.update(
    pipeline_key="sharepoint-legal-ingest",
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

**pipeline_key:** `PipelineKey` — The unique key of the pipeline to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[PipelineName]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[UpdatePipelineSource]` 
    
</dd>
</dl>

<dl>
<dd>

**trigger:** `typing.Optional[PipelineTrigger]` 
    
</dd>
</dl>

<dl>
<dd>

**transform:** `typing.Optional[PipelineTransform]` 
    
</dd>
</dl>

<dl>
<dd>

**sync_mode:** `typing.Optional[PipelineSyncMode]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
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

<details><summary><code>client.pipelines.<a href="src/vectara/pipelines/client.py">trigger</a>(...) -> PipelineRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manually trigger a pipeline run outside of the normal schedule. The pipeline will fetch new data from the source and process it through the agent. Returns the created run.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipelines.trigger(
    pipeline_key="sharepoint-legal-ingest",
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

**pipeline_key:** `PipelineKey` — The unique key of the pipeline to trigger.
    
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

## PipelineDeadLetterEntries
<details><summary><code>client.pipeline_dead_letter_entries.<a href="src/vectara/pipeline_dead_letter_entries/client.py">list</a>(...) -> ListPipelineDeadLetterEntriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List dead letters for a pipeline, with optional filtering by status or run.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipeline_dead_letter_entries.list(
    pipeline_key="sharepoint-legal-ingest",
    last_run_id="run_pip_abc_manual_550e8400",
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

**pipeline_key:** `PipelineKey` — The unique key of the pipeline.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[DeadLetterStatus]` — Filter dead letters by status.
    
</dd>
</dl>

<dl>
<dd>

**last_run_id:** `typing.Optional[PipelineRunId]` — Filter dead letters to those from a specific run.
    
</dd>
</dl>

<dl>
<dd>

**origin:** `typing.Optional[DeadLetterOrigin]` — Filter dead letters by origin.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of dead letters to return.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of dead letters after the limit has been reached.
    
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

<details><summary><code>client.pipeline_dead_letter_entries.<a href="src/vectara/pipeline_dead_letter_entries/client.py">create</a>(...) -> PipelineDeadLetterEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manually add a source record to the dead letter queue for reprocessing. Use this when you want to force a record through the pipeline again, for example when the agent or judge made an incorrect decision.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipeline_dead_letter_entries.create(
    pipeline_key="sharepoint-legal-ingest",
    source_record_id="source_record_id",
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

**pipeline_key:** `PipelineKey` — The unique key of the pipeline.
    
</dd>
</dl>

<dl>
<dd>

**source_record_id:** `str` 

The identifier for the source record to add. Format depends on connector type:
- S3: the object key (e.g. `legal/contracts/doc.pdf`)
- SharePoint: the drive item ID
    
</dd>
</dl>

<dl>
<dd>

**error_message:** `typing.Optional[str]` — Optional reason for manually adding this record.
    
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

<details><summary><code>client.pipeline_dead_letter_entries.<a href="src/vectara/pipeline_dead_letter_entries/client.py">get</a>(...) -> PipelineDeadLetterEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific dead letter by its ID.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipeline_dead_letter_entries.get(
    pipeline_key="sharepoint-legal-ingest",
    dead_letter_id="dead_letter_id",
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

**pipeline_key:** `PipelineKey` — The unique key of the pipeline.
    
</dd>
</dl>

<dl>
<dd>

**dead_letter_id:** `str` — The unique identifier of the dead letter.
    
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

<details><summary><code>client.pipeline_dead_letter_entries.<a href="src/vectara/pipeline_dead_letter_entries/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a dead letter from the queue. Use this to dismiss a known failure that does not need retrying.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipeline_dead_letter_entries.delete(
    pipeline_key="sharepoint-legal-ingest",
    dead_letter_id="dead_letter_id",
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

**pipeline_key:** `PipelineKey` — The unique key of the pipeline.
    
</dd>
</dl>

<dl>
<dd>

**dead_letter_id:** `str` — The unique identifier of the dead letter.
    
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

<details><summary><code>client.pipeline_dead_letter_entries.<a href="src/vectara/pipeline_dead_letter_entries/client.py">process</a>(...) -> PipelineRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process dead letters by creating a new pipeline run that re-fetches the specified records from source and sends them through the agent. If no filters are provided, all pending dead letters are processed.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipeline_dead_letter_entries.process(
    pipeline_key="sharepoint-legal-ingest",
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

**pipeline_key:** `PipelineKey` — The unique key of the pipeline.
    
</dd>
</dl>

<dl>
<dd>

**source_record_ids:** `typing.Optional[typing.List[str]]` — Specific source record IDs to process. If omitted, processes all matching dead letters.
    
</dd>
</dl>

<dl>
<dd>

**last_run_id:** `typing.Optional[PipelineRunId]` — Only process dead letters from this specific run.
    
</dd>
</dl>

<dl>
<dd>

**origin:** `typing.Optional[DeadLetterOrigin]` — Only process dead letters with this origin.
    
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

## Pipeline Runs
<details><summary><code>client.pipeline_runs.<a href="src/vectara/pipeline_runs/client.py">list</a>(...) -> ListPipelineRunsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List execution runs for a pipeline, with optional filtering by status.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipeline_runs.list(
    pipeline_key="sharepoint-legal-ingest",
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

**pipeline_key:** `PipelineKey` — The unique key of the pipeline.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PipelineRunStatus]` — Filter runs by status.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[datetime.datetime]` — Only return runs created after this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of runs to return.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of runs after the limit has been reached.
    
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

<details><summary><code>client.pipeline_runs.<a href="src/vectara/pipeline_runs/client.py">get</a>(...) -> PipelineRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a specific pipeline run including record counts, session keys, and status.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.pipeline_runs.get(
    pipeline_key="sharepoint-legal-ingest",
    run_id="run_pip_abc_manual_550e8400",
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

**pipeline_key:** `PipelineKey` — The unique key of the pipeline.
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `PipelineRunId` — The unique identifier of the run.
    
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

## Glossaries
<details><summary><code>client.glossaries.<a href="src/vectara/glossaries/client.py">list</a>(...) -> ListGlossariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all glossaries available to the authenticated user.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.glossaries.list(
    filter="engineering",
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

**filter:** `typing.Optional[str]` — A case-insensitive substring to filter glossary names and descriptions.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of glossaries to return.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of glossaries.
    
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

<details><summary><code>client.glossaries.<a href="src/vectara/glossaries/client.py">create</a>(...) -> Glossary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new glossary. A glossary is a reusable mapping of terms to expanded forms that agents use to expand abbreviations and acronyms in user messages.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.glossaries.create(
    name="Engineering Acronyms",
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

**name:** `str` — Human-readable name for the glossary.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[GlossaryKey]` — A unique key for the glossary. If not provided, one will be auto-generated from the name.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of what this glossary covers.
    
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

<details><summary><code>client.glossaries.<a href="src/vectara/glossaries/client.py">get</a>(...) -> Glossary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the metadata of a specific glossary.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.glossaries.get(
    glossary_key="eng-acronyms",
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

**glossary_key:** `GlossaryKey` — The unique key of the glossary.
    
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

<details><summary><code>client.glossaries.<a href="src/vectara/glossaries/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a glossary and all its entries.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.glossaries.delete(
    glossary_key="eng-acronyms",
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

**glossary_key:** `GlossaryKey` — The unique key of the glossary to delete.
    
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

<details><summary><code>client.glossaries.<a href="src/vectara/glossaries/client.py">update</a>(...) -> Glossary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the metadata of a glossary.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.glossaries.update(
    glossary_key="eng-acronyms",
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

**glossary_key:** `GlossaryKey` — The unique key of the glossary to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Updated name for the glossary.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Updated description.
    
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

<details><summary><code>client.glossaries.<a href="src/vectara/glossaries/client.py">list_entries</a>(...) -> GlossaryEntriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the entries in a glossary.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.glossaries.list_entries(
    glossary_key="eng-acronyms",
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

**glossary_key:** `GlossaryKey` — The unique key of the glossary.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of entries to return.
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `typing.Optional[str]` — Used to retrieve the next page of entries.
    
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

<details><summary><code>client.glossaries.<a href="src/vectara/glossaries/client.py">upsert_entries</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk upsert entries into a glossary. Entries with existing terms are updated and new terms are inserted. The glossary index blob is rebuilt after the upsert.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.glossaries.upsert_entries(
    glossary_key="eng-acronyms",
    entries={
        "k8s": "Kubernetes",
        "tf": "Terraform"
    },
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

**glossary_key:** `GlossaryKey` — The unique key of the glossary.
    
</dd>
</dl>

<dl>
<dd>

**entries:** `typing.Dict[str, str]` 

A map of terms to their expanded forms. Keys are terms (1–200 characters);
values are expansions (1–1000 characters).
    
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

<details><summary><code>client.glossaries.<a href="src/vectara/glossaries/client.py">delete_entries</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk delete entries from a glossary by term. The glossary index blob is rebuilt after deletion.
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
from vectara.environment import VectaraEnvironment

client = Vectara(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=VectaraEnvironment.PRODUCTION,
)

client.glossaries.delete_entries(
    glossary_key="eng-acronyms",
    terms=[
        "terms"
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

**glossary_key:** `GlossaryKey` — The unique key of the glossary.
    
</dd>
</dl>

<dl>
<dd>

**terms:** `typing.List[str]` — The terms to remove from the glossary.
    
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

