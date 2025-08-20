"""
automatically provides a
default value for missing keys,
instead of raising a KeyError.
"""

from collections import defaultdict

grouped_dictionary = defaultdict(int)


def main():
    print(f"default_dict {grouped_dictionary}")
    grouped_dictionary["new"] = []
    print(f"updated {grouped_dictionary}")


if __name__ == "__main__":
    main()
