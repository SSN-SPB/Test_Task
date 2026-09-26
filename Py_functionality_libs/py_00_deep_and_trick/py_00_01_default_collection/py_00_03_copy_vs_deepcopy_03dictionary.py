# deepcopy() creates a new object and recursively adds
# copies of nested objects found in the original.
# while copy() creates a new object but inserts
# references into it to the objects found in the original.
import copy


def main():
    original = {"key_one": {"limit": 3}}
    copied = copy.copy(original)
    copied["key_one"]["limit"] = 7
    print(original)  # - modified
    assert copied == original
    copied_deep = copy.deepcopy(original)
    copied_deep["key_one"]["limit"] = 9
    print(original)  # - modified
    assert copied == original


if __name__ == "__main__":
    main()