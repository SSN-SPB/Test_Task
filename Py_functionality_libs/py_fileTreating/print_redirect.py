from contextlib import redirect_stdout
import datetime
import time


def redirect_to_log(file_name, log_text):
    with open(file_name, "a+") as l:
        with redirect_stdout(l):
            print(log_text)
        l.close()




def main():
    message ="Hello File - "
    st = datetime.datetime.fromtimestamp(time.time()).strftime("%Y_%m_%d_%H_%M_%S_%f")

    redirect_to_log("file_to_modify.txt", message + st)



if __name__ == "__main__":
    main()
