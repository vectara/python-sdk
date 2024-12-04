from vectara.documents.client import DocumentsClient
from vectara.types import Document, CoreDocument, StructuredDocument
from vectara.utils.hash import calculate_sha256
from typing import Optional, Dict, Any, Union, Tuple
from enum import Enum
import logging

HASH_FIELD = "sha256"

class DocOpEnum(Enum):
    CREATED = 1
    UPDATED = 2
    IGNORED = 3

class DocumentManager:

    def __init__(self, documents_client: DocumentsClient):
        self.documents_client = documents_client
        self.logger = logging.getLogger(self.__class__.__name__)

    def check_exists(self, corpus_key: str, doc_id: str) -> Optional[Document]:
        """
        Checks for a document by Id, returning that Document if it exists, otherwise returning None.

        :param corpus_key: The corpus we expect the document to exist in.
        :param doc_id: The ID of the document
        :return: The found document or None
        """
        def list_documents_gen():
            response = self.documents_client.list(corpus_key, metadata_filter=f"doc.id = '{doc_id}'")

            for item in response:
                yield item

        for document in list_documents_gen():
            return document

        return None

    def check_same(self, corpus_key: str, doc_id: str, content: bytes, metadata: Optional[Dict[str, Any]] = None) -> Tuple[bool, Optional[bool]]:
        """
        Checks whether the corpus contains the existing document with a matching SHA256 hash and same metadata attributes.
        
        This will only check the metadata attributes listed in the method signature, if there are additional metadata
        attributes on the document in the corpus, these will be ignored.
        
        :param corpus_key: the corpus which holds the document
        :param doc_id: the id of the document we are checking
        :param content: the byte contents of the document we are checking.
        :param metadata: metadata fields to validate.
        :return: A boolean indicator that the document was found, has the same content and listed metadata attributes match
        """

        doc = self.check_exists(corpus_key, doc_id)
        if not doc:
            return False, None

        if doc.metadata and (HASH_FIELD not in doc.metadata or type(doc.metadata[HASH_FIELD]) is not str):
            return True, False

        # TODO Validate that document has matching metadata
        if metadata:
            if len(metadata.keys()) > 0 and doc.metadata is None:
                return True, False

            for key in metadata.keys():
                value = metadata[key]
                if value is None:
                    raise TypeError("Cannot compare a metadata attribute of value None")

                if not doc.metadata or key not in doc.metadata:
                    # Either we don't have any existing metadata or the key isn't present.
                    return True, False

                existing = doc.metadata[key]

                if existing != value:
                    return True, False

        if not doc.metadata or HASH_FIELD not in doc.metadata:
            # Existing document does not have hash field set.
            return True, False

        existing_hash: str = str(doc.metadata[HASH_FIELD])
        current_hash: str = calculate_sha256(content)
        if existing_hash.lower() != current_hash.lower():
            # Existing document has different value for hash field.
            return True, False
        else:
            return True, True


    def index_doc(self, corpus_key: str, doc: Union[CoreDocument, StructuredDocument]) -> DocOpEnum:

        # Remove the sha256 hash from metadata.
        if doc.metadata and HASH_FIELD in doc.metadata:
            del doc.metadata[HASH_FIELD]

        content = doc.model_dump_json().encode("utf-8")

        # Check exists and whether same.
        exists, same = self.check_same(corpus_key, doc.id, content, doc.metadata)

        def set_metadata():
            sha256_hash = calculate_sha256(content)
            if doc.metadata:
                metadata_copy = dict(doc.metadata)
                metadata_copy[HASH_FIELD] = sha256_hash
                result = doc.copy(update={"metadata": metadata_copy})
            else:
                result = doc.copy(update={"metadata": {HASH_FIELD: sha256_hash}})

            return result

        if exists and same:
            self.logger.info("Document already exists with same hash, skipping")
            return DocOpEnum.IGNORED

        doc = set_metadata()

        if not exists:
            self.logger.info("Document doesnt exist, creating fresh")
            self.documents_client.create(corpus_key, request=doc)
            return DocOpEnum.CREATED

        if exists and not same:
            self.logger.info(f"Document with id [{doc.id}] exists deleting existing and creating fresh (upsert)")
            self.documents_client.delete(corpus_key, doc.id)
            self.documents_client.create(corpus_key, request=doc)
            return DocOpEnum.UPDATED
        else:
            raise Exception("Invalid combination of exists/same, should not get here")









