"""Suite demonstrates inheritance in oop Python"""

# Inheritance is a fundamental concept in object-oriented programming (OOP)
# that allows a new class (called a child or subclass) to inherit attributes and methods
# from an existing class (called a parent or superclass).
# This promotes code reusability and establishes a natural hierarchical relationship between classes.
# In Python, inheritance is implemented by defining
# a new class that specifies the parent class in parentheses after the class name.


class BaseClass:
    """
    Base test class that provides common setup and teardown functionality.
    This class serves as a parent class for all test cases.
    """

    def __init__(self) -> None:
        """Initialize the base test class."""
        self.test_name = self.__class__.__name__
        self.is_setup = False

    def setup(self) -> None:
        """Set up common test environment and resources."""
        print(f"from BaseClass setup {self}")
        print("make setup base")
        self.is_setup = True

    def teardown(self) -> None:
        """Clean up after test execution."""
        print(f"from BaseClass teardown {self.__class__.__name__}")
        print("cleanup base resources")
        self.is_setup = False


class LoginTest(BaseClass):
    """
    Test class for login functionality.
    Inherits from BaseClass and demonstrates method overriding.
    """

    def __init__(self) -> None:
        """Initialize LoginTest with parent class initialization."""
        print(f"activate {self.__class__.__name__}")
        super().__init__()
        self.login_user = None

    def run(self) -> None:
        """Execute the login test."""
        print(self)
        print("make run login")

    def setup(self) -> None:
        """
        Set up login test environment.
        Calls parent setup and adds login-specific setup.
        """
        print(f"from LoginTest setup {self.__class__.__name__}")
        super().setup()  # Call parent class setup
        print("make setup login and override the base class")
        self.login_user = "test_user"

    def teardown(self) -> None:
        """Clean up login test resources."""
        print(f"from LoginTest teardown")
        self.login_user = None
        super().teardown()  # Call parent class teardown


class BuyTest(BaseClass):
    """
    Test class for purchase functionality.
    Inherits from BaseClass and uses inherited setup/teardown.
    """

    def __init__(self) -> None:
        """Initialize BuyTest with parent class initialization."""
        print(f"activate {self.__class__.__name__}")
        super().__init__()
        self.purchase_amount = 0.0

    def run(self) -> None:
        """Execute the purchase test."""
        print("make run buy")

    def setup(self) -> None:
        """Set up purchase test environment."""
        super().setup()  # Call parent class setup
        self.purchase_amount = 99.99
        print(f"Purchase test setup: amount initialized to {self.purchase_amount}")


def main() -> None:
    """
    Main function demonstrating inheritance and polymorphism.
    Creates instances of derived classes and executes their lifecycle methods.
    """
    print("=" * 50)
    print("Starting test suite")
    print("=" * 50)

    # Create instances of test classes
    bt_test = BuyTest()
    lt_test = LoginTest()

    print("\n--- Login Test Lifecycle ---")
    lt_test.setup()
    lt_test.run()
    lt_test.teardown()

    print("\n--- Buy Test Lifecycle ---")
    bt_test.setup()
    bt_test.run()
    bt_test.teardown()

    print("\n" + "=" * 50)
    print("Test suite completed")
    print("=" * 50)


if __name__ == "__main__":
    main()
