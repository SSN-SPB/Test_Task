import datetime
import time

ts = time.time()
current_time = datetime.datetime.fromtimestamp(ts).strftime(
    "%Y_%m_%d_%H_%M_%S"
)
