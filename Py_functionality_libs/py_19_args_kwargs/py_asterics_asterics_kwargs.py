def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def order_summary(item, quantity, **kwargs):
    print(f"Order: {quantity} x {item}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


def main():
    print(" Basic Example")
    greet(name="Alice", age=30, city="New York")

    print(" Practical Example: Formatting User Profiles")
    order_summary("Laptop", 2, color="Silver", warranty="2 years", delivery="Express")

    # Passing **kwargs to Another Function
    print("Passing **kwargs to Another Function")

    def display_info(name, age, city):
        print(f"{name} is {age} years old and lives in {city}.")

    def process_data(**kwargs):
        display_info(**kwargs)  # Unpacking kwargs

    process_data(name="Emma", age=28, city="London")


if __name__ == "__main__":
    main()
