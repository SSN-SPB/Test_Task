# This python code demonstrates the behavior of try-finally blocks in Python,
# return in finally block hides Exception


def return_in_finally():
    print("outside exception")
    try:
        print("inside try")
        raise TimeoutError("service not available")
    finally:
        print("inside finally")
        return "returned string"


def return_outside_finally():
    print(f"run method: {return_outside_finally.__name__}")
    try:
        print("inside try")
        raise TimeoutError("service not available")
    finally:
        print("inside finally")
    return "returned string outside finally"


def main() -> None:
    print(return_in_finally())
    print(return_outside_finally())


if __name__ == "__main__":
    main()
