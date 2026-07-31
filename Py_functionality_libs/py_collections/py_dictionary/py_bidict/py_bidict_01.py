from bidict import bidict

# pip install bidict

people = bidict(name="Tom", age=37, city="New York")


def kernel():
    print(f"dict age {people['age']}")
    print(people.inv[37])
    for k, v in people.inv.items():
        print(f"inverted: key {k}, value: {v}")


if __name__ == "__main__":
    kernel()
