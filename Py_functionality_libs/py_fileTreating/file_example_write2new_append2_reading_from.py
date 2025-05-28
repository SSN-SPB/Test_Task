# https://www.linkedin.com/learning/learning-python-2/reading-and-writing-files?u=2113185
# File writing
#


def main():
    print("Hello File")
    # creating new file; "w+" the access level to work with new file
    # w+ - overwriting
    # r - reading
    # a - append to the end of file
    # b - byte
    # e.g. 'r+b'
    new_file_name = open("course2_training_file1.txt", "w+")
    for i in range(10):
        new_file_name.write("This is line: " + str(i) + "\r\n")
    new_file_name.close()

    # r - reading from file
    new_file_name_read = open("course2_training_file1.txt", "r")
    print("Reading the file: " + "\n" + new_file_name_read.read())
    new_file_name_read.close()

    # a - append to the end of file
    file_name = open("course2_training_file1.txt", "a")
    for i in range(21, 25):
        file_name.write("This is line: " + str(i) + "\n")
    file_name.close()

    # r - reading from file
    new_file_name_read = open("course2_training_file1.txt", "r")
    fl = new_file_name_read.readlines()
    print("print first arg {}from file: ".format(fl[0]))
    for x in fl:
        print(x)


if __name__ == "__main__":
    main()
