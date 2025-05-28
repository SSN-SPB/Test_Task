from typing import List


def split(str, sep=" ", maxsplit=None):
    print("//////////////////////////////////////////////////////////")
    result_list = []
    previous_indicator = False
    interim_str = ""
    maxsplit_int = 0
    if not maxsplit:
        maxsplit_int = 0
    else:
        maxsplit_int = maxsplit
    if str == "":
        return []
    for x in str:
        print("New symbol '{}' ------------------".center(28, "*").format(x))
        print(
            "The previous_indicator is: {}".center(28, "*").format(previous_indicator)
        )
        print("The interim_str is: '{}'".center(28, "*").format(interim_str))
        print("The x is: '{}'".center(28, "*").format(x))

        print(" The x == sep is: {} ".center(28, "*").format(x == sep))
        print("The result list is: {}".center(28, "*").format(result_list))
        print("The maxsplit_int is: {}".center(28, "*").format(maxsplit_int))
        print(
            "if one: {}".format(
                x == sep and not previous_indicator and maxsplit_int >= 0
            )
        )
        if x == sep and not previous_indicator and maxsplit_int >= 0:
            result_list.append(interim_str)
            print("Upload interim string {}".format(interim_str))
            interim_str = ""
            previous_indicator = True
            if maxsplit_int >= 0:
                maxsplit_int = maxsplit_int - 1
            continue
        print(
            "if one_one: {}".format(
                x == sep and previous_indicator and maxsplit_int == 0
            )
        )
        if x == sep and previous_indicator and maxsplit_int == 0:
            continue
        print("if two: {}".format(x != sep and maxsplit_int < 0))
        if x != sep and maxsplit_int <= 0:
            interim_str = interim_str + x
            previous_indicator = False
            continue
        print(
            "if three: {}".format(
                x == sep and not previous_indicator and maxsplit_int < 0
            )
        )
        if x == sep and not previous_indicator and maxsplit_int < 0:
            result_list.append(interim_str)
            print("Upload interin string {}".format(interim_str))
            previous_indicator = True
            interim_str = ""
            continue
        # print('if four: {}'.format(x == sep and not previous_indicator and maxsplit_int > 0))
        # if x == sep and not previous_indicator and maxsplit_int > 0:
        #     result_list.append(interim_str)
        #     print('Upload interin string {}'.format(interim_str))
        #     previous_indicator = True
        #     interim_str = ''
        #     maxsplit_int = maxsplit_int - 1
        #     continue
        if x != sep and not previous_indicator and maxsplit_int >= 0:
            interim_str = interim_str + x
            continue
        # print('if one: {}'.format(x != sep and not previous_indicator and maxsplit > 0))
        # if x != sep and not previous_indicator and (maxsplit > 0 or maxsplit == None):
        #     interim_str = interim_str + x
        # print('if two: {}'.format(x != sep and maxsplit <= 0))
        # if x != sep and maxsplit <= 0:
        #     interim_str = interim_str + x
        #     previous_indicator = False
        # print('if 3: {}'.format(x == sep and previous_indicator and maxsplit > 0))
        # if x == sep and previous_indicator and maxsplit > 0:
        #     result_list.append(interim_str)
        #     previous_indicator = True
        #     interim_str = ''
        #     maxsplit = maxsplit - 1
        # print('if 3: {}'.format(x == sep and previous_indicator and maxsplit > 0))
        # if x == sep and maxsplit <= 0:
        #     result_list.append(x)
        #     continue
        # print('if 4: {}'.format(x == sep and not previous_indicator and maxsplit <= 0))
        # if x == sep and not previous_indicator and maxsplit <= 0:
        #     result_list.append(interim_str)
        #     previous_indicator = True
        #     interim_str = ''
        #     maxsplit = maxsplit - 1
        #     continue
        # print('if 5: {}'.format(x == sep and previous_indicator and maxsplit <= 0))
        # if x == sep and previous_indicator and maxsplit <= 0:
        #
        #     previous_indicator = True
        #     continue
        #     # result_list.append('')
        # print('if 6: {}'.format(x == sep and not previous_indicator and maxsplit > 0))
        # if x == sep and not previous_indicator and maxsplit > 0:
        #     result_list.append(interim_str)
        #     previous_indicator = True
        #     interim_str = ''
        #     maxsplit = maxsplit - 1
        #     continue
    print("The before final previous_indicator is: {}".format(previous_indicator))
    print("The before final maxsplit is: {}".format(maxsplit))
    print("The before final interim_str is: '{}'".format(interim_str))
    print("The before final x is: '{}'".format(x))
    print("The before final result list is: {}".format(result_list))
    print("The before final x == sep is: {}".format(x == sep))

    print("if final one: {}".format(interim_str == "" and previous_indicator))
    if interim_str == "" and previous_indicator:
        result_list.append(interim_str)
    print("if final2: {}".format(interim_str != ""))
    if interim_str != "":
        result_list.append(interim_str)
    # print('if final3: {}'.format(
    #     x == sep and interim_str != '' and previous_indicator))
    # if x == sep and interim_str == '' and previous_indicator:
    #     result_list.append(interim_str)
    print("The result is: {}".format(result_list))

    return result_list


def main():
    print("assert1")
    assert split("") == []
    print("assert2")
    assert split(",123,", sep=",") == ["", "123", ""]
    print("assert3")
    assert split("test") == ["test"]
    print("assert4")
    assert split("Python   2     3", maxsplit=1) == ["Python", "2     3"]
    # assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    # assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    # assert split('    set   3     4') == ['set', '3', '4']
    # assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    # assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']


if __name__ == "__main__":
    main()
