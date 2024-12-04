import unittest

from vectara import FilterAttribute
from vectara.factory import Factory


class TestJobsManager(unittest.TestCase):
    def setUp(self):
        self.client = Factory().build()
        self.client.corpora.create(key="test-reset-filters")
        filter_attributes = FilterAttribute(
            name="Title",
            level="document",
            description="The title of the document.",
            indexed=True,
            type="text"
        )
        res = self.client.corpora.replace_filter_attributes("test-reset-filters", filter_attributes=[filter_attributes])

        self.job_id = res.job_id

    def test_get_job(self):
        res = self.client.jobs.get(job_id=self.job_id)

        self.assertEqual(res.id, self.job_id)
        self.assertEqual(res.corpus_keys, ["test-reset-filters"])

    def test_list_jobs(self):
        for job in self.client.jobs.list():
            self.assertIsNotNone(job.id)

    def cleanup(self):
        for corpora in self.client.corpora.list():
            self.client.corpora.delete(corpora.key)

    def tearDown(self):
        for corpora in self.client.corpora.list():
            self.client.corpora.delete(corpora.key)
