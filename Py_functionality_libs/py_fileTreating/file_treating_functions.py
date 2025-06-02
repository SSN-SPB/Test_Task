# https://www.linkedin.com/learning/learning-python-2/reading-and-writing-files?u=2113185
# File writing


def main():
    print("Hello File")
    # creating new file; "w+" the access level to work with new file
    # w+ - overwriting
    # r - reading
    # a - append to the end of file
    # x - open for exclusive creation, failing if the file already exists
    # b - byte
    # e.g. 'r+b'
    # .flush() - opens buffer
    # .close() - closes buffer
    new_file_name = open("course2_training_file1.txt", "w+")
    for i in range(10):
        new_file_name.write("This is line: " + str(i) + "\r")
    new_file_name.close()

    print("Read from file {}".format("course2_train1.txt").center(80, "/"))
    # r - reading from file
    new_file_read = open("course2_train1.txt", "r+")
    fl = new_file_read.readlines()
    for x in fl:
        print(x + "\n")
    try:
        xfile_read = open("course2_train1.txt", "x")
        test = str(xfile_read)
        print(test)
    except Exception as e:
        # print(e.args)
        # print(dir(e))
        print("e: ")
        print(e)
        print("exception {} is {}".format("__doc__", e.__doc__))
        print("exception {} is {}".format("__str__", e.__str__))
        for x in dir(e):
            try:
                print(
                    "exeception function: {}; The value is {}".format(
                        x, getattr(e, str(x))
                    )
                )
            except Exception as e:
                print(f"not found attribute: {str(x)}  {e}")
    print("open file function: {}".format("tell()").center(80, "/"))
    print("tell - where you are in file")
    print(new_file_read.tell())

    print("open file function: {}".format("seek(8)").center(80, "/"))
    new_file_read.seek(8)
    print(new_file_read.tell())
    new_file_read.flush()


if __name__ == "__main__":
    main()
