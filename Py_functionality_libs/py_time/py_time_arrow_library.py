import arrow


def ts_printed():
    ts = arrow.now()
    ts_printed = ts.format("YYYY_MM_DD__HH_mm_ss")
    ts_shifted = ts.shift(hours=3)
    return ts_printed, ts_shifted


def main():
    this_time, shifted_time = ts_printed()
    print(this_time)
    print(f"The time in English: {shifted_time.humanize(locale='en')}")
    print(f"The time in Russian: {shifted_time.humanize(locale='ru')}")
    print(f"The time in Chinese: {shifted_time.humanize(locale='zh')}")


if __name__ == "__main__":
    main()
