"""argv: By default, sys.argv is used, which allows command-line arguments
to be passed. You can override it if needed.

verbosity: Controls the level of detail in the test output. For example,
verbosity=2 provides more detailed output.

exit: If True (default), the script will exit after running the tests.
If False, the script continues running, which is useful
 in interactive sessions."""

import unittest


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
