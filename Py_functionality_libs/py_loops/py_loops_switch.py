def main():
    http_code = "418"
    match http_code:
        case "200":
            print("OK")
            # do_something_good()
        case "404":
            print("Not Found")
            # do_something_bad()
        case "418":
            print("I'm a teapot")
            # make_coffee()
        case _:
            print("Code not found")


if __name__ == "__main__":
    main()
