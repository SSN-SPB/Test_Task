# difflib is a module in Python's standard library
# that provides classes and functions for comparing sequences,
# including strings, lists, and other iterable objects.
# It is commonly used for tasks such as
# finding differences between files, generating diffs,
# and performing approximate string matching.
import difflib
import logging

logger = logging.getLogger(__name__)


text1 = """
This is the first line.
This is the second line.
This is the third line.
"""

text2 = """
This is the first line.
This is the modified second line.
This is the fourth line.
"""


def difflib_unified_diff(text_one: str, text_two: str):
    diff = difflib.unified_diff(text_one.splitlines(), text_two.splitlines())

    logger.info("\n".join(diff))


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(funcName)s:%(lineno)d - %(message)s"
    )
    difflib_unified_diff(text1, text2)
