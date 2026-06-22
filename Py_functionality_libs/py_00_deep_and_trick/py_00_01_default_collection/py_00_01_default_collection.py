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


def add_item_none(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(add_item_none(1))  # [1]
print(add_item_none(2))  # [2] - This is because a new list
# is created each time the function is called with the default value of None.
