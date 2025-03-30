# code demonstrates using command line arguments
# command line for demo -v --h --help -help -h --version -version --v
import sys

VERSION = "The current version is 1.0.0."
HELP_INSTRACTION = "Intruction for user"


def main():
    for x in sys.argv:
        print("for argumenet {} print:".format(x))
        if x == "-v" or x == "--version":
            print(VERSION)
        elif x == "-h" or x == "--help":
            print(HELP_INSTRACTION)
        else:
            print("no value found")


if __name__ == "__main__":
    main()
