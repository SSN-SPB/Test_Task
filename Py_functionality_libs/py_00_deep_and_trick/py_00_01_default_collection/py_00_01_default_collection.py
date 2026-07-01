# default mutable arguments in Python
# can lead to unexpected behavior because
# the default value is evaluated only once
# when the function is defined, not each time
# the function is called.
# This means that if you use a mutable default
# argument (like a list or dictionary),
# it will retain its state across multiple calls to the function.


def add_item(item, items=[]):
    items.append(item)
    return items


print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - This is because
# the default list is mutable and retains its state across function calls.
print(add_item(7, items=[10, 20]))  # [10, 20, 7] - This is because
# a new list is provided as an argument, so the default list is not used.
print(add_item(9))  # [1, 2, 9]
print(add_item(9, items=[10, 20]))  # [10, 20, 9]
print(add_item(9))  # [1, 2, 9, 9]
c = add_item(33, items=[11, 31])
print(c)  #

d = add_item(35, items=[11, 31])
print(d)  # [11, 31, 35]
print(add_item(37, items=[11, 31]))  # [11, 31, 37]
print(add_item(39, items=[11, 31]))  # [11, 31, 39]


def add_item_none(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(add_item_none(1))  # [1]
print(add_item_none(2))  # [2] - This is because a new list
# is created each time the function is called with the default value of None.
print(add_item_none(37, items=[11, 31]))  # [11, 31, 37]
print(add_item_none(39, items=[11, 31]))  # [11, 31, 39]
print(add_item_none(37))  # [1]
