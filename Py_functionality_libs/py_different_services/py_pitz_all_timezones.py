from datetime import *
import pytz


def main():
    tz_india = pytz.timezone('Asia/Kolkata')
    datetime_india = datetime.now(tz_india)
    print("INDIA time:", datetime_india.strftime("%H:%M:%S")),
    for x in pytz.all_timezones:
        # print(x)
        print("Timezone {} "
              "- current time:"
              " {}".format(x,
                           datetime.now(pytz.timezone(x)).strftime("%H:%M:%S")))


if __name__ == "__main__":
    main()
