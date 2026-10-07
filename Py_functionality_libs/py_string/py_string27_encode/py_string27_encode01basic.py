def main():
    test_string = "Terve"
    expected_text = b"Terve"
    encoded_test = test_string.encode("utf-8")
    print(f" encoded_text: {encoded_test}")
    assert encoded_test == expected_text


if __name__ == "__main__":
    main()
