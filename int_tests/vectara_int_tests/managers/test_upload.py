import unittest
import os
from pathlib import Path

from vectara import Vectara
from vectara.core import File
from vectara.types import MaxCharsChunkingStrategy, TableExtractionConfig


class UploadManagerTest(unittest.TestCase):
    client = None
    created_corpora = None

    @classmethod
    def setUpClass(cls):
        # Setup client
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        
        cls.client = Vectara(api_key=api_key)
        cls.created_corpora = set()

    def _create_test_corpus(self, name_suffix=""):
        """Helper method to create a test corpus."""
        name = f"int-test-upload-{name_suffix}" if name_suffix else "int-test-upload"
        key = name  # Using same value for key for simplicity
        
        response = self.client.corpora.create(key=key, name=name)
        self.created_corpora.add(response.key)
        return response

    def _get_test_file(self):
        """Helper method to get the test file path."""
        test_file = Path("examples/01_getting_started/resources/arxiv/2409.05866v1.pdf")
        if not test_file.exists():
            raise FileNotFoundError(f"Test file not found: {test_file}")
        return test_file

    def test_upload_with_metadata(self):
        """Test file upload with metadata."""
        # Create test corpus
        corpus = self._create_test_corpus("metadata")
        
        # Upload file with metadata
        test_file = self._get_test_file()
        file = File(path=test_file)
        
        document = self.client.upload.file(
            corpus_key=corpus.key,
            file=file,
            metadata={"key": "value", "test": True},
            filename="test_document.pdf"
        )
        
        # Verify upload
        self.assertIsNotNone(document)
        self.assertGreater(document.storage_usage.bytes_used, 0)
        self.assertGreater(document.storage_usage.metadata_bytes_used, 0)

    def test_upload_with_chunking(self):
        """Test file upload with custom chunking strategy."""
        # Create test corpus
        corpus = self._create_test_corpus("chunking")
        
        # Upload file with chunking strategy
        test_file = self._get_test_file()
        file = File(path=test_file)
        
        chunking_strategy = MaxCharsChunkingStrategy(
            type="max_chars_chunking_strategy",
            max_chars_per_chunk=200
        )
        
        document = self.client.upload.file(
            corpus_key=corpus.key,
            file=file,
            chunking_strategy=chunking_strategy
        )
        
        # Verify upload
        self.assertIsNotNone(document)
        self.assertGreater(document.storage_usage.bytes_used, 0)

    def test_upload_with_table_extraction(self):
        """Test file upload with table extraction."""
        # Create test corpus
        corpus = self._create_test_corpus("tables")
        
        # Upload file with table extraction
        test_file = self._get_test_file()
        file = File(path=test_file)
        
        table_config = TableExtractionConfig(extract_tables=True)
        
        document = self.client.upload.file(
            corpus_key=corpus.key,
            file=file,
            table_extraction_config=table_config
        )
        
        # Verify upload
        self.assertIsNotNone(document)
        self.assertGreater(document.storage_usage.bytes_used, 0)

    def test_upload_with_all_options(self):
        """Test file upload with all options."""
        # Create test corpus
        corpus = self._create_test_corpus("all_options")
        
        # Upload file with all options
        test_file = self._get_test_file()
        file = File(path=test_file)
        
        chunking_strategy = MaxCharsChunkingStrategy(
            type="max_chars_chunking_strategy",
            max_chars_per_chunk=200
        )
        
        table_config = TableExtractionConfig(extract_tables=True)
        
        document = self.client.upload.file(
            corpus_key=corpus.key,
            file=file,
            metadata={"key": "value", "test": True},
            chunking_strategy=chunking_strategy,
            table_extraction_config=table_config,
            filename="test_document.pdf"
        )
        
        # Verify upload
        self.assertIsNotNone(document)
        self.assertGreater(document.storage_usage.bytes_used, 0)
        self.assertGreater(document.storage_usage.metadata_bytes_used, 0)

    @classmethod
    def tearDownClass(cls):
        """Clean up all test resources."""
        # Delete all created corpora
        for corpus_key in cls.created_corpora:
            try:
                cls.client.corpora.delete(corpus_key)
            except Exception:
                pass


