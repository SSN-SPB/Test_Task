# https://www.linkedin.com/learning/learning-python-2
#        /reading-and-writing-files?u=2113185
# File writing
import os


def get_list_of_file(name_of_dir):
    # list_of_files = os.listdir(name_of_dir)
    print("Check dir: {}".format(name_of_dir))
    #    print(list_of_files)
    #    for i in list_of_files:
    #        if os.path.isdir(i):
    #            print('See the list of files in subdirectory {}'.format(i))
    #            get_list_of_file(i)
    #        else:
    #            print('The {} is file'.format(i))
    for dirpath, dirnames, filenames in os.walk("."):
        # перебрать каталоги
        for dirname in dirnames:
            print("Catalogue:", os.path.join(dirpath, dirname))
        # перебрать файлы
        for filename in filenames:
            print("File:", os.path.join(dirpath, filename))


def main():
    current_dir = os.getcwd()
    get_list_of_file(current_dir)
    target_dir = "c:\\DiskD\\Projects\\IDBS_EWB\\Demos"
    # print('Check the exact dir: {}'.format(target_dir))
    get_list_of_file(target_dir)


if __name__ == "__main__":
    main()
