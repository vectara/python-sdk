import json
import logging
from pathlib import Path
from typing import Union, Optional, Dict
from vectara.upload.client import UploadClient
from vectara.types import Document
import mimetypes


class UploadManager:

    def __init__(self, upload_client: UploadClient):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.upload_client = upload_client

    def _discover_mime_type(self, name: str):
        mime_type, encoding = mimetypes.guess_type(name)
        return mime_type

    def upload(self, corpus_key: str, target: Union[str, Path], doc_id: Union[None, str] = None,
               metadata: Optional[Dict] = None) -> Document:

        if isinstance(target, str):
            target = Path(target)

        # TODO Add directory processing.
        if not doc_id:
            doc_id = target.name

        content_type = self._discover_mime_type(target.name)  # Change this based on extension.
        with open(target, "rb") as f:
            content = f.read()

        return self.upload_client.file(corpus_key, file=(doc_id, content, content_type), metadata=metadata)






