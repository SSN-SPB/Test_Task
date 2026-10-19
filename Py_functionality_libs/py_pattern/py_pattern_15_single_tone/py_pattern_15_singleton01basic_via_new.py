class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


def main():
    obj1 = Singleton()
    obj2 = Singleton()
    print(f"if obj1 is obj2: {obj2 is obj1}")


if __name__ == "__main__":
    main()
