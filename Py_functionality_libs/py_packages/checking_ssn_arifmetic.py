import ssn

# imported from C:\Users\Sergei_Smirnov\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\ssn


def main():
    print("Hello")
    sum_function(1, 3, "Test")


def sum_function(
    x,
    y,
    message,
):
    result = int(x) + int(y)
    print("Sum of {} and {} is {}.The message is: {}".format(x, y, result, message))
    return result


if __name__ == "__main__":
    main()
