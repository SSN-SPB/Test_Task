import uuid
import sys

namespace1 = uuid.NAMESPACE_DNS
print(sys.getrefcount(namespace1))
namespace12 = namespace1
name = "example.com"


def main():
    """sys.getrefcount(object) allows getting number of links to object"""
    print(sys.getrefcount(namespace1))
    namespace13 = namespace1
    print(sys.getrefcount(namespace1))
    print(namespace13)
    print(namespace1)
    print(sys.getrefcount(namespace1))


if __name__ == "__main__":
    main()
