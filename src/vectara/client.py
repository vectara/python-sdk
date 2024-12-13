import logging
from typing import Union, Iterator, Optional

from vectara.managers.corpus import CorpusManager
from vectara.managers.upload import UploadManager
from vectara.managers.document import DocumentManager
from vectara.utils import LabHelper

from . import SearchCorporaParameters, GenerationParameters, ChatParameters, ChatStreamedResponse
from .base_client import BaseVectara, AsyncBaseVectara, OMIT
from .core import RequestOptions


class ChatSession:
    def __init__(
            self,
            client,
            search: SearchCorporaParameters,
            generation: Optional[GenerationParameters] = OMIT,
            chat_id: Optional[str] = None,
            request_timeout: Optional[int] = None,
            request_timeout_millis: Optional[int] = None,
            chat_config: Optional[ChatParameters] = OMIT,
            request_options: Optional[RequestOptions] = None,
    ):
        self.client = client
        self.chat_id = chat_id
        self.search = search
        self.generation = generation
        self.chat_config = chat_config
        self.request_timeout = request_timeout
        self.request_timeout_millis = request_timeout_millis
        self.request_options = request_options

    def chat(self, query: str):
        """
        Handles chat queries using the session configuration.
        """
        if not self.chat_id:
            response = self.client.chat(
                query=query,
                search=self.search,
                generation=self.generation,
                chat=self.chat_config,
                request_timeout=self.request_timeout,
                request_timeout_millis=self.request_timeout_millis,
                request_options=self.request_options,
            )
            self.chat_id = getattr(response, "chat_id", None)
        else:
            response = self.client.chats.create_turns(
                chat_id=self.chat_id,
                query=query,
                search=self.search,
                generation=self.generation,
                chat=self.chat_config,
                request_timeout=self.request_timeout,
                request_timeout_millis=self.request_timeout_millis,
                request_options=self.request_options,
            )
        return response

    def chat_stream(self, query: str) -> Iterator[ChatStreamedResponse]:
        """
        Handles streaming chat queries using the session configuration.
        """
        if not self.chat_id:
            response = self.client.chat_stream(
                query=query,
                search=self.search,
                generation=self.generation,
                chat=self.chat_config,
                request_timeout=self.request_timeout,
                request_timeout_millis=self.request_timeout_millis,
                request_options=self.request_options,
            )
        else:
            response = self.client.chats.create_turns_stream(
                chat_id=self.chat_id,
                query=query,
                search=self.search,
                generation=self.generation,
                chat=self.chat_config,
                request_timeout=self.request_timeout,
                request_timeout_millis=self.request_timeout_millis,
                request_options=self.request_options,
            )

        yield response


class Vectara(BaseVectara):
    """
    We extend the Vectara client, adding additional helper services. Due to the methodology used in the
    Vectara constructor, hard-coding dependencies and using an internal wrapper, we use lazy initialization
    for the helper classes like the CorpusManager.

    TODO Change Client to build dependencies inside constructor (harder to decouple, but removes optionality)

    """

    def __init__(self, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.corpus_manager: Union[None, CorpusManager] = None
        self.upload_manager: Union[None, UploadManager] = None
        self.lab_helper: Union[None, LabHelper] = None
        self.document_manager: Union[None, DocumentManager] = None

    def set_corpus_manager(self, corpus_manager: CorpusManager) -> None:
        self.corpus_manager = corpus_manager

    def set_upload_manager(self, upload_manager: UploadManager) -> None:
        self.upload_manager = upload_manager

    def set_document_manager(self, document_manager: DocumentManager) -> None:
        self.document_manager = document_manager

    def set_lab_helper(self, lab_helper: LabHelper) -> None:
        self.lab_helper = lab_helper

    def create_chat_session(
            self,
            search: SearchCorporaParameters,
            request_timeout: Optional[int] = None,
            request_timeout_millis: Optional[int] = None,
            generation: Optional[GenerationParameters] = OMIT,
            chat_config: Optional[ChatParameters] = OMIT,
            request_options: Optional[RequestOptions] = None,
    ) -> ChatSession:
        """
        Creates and returns a `ChatSession` object with the specified configuration.
        """
        return ChatSession(
            client=self,
            search=search,
            generation=generation,
            chat_config=chat_config,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            request_options=request_options,
        )


class AsyncVectara(AsyncBaseVectara):
    pass

