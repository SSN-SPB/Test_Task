services = ["api", "auth", "db"]


def main():
    test_dict = dict.fromkeys(services, [])
    print(test_dict)
    # each value refers the same object list
    # the modifying one value modifies all
    #               ┌─────────┐
    # api   ───────►│         │
    # auth  ───────►│   []    │
    # db    ───────►│         │
    #               └─────────┘
    test_dict["auth"].append("ok")
    print(test_dict)
    assert test_dict == {"api": ["ok"], "auth": ["ok"], "db": ["ok"]}
    # Solution is: test_dict = {k: [] for k in services}
    test_dict2 = {k: [] for k in services}
    # api   ─────► []
    # auth  ─────► []
    # db    ─────► []
    print(test_dict2)
    test_dict2["db"].append("ok")
    print(test_dict2)


if __name__ == "__main__":
    main()
