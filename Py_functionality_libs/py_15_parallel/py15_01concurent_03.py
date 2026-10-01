from concurrent.futures import ThreadPoolExecutor
import time


def request(name):
    print(f"Start {name}")
    time.sleep(2)
    print(f"Done {name}")


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(request, ["API 1", "API 2", "API 3"])