# Template strings are a simpler and less powerful
# alternative to regular string formatting.
# They use placeholders in the form of $identifier,
# which can be replaced with values using the substitute() method.
# Template strings are useful when you want to create strings
# that will be used as templates for generating other strings,
# especially when the template is
# user-defined or comes from an external source.
from string import Template


string_template = Template("Hello $name! Welcome to $area!")


def main():
    final_string = string_template.substitute(area="our city", name="John")
    print(final_string)  # Hello John! Welcome to our city!


if __name__ == "__main__":
    main()
