# Define a cache to store previous computations
cache = {}


def square(n):
    # Check if the result is already in the cache
    if n in cache:
        print(f"Returning cached result for {n}")
        return cache[n]
    else:
        # Compute the square and store it in the cache
        result = n * n
        cache[n] = result
        print(f"Computed and cached the result for {n}")
        return result


def main():
    while True:
        input_value = input("Enter a number to square (or 'exit' to quit): ")

        if input_value.lower() == "exit":
            print("Exiting the program.")
            break

        try:
            num = int(input_value)
            result = square(num)
            print(f"The square of {num} is {result}")
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
