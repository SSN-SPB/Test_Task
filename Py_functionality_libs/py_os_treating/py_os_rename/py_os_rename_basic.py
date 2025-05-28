#!/usr/bin/env python3

import os


def rename_file(file_name_init, file_name_new):
    os.rename(file_name_init, file_name_new)


def main():
    rename_file("filename.txt", "filename_modified.txt")
    # rename_file("filename_modified.txt", "filename.txt")


if __name__ == "__main__":
    main()
