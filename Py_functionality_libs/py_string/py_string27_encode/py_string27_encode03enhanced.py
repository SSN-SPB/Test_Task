def main():
    test_string = "приветст"
    expected_text = b"\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82"
    encoded_test = test_string.encode()
    print(f" encoded_text: {encoded_test}")
    print(f" length of encoded_text: {len(encoded_test)}")
    assert encoded_test == expected_text


if __name__ == "__main__":
    main()
