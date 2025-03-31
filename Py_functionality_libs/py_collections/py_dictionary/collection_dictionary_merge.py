dict_one = {1: "a", 2: "b"}
dict_two = {3: "c", 4: "d"}
print(dict_one[1])
print(dict_two[3])
dict_tree = {**dict_two, **dict_one}

print(dict_tree[1])
for k, v in dict_tree.items():
    print(f"{k}: {v} value")
