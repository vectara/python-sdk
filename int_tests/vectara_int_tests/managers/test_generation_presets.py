import unittest

from vectara.factory import Factory


class TestGenerationPresetsManager(unittest.TestCase):
    def setUp(self):
        self.client = Factory().build()

    def test_list_generation_presets(self):
        response = self.client.generation_presets.list_generation_presets()
        for gp in response.generation_presets:
            self.assertIsNotNone(gp.name)
