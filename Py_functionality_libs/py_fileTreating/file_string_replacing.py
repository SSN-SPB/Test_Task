# https://www.linkedin.com/learning/learning-python-2/reading-and-writing-files
# File writing
#
import os


def cleaning_files():
    result = "File to remove is not found"
    for x in os.listdir(os.getcwd()):
        # print(x)
        if x == "file_to_modify.txt":
            result = "File to remove is found"
            os.remove(x)
    print(result)


def main():
    print("Hello File")
    # creating new file; "w+" the access level to work with new file
    # w+ - overwriting
    # r - reading
    # a - append to the end of file
    # b - byte
    # e.g. 'r+b'
    # .flush() - opens buffer
    # .close() - closes buffer

    cleaning_files()
    current_dir = os.getcwd()
    print(current_dir)
    file_path = current_dir + "\\file_init_to_modify.txt"
    print(file_path)
    file_name = open(file_path, "r")
    data = file_name.read()
    data = data.replace(",", "()")
    file_name.close()
    file_name_modified = open("file_to_modify.txt", "w+")
    file_name_modified.write(data)
    file_name_modified.close()
    cleaning_files()


if __name__ == "__main__":
    main()
