import logging
from pathlib import Path
from typing import Union
from abc import ABC, abstractmethod
from vectara.upload.client import UploadClient
from vectara.core.client_wrapper import SyncClientWrapper
from vectara.core.jsonable_encoder import jsonable_encoder
from vectara import VectaraEnvironment
import httpx
import asyncio
from httpx import Response
import mimetypes

class BaseNameTransformer(ABC):

    @abstractmethod
    def transform(self, input_name: Path) -> str:
        """
        Implementations of this class can transform a path into a document Id.
        :param input_name: the path to transform.
        :return: the document Id.
        """
        pass


class UploadWrapper(UploadClient):

    def __init__(self, *, upload_client: UploadClient, customer_id: str):
        self.logger = logging.getLogger(self.__class__.__name__)
        super().__init__(client_wrapper=upload_client._client_wrapper)
        self._client_wrapper = upload_client._client_wrapper
        self.customer_id = customer_id

    def upload(self, corpus_key: str, name: str, content: bytes, content_type: str) -> Response:
        files = {'file': (name, content, content_type)}
        headers = self._client_wrapper.get_headers()
        headers["Customer-Id"] = self.customer_id
        headers["Accept"] = "application/json"

        http_client = self._client_wrapper.httpx_client

        url = VectaraEnvironment.PRODUCTION.default + f"/v2/corpora/{jsonable_encoder(corpus_key)}/upload_file"

        def log_request(request):
            logging.debug(f"Request headers: {request.headers}")

        client = httpx.Client(event_hooks={'request': [log_request]})
        # Trying the old method of putting in the customer Id. Likely can remove.
        #response = client.post(url, files=files, headers=headers, data={"c": self.customer_id})
        response = client.post(url, files=files, headers=headers, data={}, timeout=120.0)

        self.logger.info(f"Response is [{response.status_code}]: {response.reason_phrase}")
        return response


class UploadManager:

    def __init__(self, upload_wrapper: UploadWrapper):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.upload_wrapper = upload_wrapper

    def _discover_mime_type(self, name: str):
        mime_type, encoding = mimetypes.guess_type(name)
        return mime_type

    def upload(self, corpus_key: str, target: Union[str, Path], overwrite=False, check_first=True,
               name_transformer: Union[None, BaseNameTransformer] = None, doc_id: Union[None, str] = None) -> Response:

        if isinstance(target, str):
            target = Path(target)

        # TODO Add directory processing.
        if not doc_id:
            doc_id = target.name

        content_type = self._discover_mime_type(target.name)  # Change this based on extension.
        with open(target, "rb") as f:
            content = f.read()

        return self.upload_wrapper.upload(corpus_key, doc_id, content, content_type)







