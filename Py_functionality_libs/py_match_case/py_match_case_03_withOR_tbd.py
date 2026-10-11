# match case statement is used to check the exact value of the variable
# it is similar to switch case statement in other programming languages
# It is available in python 3.10 and above

def server_codes_checking(status_code):
    match status_code:
        case 200:
            print("OK")
        case 201:
            print("Created. New source as result")
        case 202:
            print("Accepted. Request has been received but not completed yet")
        case 204:
            print(
                "No Content.The server has fulfilled"
                " the request but does not need to return a response body. "
            )
        case _:
            print("Not known code")


def main():
    server_codes_checking(200)
    server_codes_checking(201)
    server_codes_checking(202)


if __name__ == "__main__":
    main()
