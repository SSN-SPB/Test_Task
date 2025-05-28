#!/usr/bin/env python3


# import pytest
import requests

# https://stackoverflow.com/questions/29001307/going-through-html-dom-in-python

import urllib.request


def getSite(url):
    return urllib.request.urlopen(url)


def main():
    # dom as a string
    content = str(getSite("https://github.com/jdi-testing/jdn").read())
    # defining first 5 simbols after split
    print((content.split("/jdi-testing/jdn/releases/tag/", 1)[-1])[0:5])  # 2.2.0
    # defining first 5 simbols after partition
    print((content.partition("/jdi-testing/jdn/releases/tag/")[2])[0:5])  # 2.2.0


if __name__ == "__main__":
    main()
