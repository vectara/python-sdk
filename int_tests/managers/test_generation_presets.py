import unittest
import os

from vectara import Vectara


class TestGenerationPresetsManager(unittest.TestCase):
    def setUp(self):
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY not found in environment variables or .env file")
        self.client = Vectara(api_key=api_key)

    def test_list_generation_presets(self):
        # Test with default parameters
        found_presets = set()
        pager = self.client.generation_presets.list()
        for preset in pager.items:
            self.assertIsNotNone(preset.name)
            found_presets.add(preset.name)

        # Test with limit parameter
        limited_pager = self.client.generation_presets.list(limit=2)
        self.assertLessEqual(len(limited_pager.items), 2)

        # Test with llm_name filter
        llm_pager = self.client.generation_presets.list(llm_name="gpt-3.5-turbo")
        for preset in llm_pager.items:
            self.assertEqual(preset.llm_name, "gpt-3.5-turbo")
