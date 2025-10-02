#!/usr/bin/env python3
import os
import subprocess


def main():
    # os.system("cmd")
    subprocess.run("cmd")
    os.system("cmd", "python -v")
    # os.system("notepad systemfile")
    # os.path.dirname(sys.executable)


if __name__ == "__main__":
    main()
