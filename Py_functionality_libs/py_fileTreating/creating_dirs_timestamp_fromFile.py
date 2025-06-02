#!/usr/bin/env python3

import os


def main():
    timestamp_file = open("timestamp_file.txt", "r")
    timestamp = timestamp_file.readlines()[0]
    # print(timestamp)
    makedir(timestamp, postfix="_jdn")
    makedir(timestamp, postfix="_jdi_light")


def makedir(ts, prefix="clone_", postfix="temp"):
    name_of_dir = prefix + str(ts) + postfix
    os.mkdir(name_of_dir)


if __name__ == "__main__":
    main()
