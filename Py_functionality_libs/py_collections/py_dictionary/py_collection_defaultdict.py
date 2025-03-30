from collections import defaultdict


def default_dif_factory():
    return "default"


d1 = defaultdict(default_dif_factory)
d1[1] = "one"
d1[2] = " two"

print(d1[1])
print(d1)
print(d1[2])


grouped_items = defaultdict(list)
print(dict(grouped_items))

# Sample data: list of tuples (category, item)
items = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'orange'), ('vegetable', 'spinach')]

# Group items by category
for category, item in items:
    grouped_items[category].append(item)

# Print the grouped items
print(dict(grouped_items))