import logging
import threading
import typing

from datetime import datetime, timedelta

from . import SearchCorporaParameters, GenerationParameters, ChatParameters, ChatFullResponse
from .base_client import BaseVectara, AsyncBaseVectara, OMIT
from vectara.managers.corpus import CorpusManager
from vectara.managers.upload import UploadManager
from vectara.utils import LabHelper

from typing import Union

from .core import RequestOptions


class ChatSessionManager:
    def __init__(self, session_expiry_time: timedelta = timedelta(days=7),
                 cleanup_interval_in_seconds: int = 43200):
        self.sessions: typing.Dict[str, typing.Any] = {}
        self.session_expiry_time = session_expiry_time
        self.lock = threading.Lock()
        self.cleanup_event = threading.Event()
        self.cleanup_interval_in_seconds = cleanup_interval_in_seconds  # Default is set to 12 hours in
        # seconds
        self.cleanup_thread = threading.Thread(target=self._run_cleanup, daemon=True)
        self.cleanup_thread.start()

    def create_session(self, chat_id: str,
                       search: SearchCorporaParameters,
                       generation: typing.Optional[GenerationParameters] = OMIT,
                       chat: typing.Optional[ChatParameters] = OMIT,
                       request_options: typing.Optional[RequestOptions] = None,
                       request_timeout: typing.Optional[int] = None,
                       request_timeout_millis: typing.Optional[int] = None,
                       ):
        with self.lock:
            self.sessions[chat_id] = {
                "search": search,
                "generation": generation,
                "chat": chat,
                "created_at": datetime.now(),
                "request_timeout": request_timeout,
                "request_timeout_millis": request_timeout_millis,
                "request_options": request_options
            }

    def get_session(self, chat_id: str):
        with self.lock:
            session = self.sessions.get(chat_id)
            if not session:
                return None

            return session

    def clean_expired_sessions(self):
        with self.lock:
            now = datetime.now()
            expired_chat_ids = [
                chat_id for chat_id, session in self.sessions.items()
                if now - session["created_at"] > self.session_expiry_time
            ]
            for chat_id in expired_chat_ids:
                del self.sessions[chat_id]

    def _run_cleanup(self):
        while not self.cleanup_event.wait(self.cleanup_interval_in_seconds):
            self.clean_expired_sessions()


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
        self.session_manager = ChatSessionManager()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.corpus_manager: Union[None, CorpusManager] = None
        self.upload_manager: Union[None, UploadManager] = None
        self.lab_helper: Union[None, LabHelper] = None

    def set_corpus_manager(self, corpus_manager: CorpusManager) -> None:
        self.corpus_manager = corpus_manager

    def set_upload_manager(self, upload_manager: UploadManager) -> None:
        self.upload_manager = upload_manager

    def set_lab_helper(self, lab_helper: LabHelper) -> None:
        self.lab_helper = lab_helper

    def chat(
            self,
            *,
            query: str,
            search: SearchCorporaParameters = OMIT,
            request_timeout: typing.Optional[int] = None,
            request_timeout_millis: typing.Optional[int] = None,
            generation: typing.Optional[GenerationParameters] = OMIT,
            chat: typing.Optional[ChatParameters] = OMIT,
            chat_id: typing.Optional[str] = None,
            request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatFullResponse:
        """
        Modified `chat` method to support chat_id for session reuse.

        Parameters
        ----------
        query : str
            The chat message or question.
        search : typing.Optional[SearchCorporaParameters]
            Retrieval parameters. Optional if chat_id is provided.
        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.
        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.
        generation : typing.Optional[GenerationParameters]
            Parameters for response generation.
        chat : typing.Optional[ChatParameters]
            Chat-specific parameters. Optional if chat_id is provided.
        chat_id : typing.Optional[str]
            ID of the chat session to reuse stored session data.
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatFullResponse
        """

        if not chat_id and not search:
            raise ValueError("`search` parameter is required when `chat_id` is not provided.")

        if chat_id:
            session = self.session_manager.get_session(chat_id)
            if session:
                search = session.get("search")
                generation = session.get("generation")
                chat = session.get("chat")
                request_timeout = session.get("request_timeout")
                request_timeout_millis = session.get("request_timeout_millis")
                request_options = session.get("request_options")
                return self.chats.create_turns(
                    chat_id=chat_id,
                    query=query,
                    search=search,
                    generation=generation,
                    chat=chat,
                    request_options=request_options,
                    request_timeout=request_timeout,
                    request_timeout_millis=request_timeout_millis,
                )

        response = super().chat(
            query=query,
            search=search,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            generation=generation,
            chat=chat,
            request_options=request_options,
        )

        if response.chat_id:
            self.session_manager.create_session(response.chat_id, search, generation, chat, request_timeout,
                                                request_timeout_millis, request_options)
        return response


class AsyncVectara(AsyncBaseVectara):
    pass
