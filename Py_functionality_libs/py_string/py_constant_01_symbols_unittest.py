import string
import unittest


class StingPunctuation(unittest.TestCase):
    def test_string_punctuation(self):
        received = string.punctuation
        self.assertEqual(received, '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')


if __name__ == '__main__':
    unittest.main()
