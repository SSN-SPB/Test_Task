# These patterns help in composing
# classes and objects to form larger structures.

class OldSystem:
    def old_request(self):
        return "Old System Response"

class NewSystemAdapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def new_request(self):
        return self.old_system.old_request()

old = OldSystem()
adapter = NewSystemAdapter(old)
print(adapter.new_request())