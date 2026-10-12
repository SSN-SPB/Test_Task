def define_api_responses(api_response):
    match api_response:
        case 200 | 201 | 203 | 204 | 205:
            print("Successful response")
        case 300 | 301 | 303 | 304 | 305:
            print("Redirect")
        case 400 | 401 | 403 | 404 | 405:
            print("Client error")
        case 500 | 501 | 503 | 504 | 505:
            print("Server error")
        case _:
            print("Unknown code")


def main():
    define_api_responses(201)
    define_api_responses(301)
    define_api_responses(401)
    define_api_responses(501)
    define_api_responses(601)


if __name__ == "__main__":
    main()
