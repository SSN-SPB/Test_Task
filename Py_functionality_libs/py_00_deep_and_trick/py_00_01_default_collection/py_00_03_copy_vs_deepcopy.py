# deepcopy() creates a new object and recursively adds
# copies of nested objects found in the original.
# while copy() creates a new object but inserts
# references into it to the objects found in the original.


import copy

original = [[1, 2], [3, 4]]
original2 = [[1, 2], [3, 4]]

copied = copy.copy(original)
deep_copied = copy.deepcopy(original2)

copied[0][0] = 99
deep_copied[0][0] = 97

print(
    original
)  # [[99, 2], [3, 4]] original is changed because copied is a shallow copy
print(copied)  # [[99, 2], [3, 4]]
print(
    original2
)  # [[1, 2], [3, 4]] original2 is not changed because of it is a deep copy
print(deep_copied)  # [[97, 2], [3, 4]]
