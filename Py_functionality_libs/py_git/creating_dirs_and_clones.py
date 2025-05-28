#!/usr/bin/env python3

import os
import time
import datetime
import git

# set the current directory as root
script_rood_dir = os.getcwd()


def git_clone(rep_to_clone):
    # clone required repository to current folder
    git.Git(os.getcwd()).clone(rep_to_clone)
    # return to root directoty
    os.chdir(script_rood_dir)


def main():
    # open existing file with timestamp
    timestamp_file = open("timestamp_file.txt", "r")
    timestamp = timestamp_file.readlines()[0]
    # print(timestamp)
    makedir(
        timestamp,
        postfix="_jdn",
        repsitory_to_clone="https://github.com/jdi-testing/jdn.git",
    )
    makedir(
        timestamp,
        postfix="_jdi_light",
        repsitory_to_clone="https://github.com/jdi-examples/jdn-with-jdi-light.git",
    )


def makedir(
    ts,
    prefix="clone_",
    postfix="temp",
    repsitory_to_clone="https://github.com/jdi-testing/jdn.git",
):
    name_of_dir = prefix + str(ts) + postfix
    os.mkdir(name_of_dir)
    os.chdir(name_of_dir)
    print(name_of_dir)
    print(os.getcwd())
    git_clone(repsitory_to_clone)


if __name__ == "__main__":
    main()
