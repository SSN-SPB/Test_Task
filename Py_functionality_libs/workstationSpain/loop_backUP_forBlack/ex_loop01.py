def checking_result(expected, received, text="Check maximal val"):
    print(text)
    print("expected: {}".format(expected))
    print("received: {}".format(received))
    try:
        assert expected == received
        print("Checking has passed")
    except AssertionError as ae:
        print("checking has failed. \n__doc__: {}".format(ae.__doc__))
        print("__context__: {}".format(ae.__context__))

def list_all_negatives_in_list(tested_array):
    negative_list = []
    for x in tested_array:
        try:
            if x < 0:
                negative_list.append(x)
        except TypeError:
            print("The list includes non-digits {}".format(x))
    return negative_list

def main():
    x = 0
    while x < 10:
        x += 1
        print(x)

if __name__ == "__main__":
    main()

