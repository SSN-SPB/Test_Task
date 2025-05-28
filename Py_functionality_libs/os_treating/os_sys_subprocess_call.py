#!/usr/bin/env python3

import os
import subprocess


def main():
    print(
        subprocess.Popen(
            "echo Hello World", shell=True, stdout=subprocess.PIPE
        ).stdout.read()
    )
    print(subprocess.call("echo Hello World", shell=True))
    print(os.popen("echo Hello World from os").read())


if __name__ == "__main__":
    main()
