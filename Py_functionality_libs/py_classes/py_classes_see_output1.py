class Counter:
    @staticmethod
    def static_method():
        return "Static Method1"  # Static Method1

    @classmethod
    def class_method(cls):
        return f"Class Method from {cls.__name__}"  # Class Method from Counter


def main():
    print(Counter.static_method())
    print(Counter.class_method())


if __name__ == "__main__":
    main()
