from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

a = ZoneInfo("America/Los_Angeles")
print(a)

# dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
# print(dt)
