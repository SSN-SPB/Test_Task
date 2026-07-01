import time
from functools import wraps

# 1️⃣ Retry decorator
def retry(times=2, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(times):
                try:
                    print(f"Attempt {attempt+1}/{times}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying due to: {e}")
                    last_exception = e
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator


# 2️⃣ Screenshot on failure
def screenshot_on_fail(func):
    @wraps(func)
    def wrapper(page, *args, **kwargs):
        try:
            return func(page, *args, **kwargs)
        except Exception:
            filename = f"screenshot_{int(time.time())}.png"
            page.screenshot(path=filename)
            print(f"Saved screenshot: {filename}")
            raise
    return wrapper


# 3️⃣ Measure execution time
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"{func.__name__} took {duration:.2f}s")
        return result
    return wrapper


# 4️⃣ Login decorator
def login_required(func):
    @wraps(func)
    def wrapper(page, *args, **kwargs):
        print("Logging in...")
        page.goto("https://the-internet.herokuapp.com/login")

        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type=submit]")

        page.wait_for_selector(".flash.success")
        print("Login successful")

        return func(page, *args, **kwargs)
    return wrapper