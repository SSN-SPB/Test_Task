"""Suit for demo of itertools.premutations() - creates an iterator that returns
the list of tuples with all possible combinations of the input elements,
with the specified length (default is the length of the iterable)."""

from itertools import permutations


list_of_words = ["cat", "dog", "mouse"]
expected_combinations = [
    ("cat", "dog", "mouse"),
    ("cat", "mouse", "dog"),
    ("dog", "cat", "mouse"),
    ("dog", "mouse", "cat"),
    ("mouse", "cat", "dog"),
    ("mouse", "dog", "cat"),
]


def find_all_combinations(words):
    """
    :type words: List[str]
    :rtype: List[tuple]
    """
    return list(permutations(words))


def main():
    print(f"The list of combinations: {find_all_combinations(list_of_words)}")
    assert find_all_combinations(list_of_words) == expected_combinations


if __name__ == "__main__":
    main()
