# collection
from collections import namedtuple

# Define a named tuple type called 'Person'
Person = namedtuple("Person", ["name", "age", "city"])


def main():
    # Create an instance of the named tuple
    person1 = Person(name="Alice", age=30, city="New York")
    person2 = Person(name="Bob", age=25, city="Los Angeles")

    # Accessing the values using named fields
    print(f"{person1.name} is {person1.age} y.o. and lives in {person1.city}.")
    print(f"{person2.name} is {person2.age} y.o. and lives in {person2.city}.")

    # Accessing the values using index (just like a regular tuple)
    print(f"{person1[0]} is {person1[1]} years old and lives in {person1[2]}.")
    print(f"{person2[0]} is {person2[1]} years old and lives in {person2[2]}.")

    # Unpacking the named tuple
    name, age, city = person1
    print(f"{name} is {age} years old and lives in {city}.")


if __name__ == "__main__":
    main()
