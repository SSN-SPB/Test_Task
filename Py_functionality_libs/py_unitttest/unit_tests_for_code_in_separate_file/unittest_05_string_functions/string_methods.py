def method_explanation(func):
    def wrapper(to_check):
        print(
            f"Perform function {func.__name__} for argument: '{to_check}'"
        )
        return func(to_check)

    return wrapper


@method_explanation
def define_string_length(test_string: str):
    return len(test_string)


def main():
    result = define_string_length("Hello")
    print(result)


if __name__ == "__main__":
    main()
