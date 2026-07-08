import concurrent.futures
import time
import requests

# concurrent.futures is a high-level interface
# for asynchronously executing callables.

URLS = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
]

def load_url(url, timeout):
    try:
        response = requests.get(url, timeout=timeout)
        print(f"Loaded {url} with status code {response.status_code}")
        return f"{url}: {len(response.content)} bytes"
    except requests.exceptions.RequestException as e:
        return f"{url}: Error: {e}"


start_time = time.time()

# Sequential execution:
for url in URLS:
    print(load_url(url, timeout=60))


end_time = time.time()
print(f"Sequential execution took: {end_time - start_time} seconds")





start_time = time.time()

# Asynchronous execution with ThreadPoolExecutor:
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # map() returns results in the order of URLS
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print(f"{url}: generated an exception: {exc}")
        else:
            print(data)

end_time = time.time()
print(f"Asynchronous execution took: {end_time - start_time} seconds")



