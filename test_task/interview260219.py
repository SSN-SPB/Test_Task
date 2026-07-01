list_of_numbers = [2, 3, 2, 3, 5, 3]
list_of_numbers2 = [2, 3, 2, 3, 5, 3]

def main():
    result = 0
    c = 0
    for x in list_of_numbers:
        if list_of_numbers.index(x) == c:
            result += 1
        c += 1
    print(f"Total number of unique elements is: {result}")
    # second solution with updating list
    w = 0
    for y in list_of_numbers2:
        if list_of_numbers2.index(y) != w:
            list_of_numbers2.remove(y) # removing element from list if it is not unique preserve last not unique element in list
            # list_of_numbers2.pop(w)
        w += 1
    print(f"Updated elements 1 is: {list_of_numbers}")
    print(f"Updated elements 2 is: {list_of_numbers2}")
    print(f"Total number of unique elements 2 is: {len(list_of_numbers2)}")

if __name__ == "__main__":
    main()
