import uuid

namespace = uuid.NAMESPACE_DNS
namespace2 = uuid.NAMESPACE_URL
name = "example.com"


def main():
    print(uuid.uuid4())
    print(uuid.uuid3(namespace, name))
    print(uuid.uuid3(namespace2, name))
    # uuid3 is always the same
    assert uuid.uuid3(namespace, name) == uuid.uuid3(namespace, name)
    test_value = uuid.uuid3(namespace, name)
    assert str(test_value) == "9073926b-929f-31c2-abc9-fad77ae3e8eb"


if __name__ == "__main__":
    main()
