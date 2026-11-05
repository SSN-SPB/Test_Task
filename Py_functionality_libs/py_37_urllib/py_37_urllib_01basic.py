from urllib.parse import urljoin


def main():
    base = "http://example.com/api/"

    assert urljoin(base, "users") == "http://example.com/api/users"
    assert urljoin(base, "/users") == "http://example.com/users"


if __name__ == "__main__":
    main()
