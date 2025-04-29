import unittest
import os

from vectara import Vectara, FilterAttribute


class TestJobsManager(unittest.TestCase):
    client = None
    corpus_key = None
    job_id = None
    created_corpora = None

    @classmethod
    def setUpClass(cls):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        
        cls.client = Vectara(api_key=api_key)
        cls.created_corpora = set()

        # Create test corpus
        cls.corpus_key = "test-jobs"
        cls.client.corpora.create(key=cls.corpus_key)
        cls.created_corpora.add(cls.corpus_key)

        # Setup filter attributes
        filter_attributes = FilterAttribute(
            name="Title",
            level="document",
            description="The title of the document.",
            indexed=True,
            type="text"
        )
        res = cls.client.corpora.replace_filter_attributes(
            cls.corpus_key,
            filter_attributes=[filter_attributes]
        )
        cls.job_id = res.job_id

    def test_get_job(self):
        res = self.client.jobs.get(job_id=self.job_id)
        self.assertEqual(res.id, self.job_id)
        self.assertEqual(res.corpus_keys, [self.corpus_key])

    def test_list_jobs(self):
        found_job = False
        jobs_list = self.client.jobs.list(corpus_key=self.corpus_key)
        
        for job in jobs_list.items:
            if job.id == self.job_id:
                found_job = True
                break
        
        self.assertTrue(found_job)

    @classmethod
    def tearDownClass(cls):
        """Clean up all test resources."""
        for corpus_key in cls.created_corpora:
            try:
                cls.client.corpora.delete(corpus_key)
            except Exception:
                pass
