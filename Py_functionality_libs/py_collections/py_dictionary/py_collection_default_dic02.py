from collections import defaultdict

grouped_dictionary = defaultdict(int)

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

def count_default_dic(tested_list, test_default_dic):
    for item in tested_list:
        test_default_dic[item] += 1
    return test_default_dic


# updated_dict = count_default_dic(words, grouped_dictionary)
# print(dict(updated_dict))
print(dict(count_default_dic(words, grouped_dictionary)))

