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
    new_file_name = open("output.txt", "r+")
    print(dir(new_file_name))
    for line in new_file_name:
        print(line.strip())


if __name__ == "__main__":
    main()
