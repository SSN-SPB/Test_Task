from collections import Counter

# def add_line(self, line: str):
#     array_list.append(line.split(" "))

def add_line(test_list, line: str):
    test_list.append(line.split(" "))

# def error_count(self) -> int:
#     return True

def error_count(test_list) -> int:
    error_counter = 0
    for x in test_list:
        if x[1] == 'ERROR':
            error_counter +=1
    return error_counter

# def count_by_level(self) -> dict:
#     return True

def count_by_level(test_list) -> dict:
    status_list = []
    for x in test_list:
        status_list.append(x[1])
    print(status_list)
    return dict(Counter(status_list))

# def top_users(self, n=3):
#     return True

def top_users(test_list):
    users_list = []
    final_list = []
    for x in test_list:
        users_list.append(x[2])
    print(users_list)
    dict_sorted =dict(Counter(users_list))
    for k, v in dict_sorted.items():
        final_list.append((k,v))
    print(final_list)
    sorted_data = sorted(final_list, key=lambda x: x[1], reverse=True)
    print(sorted_data)
    return dict_sorted

def search(self, keyword: str):
    return True

def main():
    new_file_name = open("log260620.txt", "r+")
    array_list = []
    for line in new_file_name:
        print(line.strip())
        add_line(array_list, line)
        # array_list.append(line.split(" "))
    print(array_list)
    print(error_count(array_list))
    print(count_by_level(array_list))
    print(top_users(array_list))



if __name__ == "__main__":
    main()