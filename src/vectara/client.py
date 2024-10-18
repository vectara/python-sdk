from .base_client import BaseVectara, AsyncBaseVectara
from vectara.managers.corpus import CorpusManager
from vectara.managers.upload import UploadManager, UploadWrapper
from vectara.utils import LabHelper

from typing import Union, Optional, Callable
import logging

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

    def set_corpus_manager(self, corpus_manager: CorpusManager) -> None:
        self.corpus_manager = corpus_manager

    def set_upload_manager(self, upload_manager: UploadManager) -> None:
        self.upload_manager = upload_manager

    def set_lab_helper(self, lab_helper: LabHelper) -> None:
        self.lab_helper = lab_helper

class AsyncVectara(AsyncBaseVectara): 
    pass