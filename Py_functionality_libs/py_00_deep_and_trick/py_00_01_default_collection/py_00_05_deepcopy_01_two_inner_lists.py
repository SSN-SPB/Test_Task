import copy

inner_list = [1]
source_list = [inner_list, inner_list]


def main():
    print(f"initial source: {source_list}")
    deep_copy_source = copy.deepcopy(source_list)
    inner_list.append("a")
    print(f"the source with modified inner: {source_list}")
    print(f"the deepcopy with modified inner: {deep_copy_source}")
    assert source_list == [[1, "a"], [1, "a"]]
    assert deep_copy_source == [[1], [1]]


if __name__ == "__main__":
    main()
