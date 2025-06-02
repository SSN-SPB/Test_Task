#!/usr/bin/env python3

import datetime
import os
import time
import zipfile

# %d - Day of the month as a zero-padded decimal number.
# %m - Month as a zero-padded decimal number.
# %Y - Year with century as a decimal number
# %H - Hour (24-hour clock) as a zero-padded decimal number.
# %M - Minute as a zero-padded decimal number.
# %S - Second as a zero-padded decimal number.
# %f - Microsecond as a decimal number, zero-padded on the left.

target_zip = "C:\\Users\\Sergei_Smirnov\\Downloads\\dist.zip"
script_rood_dir = os.getcwd()


def upzipfile(path_to_zip_file, directory_to_extract_to):
    with zipfile.ZipFile(path_to_zip_file, "r") as zip_ref:
        zip_ref.extractall(directory_to_extract_to)


def makedir(ts, prefix="jdn_plugin_", postfix="_temp"):
    name_of_dir = prefix + str(ts) + postfix
    os.mkdir(name_of_dir)
    os.chdir(name_of_dir)
    created_dir = os.getcwd()
    return created_dir


def main():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y_%m_%d_%H_%M_%S_%f")
    timestamp_file = open("timestamp_file.txt", "w+")
    timestamp_file.write(st)
    timestamp_file.close()
    # opening timestamp file
    timestamp_file = open("timestamp_file.txt", "r")
    timestamp = timestamp_file.readlines()[0]
    # creating dir with timestamp
    target_dir = makedir(timestamp, postfix="_test")
    upzipfile(target_zip, target_dir)
    os.chdir(script_rood_dir)


if __name__ == "__main__":
    main()
