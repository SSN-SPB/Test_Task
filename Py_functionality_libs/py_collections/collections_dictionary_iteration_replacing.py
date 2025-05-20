# dictionary
# creating dictionary via {} or dict(...)
# setdefault - add value if key is not found or returns existing value
# iteration - via 'key, value in dictionary.items()'


def main():
    # create dictionary
    e2f = dict(dog="chien", cat="chat")
    print(e2f.setdefault("walrus", "morse"))  # zval
    print("En2Fr dict is: {}".format(e2f))
    f2e = {}
    # En2Fr dict is: {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
    # iteration
    for ekey, evalue in e2f.items():
        f2e[evalue] = ekey
    print("Fr2En dict is: {}".format(f2e))
    # Fr2En dict is: {'chien': 'dog', 'chat': 'cat', 'morse': 'walrus'}


if __name__ == "__main__":
    main()
