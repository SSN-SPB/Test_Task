# https://www.linkedin.com/learning/learning-python-2/reading-and-writing-files?u=2113185
# File writing
import sys


def main():
    print("Hello File")
    # creating new file; "w+" the access level to work with new file
    # w+ - overwriting
    # r - reading
    # a - append to the end of file
    # x - open for exclusive creation, failing if the file already exists
    # b - byte
    # e.g. 'r+b'
    # .flush() - cleans buffer
    # .close() - closes file and cleans buffer
    new_file_name = open("course2_training_file1.txt", "r+")
    print(dir(new_file_name))
    for x in dir(new_file_name):
        function_list = str(x) + "()"
        print(function_list)

    print(new_file_name.tell())
    print(new_file_name.fileno())
    print(new_file_name.detach())
    print(*range(4))  # 0 1 2 3
    print(*range(4), sep="_")  # 0_1_2_3
    # print(new_file_name.seek(0), file = sys.stderr)
    # print('new_file_name.seek(0)', file = sys.stdout)
    # output = open("sys.stdout", "r+")
    # for x in dir(file):
    #    print(x)
    # print(new_file_name.fileno())


if __name__ == "__main__":
    main()
