#!/usr/bin/env python3


def check_if_with_mask(string, mask):
    mask_included = False
    if string.find(mask) != -1:
        mask_included = True
    return mask_included


def main():
    # input data
    result = check_if_with_mask("0.0.0.0", "/")
    print(result)
    result = check_if_with_mask("255.255.255.255/32", "/")
    print(result)


if __name__ == "__main__":
    main()
