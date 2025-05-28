import re


def check(str, pattern):
    # _matching the strings
    if re.search(pattern, str):
        print("Valid String")
    else:
        print("Invalid String")


# _driver code
# pattern = re.compile('^[1234]+$')
pattern = re.compile("[583]")
check("7865serS3", pattern)
check("7865serS4", pattern)
