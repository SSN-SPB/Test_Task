def main():
    http_code = 500
    code_OK = [200, 201, 209]
    code_client_errors = [400, 401, 404, 409]
    code_server_errors = [500, 501, 503]
    match http_code:
        case http_code if http_code in code_OK:
            print("OK")
            # do_something_good()
        case http_code if http_code in code_client_errors:
            print("Client error")
            # do_something()
        case http_code if http_code in code_server_errors:
            print("Server error")
            # do_something_with_server()
        case _:
            print("Code not found")


if __name__ == "__main__":
    main()
