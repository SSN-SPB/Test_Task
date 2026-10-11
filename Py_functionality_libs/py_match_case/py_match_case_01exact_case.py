# match case statement is used to check the exact value of the variable
# it is similar to switch case statement in other programming languages
# It is available in python 3.10 and above

def exact_state_checking(status_code_200x):
    match status_code_200x:
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
    exact_state_checking(200)
    exact_state_checking(201)
    exact_state_checking(202)
    exact_state_checking(203)
    exact_state_checking(204)
    exact_state_checking(700)
    exact_state_checking("x")


if __name__ == "__main__":
    main()
