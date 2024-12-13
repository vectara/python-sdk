from vectara.utils.hash import calculate_sha256
import unittest




class HashTest(unittest.TestCase):


    def test_hash(self):
        content = "This is my content"
        expected_sha256_hash = "ee302829a269d5db4b10188b2d006e4c8bb639b25d73b92db3944ec5faddd40d"

        byte_content = content.encode()
        found_sha256_hash = calculate_sha256(byte_content)

        self.assertEqual(expected_sha256_hash, found_sha256_hash, "The hashes were not the same")  # add assertion here


if __name__ == '__main__':
    unittest.main()
