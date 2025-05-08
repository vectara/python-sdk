import unittest
import os
import time
import functools
from pathlib import Path

from vectara import Vectara
from vectara.core import File
from vectara.types import MaxCharsChunkingStrategy, TableExtractionConfig
import httpx


def retry_on_exception(max_retries=3, retry_delay=10):
    """
    Decorator to retry a test if it fails with an exception.
    
    Parameters:
    - max_retries: Maximum number of retry attempts
    - retry_delay: Delay in seconds between retries
    
    Before retrying, it will attempt to delete any previously uploaded file.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            last_exception = None
            
            test_name = func.__name__
            filename = None
            
            if "metadata" in test_name:
                filename = "test_document_with_metadata.pdf"
            elif "chunking" in test_name and "larger" in test_name:
                filename = "test_document_with_larger_chunks.pdf"
            elif "chunking" in test_name:
                filename = "test_document_with_chunking.pdf"
            elif "table" in test_name:
                filename = "test_document_with_table_extraction.pdf"
            elif "all_options" in test_name:
                filename = "test_document_with_all_options.pdf"
            
            doc_id = filename if filename else None
            
            for attempt in range(max_retries):
                try:
                    # For retry attempts, try to delete any existing document first
                    if attempt > 0 and doc_id and hasattr(self, 'client') and hasattr(self, 'corpus'):
                        try:
                            self.client.documents.delete(
                                corpus_key=self.corpus.key,
                                document_id=doc_id
                            )
                        except Exception:
                            pass
                    
                    # Attempt the test
                    return func(self, *args, **kwargs)
                    
                except (httpx.ReadTimeout, httpx.ConnectTimeout, httpx.TimeoutException, Exception) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
            
            # Re-raise the last exception if all retries failed
            if last_exception:
                raise last_exception
                
        return wrapper
    return decorator


class UploadManagerTest(unittest.TestCase):
    client = None
    corpus = None

    @classmethod
    def setUpClass(cls):
        # Setup client
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        
        cls.client = Vectara(api_key=api_key)
        
        response = cls.client.corpora.create(key="test-upload", name="test-upload")
        cls.corpus = response

    def _get_test_file(self):
        """Helper method to get the test file path."""
        test_file = Path("examples/01_getting_started/resources/arxiv/2409.05866v1.pdf")
        if not test_file.exists():
            raise FileNotFoundError(f"Test file not found: {test_file}")
        return test_file

    @retry_on_exception(max_retries=3, retry_delay=10)
    def test_upload_with_metadata(self):
        """Test file upload with metadata."""
        test_file = self._get_test_file()
        
        with open(test_file, "rb") as file_content:
            file = (test_file.name, file_content, "application/pdf")
            
            document = self.client.upload.file(
                corpus_key=self.corpus.key,
                file=file,
                metadata={"key": "value", "test": True},
                filename="test_document_with_metadata.pdf",
                request_timeout=600  # 10 minutes timeout
            )
            
            # Verify upload
            self.assertIsNotNone(document)
            self.assertGreater(document.storage_usage.bytes_used, 0)
            self.assertGreater(document.storage_usage.metadata_bytes_used, 0)

    @retry_on_exception(max_retries=3, retry_delay=10)
    def test_upload_with_chunking(self):
        """Test file upload with custom chunking strategy."""
        test_file = self._get_test_file()
        
        with open(test_file, "rb") as file_content:
            file = (test_file.name, file_content, "application/pdf")
            
            chunking_strategy = MaxCharsChunkingStrategy(
                type="max_chars_chunking_strategy",
                max_chars_per_chunk=200
            )
            
            document = self.client.upload.file(
                corpus_key=self.corpus.key,
                file=file,
                chunking_strategy=chunking_strategy,
                filename="test_document_with_chunking.pdf",
                request_timeout=600  # 10 minutes timeout
            )
            
            # Verify upload
            self.assertIsNotNone(document)
            self.assertGreater(document.storage_usage.bytes_used, 0)

    @retry_on_exception(max_retries=3, retry_delay=10)
    def test_upload_with_larger_chunking(self):
        """Test file upload with larger chunk size."""
        test_file = self._get_test_file()
        
        with open(test_file, "rb") as file_content:
            file = (test_file.name, file_content, "application/pdf")
            
            chunking_strategy = MaxCharsChunkingStrategy(
                type="max_chars_chunking_strategy",
                max_chars_per_chunk=1024
            )
            
            document = self.client.upload.file(
                corpus_key=self.corpus.key,
                file=file,
                chunking_strategy=chunking_strategy,
                filename="test_document_with_larger_chunks.pdf",
                request_timeout=600
            )
            
            # Verify upload
            self.assertIsNotNone(document)
            self.assertGreater(document.storage_usage.bytes_used, 0)

    @retry_on_exception(max_retries=3, retry_delay=10)
    def test_upload_with_table_extraction(self):
        """Test file upload with table extraction."""
        test_file = self._get_test_file()
        
        with open(test_file, "rb") as file_content:
            file = (test_file.name, file_content, "application/pdf")
            
            table_config = TableExtractionConfig(extract_tables=True)
            
            document = self.client.upload.file(
                corpus_key=self.corpus.key,
                file=file,
                table_extraction_config=table_config,
                filename="test_document_with_table_extraction.pdf",
                request_timeout=600  # 10 minutes timeout
            )
            
            # Verify upload
            self.assertIsNotNone(document)
            self.assertGreater(document.storage_usage.bytes_used, 0)

    @retry_on_exception(max_retries=3, retry_delay=30)
    def test_upload_with_all_options(self):
        """Test file upload with all options."""
        test_file = self._get_test_file()
        
        with open(test_file, "rb") as file_content:
            file = (test_file.name, file_content, "application/pdf")
            
            chunking_strategy = MaxCharsChunkingStrategy(
                type="max_chars_chunking_strategy",
                max_chars_per_chunk=200
            )
            
            table_config = TableExtractionConfig(extract_tables=True)
            
            document = self.client.upload.file(
                corpus_key=self.corpus.key,
                file=file,
                metadata={"key": "value", "test": True},
                chunking_strategy=chunking_strategy,
                table_extraction_config=table_config,
                filename="test_document_with_all_options.pdf",
                request_timeout=600  # 10 minutes timeout
            )
            
            # Verify upload
            self.assertIsNotNone(document)
            self.assertGreater(document.storage_usage.bytes_used, 0)
            self.assertGreater(document.storage_usage.metadata_bytes_used, 0)

    @classmethod
    def tearDownClass(cls):
        """Clean up test resources."""
        # Delete the test corpus
        try:
            cls.client.corpora.delete(cls.corpus.key)
        except Exception:
            pass
        