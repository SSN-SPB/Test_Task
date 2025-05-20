# collection
import collections


def main():
    count = collections.Counter(["a", "b"])
    print(count)
    assert count == ({"a": 1, "b": 1})
    baseline = {"music": "bach", "art": "rembrandt"}
    adjustments = {"art": "van gogh", "opera": "carmen"}
    t1 = list(collections.ChainMap(adjustments, baseline))
    t2 = list(collections.ChainMap(baseline))
    print(t1)
    print(t2)


if __name__ == "__main__":
    main()
