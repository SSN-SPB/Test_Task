def main():
    http_code = 401
    match http_code:
        case 200 | 201:
            print("OK")
            # do_something_good()
        case 401 | 402 | 403 | 404:
            print("Client error")
            # do_something()
        case 501 | 502 | 503:
            print("Server Error")
            # do_something_with_server()
        case _:
            print("Code not found")


if __name__ == "__main__":
    main()
