# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# list 20- 25
# append - one element to the end
# extend - several elements to the end of list
# insert - add element by index


def main():
    list = [0, 1]
    list2 = ['a', 'b']
    list3 = ['с', 'в']
    list.append(list2)
    print(list)      # [0, 1, ['a', 'b']]
    list.extend(list3)
    print(list)      # [0, 1, ['a', 'b'], 'с', 'в']

if __name__ == "__main__":
    main()
