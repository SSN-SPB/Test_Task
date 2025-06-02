import datetime
import time
from contextlib import redirect_stdout


def redirect_to_log(file_name, log_text):
    with open(file_name, "a+") as file_log:
        with redirect_stdout(file_log):
            print(log_text)
        file_log.close()


def main():
    message = "Hello File - "
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y_%m_%d_%H_%M_%S_%f")

    redirect_to_log("file_to_modify.txt", message + st)


if __name__ == "__main__":
    main()
