# This file was auto-generated by Fern from our API Definition.

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chunking_strategy import ChunkingStrategy
from ..types.corpus_key import CorpusKey
from ..types.document import Document
from ..types.table_extraction_config import TableExtractionConfig
from .raw_client import AsyncRawUploadClient, RawUploadClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class UploadClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUploadClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUploadClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUploadClient
        """
        return self._raw_client

    def file(
        self,
        corpus_key: CorpusKey,
        *,
        file: core.File,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        chunking_strategy: typing.Optional[ChunkingStrategy] = OMIT,
        table_extraction_config: typing.Optional[TableExtractionConfig] = OMIT,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Upload files such as PDFs and Word Documents for automatic text extraction and metadata parsing.
        The request expects a `multipart/form-data` format containing the following parts:
        * `metadata` - Optionally specifies a JSON object representing any additional metadata to be associated with the extracted document. For example, `'metadata={"key": "value"};type=application/json'`
        * `chunking_strategy` - If provided, specifies the chunking strategy for the platform to use. If you do not set this option, the platform uses the default strategy, which creates one chunk per sentence. You can explicitly set sentence chunking with `'chunking_strategy={"type":"sentence_chunking_strategy"};type=application/json'` or use max chars chunking with `'chunking_strategy={"type":"max_chars_chunking_strategy","max_chars_per_chunk":200};type=application/json'`
        * `table_extraction_config` - You can optionally specify whether to extract table data from the uploaded file. If you do not set this option, the platform does not extract tables from PDF files. Example config, `'table_extraction_config={"extract_tables":true};type=application/json'`
        * `file` - Specifies the file that you want to upload.
        * `filename` - Specified as part of the file field with the file name that you want to associate with the uploaded file. For a curl example, use the following syntax: `'file=@/path/to/file/file.pdf;filename=desired_filename.pdf'`

        For more detailed information, see this [File Upload API guide.](https://docs.vectara.com/docs/api-reference/indexing-apis/file-upload/file-upload)

        Parameters
        ----------
        corpus_key : CorpusKey
            The unique key identifying the corpus of which to upload the file.

        file : core.File
            See core.File for more documentation

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Arbitrary object that will be attached as document metadata to the extracted document.

        chunking_strategy : typing.Optional[ChunkingStrategy]

        table_extraction_config : typing.Optional[TableExtractionConfig]

        filename : typing.Optional[str]
            Optional multipart section to override the filename.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            The extracted document has been parsed and added to the corpus.

        Examples
        --------
        from vectara import Vectara
        client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.upload.file(corpus_key='my-corpus', )
        """
        response = self._raw_client.file(
            corpus_key,
            file=file,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            metadata=metadata,
            chunking_strategy=chunking_strategy,
            table_extraction_config=table_extraction_config,
            filename=filename,
            request_options=request_options,
        )
        return response.data


class AsyncUploadClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUploadClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUploadClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUploadClient
        """
        return self._raw_client

    async def file(
        self,
        corpus_key: CorpusKey,
        *,
        file: core.File,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        chunking_strategy: typing.Optional[ChunkingStrategy] = OMIT,
        table_extraction_config: typing.Optional[TableExtractionConfig] = OMIT,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Document:
        """
        Upload files such as PDFs and Word Documents for automatic text extraction and metadata parsing.
        The request expects a `multipart/form-data` format containing the following parts:
        * `metadata` - Optionally specifies a JSON object representing any additional metadata to be associated with the extracted document. For example, `'metadata={"key": "value"};type=application/json'`
        * `chunking_strategy` - If provided, specifies the chunking strategy for the platform to use. If you do not set this option, the platform uses the default strategy, which creates one chunk per sentence. You can explicitly set sentence chunking with `'chunking_strategy={"type":"sentence_chunking_strategy"};type=application/json'` or use max chars chunking with `'chunking_strategy={"type":"max_chars_chunking_strategy","max_chars_per_chunk":200};type=application/json'`
        * `table_extraction_config` - You can optionally specify whether to extract table data from the uploaded file. If you do not set this option, the platform does not extract tables from PDF files. Example config, `'table_extraction_config={"extract_tables":true};type=application/json'`
        * `file` - Specifies the file that you want to upload.
        * `filename` - Specified as part of the file field with the file name that you want to associate with the uploaded file. For a curl example, use the following syntax: `'file=@/path/to/file/file.pdf;filename=desired_filename.pdf'`

        For more detailed information, see this [File Upload API guide.](https://docs.vectara.com/docs/api-reference/indexing-apis/file-upload/file-upload)

        Parameters
        ----------
        corpus_key : CorpusKey
            The unique key identifying the corpus of which to upload the file.

        file : core.File
            See core.File for more documentation

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Arbitrary object that will be attached as document metadata to the extracted document.

        chunking_strategy : typing.Optional[ChunkingStrategy]

        table_extraction_config : typing.Optional[TableExtractionConfig]

        filename : typing.Optional[str]
            Optional multipart section to override the filename.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Document
            The extracted document has been parsed and added to the corpus.

        Examples
        --------
        from vectara import AsyncVectara
        import asyncio
        client = AsyncVectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.upload.file(corpus_key='my-corpus', )
        asyncio.run(main())
        """
        response = await self._raw_client.file(
            corpus_key,
            file=file,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            metadata=metadata,
            chunking_strategy=chunking_strategy,
            table_extraction_config=table_extraction_config,
            filename=filename,
            request_options=request_options,
        )
        return response.data
