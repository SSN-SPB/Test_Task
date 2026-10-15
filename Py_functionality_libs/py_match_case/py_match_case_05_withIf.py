# code_of_response in code below receives the value
# of response_code and then checks if it falls within
# the specified ranges for each case. If it does, it prints
# the corresponding message and returns a string indicating
# the checked code. If none of the cases match, it falls to
# the default case and prints "Code is not known" along with the checked code.


def match_case_with_if(response_code):
    match response_code:
        case code_of_response if 200 <= code_of_response < 300:
            print("Successful response")
            return f"Checked code: {code_of_response}"

        case code_of_response if 300 <= code_of_response < 400:
            print("Redirect")
            return f"Checked code: {code_of_response}"

        case code_of_response if 400 <= code_of_response < 500:
            print("Client errors")
            return f"Checked code: {code_of_response}"

        case code_of_response if 500 <= code_of_response:
            print("Server error")
            return f"Checked code: {code_of_response}"

        case _:
            print("Code is not known")
            return f"Checked code: {code_of_response}"


def main():
    print(match_case_with_if(201))
    print(match_case_with_if(300))
    print(match_case_with_if(404))
    print(match_case_with_if(510))
    print(match_case_with_if(50))
    match_case_with_if(201)  # Success: 201
    match_case_with_if(404)  # Client error: 404
    match_case_with_if(503)


if __name__ == "__main__":
    main()
