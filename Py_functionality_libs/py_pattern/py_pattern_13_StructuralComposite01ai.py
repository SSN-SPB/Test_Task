# Treats individual objects and compositions of objects uniformly.
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        return " + ".join([child.operation() for child in self.children])

leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
print(composite.operation())  # Output: Leaf + Leaf
composite.add(leaf2)
print(composite.operation())