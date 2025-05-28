class Father:
    def hobby(self):
        return "fishing"


class Mother:
    @staticmethod
    def hobby():
        return "gardening"


class Child(Mother, Father):
    pass


child = Child()
print(child.hobby())  # Output: gardening
print(Child.mro())
print(Mother.hobby())
