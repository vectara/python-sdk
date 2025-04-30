import unittest
import os
from pathlib import Path

from vectara import Vectara
from vectara.core import File
from vectara.types import MaxCharsChunkingStrategy, TableExtractionConfig


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

    def test_upload_with_metadata(self):
        """Test file upload with metadata."""
        test_file = self._get_test_file()
        file = (test_file.name, open(test_file, "rb"), "application/pdf")
        
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

    def test_upload_with_chunking(self):
        """Test file upload with custom chunking strategy."""
        test_file = self._get_test_file()
        file = (test_file.name, open(test_file, "rb"), "application/pdf")
        
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

    def test_upload_with_table_extraction(self):
        """Test file upload with table extraction."""
        test_file = self._get_test_file()
        file = (test_file.name, open(test_file, "rb"), "application/pdf")
        
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

    def test_upload_with_all_options(self):
        """Test file upload with all options."""
        test_file = self._get_test_file()
        file = (test_file.name, open(test_file, "rb"), "application/pdf")
        
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


