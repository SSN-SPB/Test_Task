#!/usr/bin/env python3

import datetime
import time

# %d - Day of the month as a zero-padded decimal number.
# %m - Month as a zero-padded decimal number.
# %Y - Year with century as a decimal number
# %H - Hour (24-hour clock) as a zero-padded decimal number.
# %M - Minute as a zero-padded decimal number.
# %S - Second as a zero-padded decimal number.
# %f - Microsecond as a decimal number, zero-padded on the left.


def main():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y_%m_%d_%H_%M_%S_%f")
    print(st)
    st = datetime.datetime.fromtimestamp(ts).strftime("%y.%m.%d.")
    print(st)


if __name__ == "__main__":
    main()
