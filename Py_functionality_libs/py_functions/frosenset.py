animals = frozenset(["dog", "cat", "mouse"])
jard_animals = {"pig", "cow", "horse"}
jard_animals.add("goat")
print(jard_animals)
try:
    animals.add("frog")
except AttributeError as ae:
    print(ae)
