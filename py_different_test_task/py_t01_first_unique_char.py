
tested_string = "swiss"
tested_string2 = "aabb"

def return_first_unique(list_to_review):
    for x in list_to_review:
        if list_to_review.count(x) == 1:
            return x
    return None

def main():
    print(return_first_unique(tested_string))
    print(return_first_unique(tested_string2))
    assert return_first_unique(tested_string) == "w"
    assert not return_first_unique(tested_string2)
if __name__ == "__main__":
    main()