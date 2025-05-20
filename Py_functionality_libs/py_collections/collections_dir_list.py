def main():
    list1 = [0, 1]
    list1.append("x")
    print(list1)  # [0, 1, 'x']
    print("Dir of list class")
    print(dir(list))
    print("Dir of list object")
    print(dir(list1))
    a = 5
    print("Dir of int")
    print(dir(a))


if __name__ == "__main__":
    main()
