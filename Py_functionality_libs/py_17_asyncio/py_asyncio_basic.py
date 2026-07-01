import asyncio
import time
import datetime


async def put_movie(title, year, plot, rating, dynamodb=None):
    initial_time = time.time()
    # Build timestamp with milliseconds (3 digits) but not (%f gives 6 digits)
    st = await get_actual_time(initial_time)
    print(f"Putting movie into database...{st}")
    # Simulate an asynchronous operation, e.g., a database call
    await asyncio.sleep(11)
    completion_time = time.time()
    ct = await get_actual_time(completion_time)
    print(f"Movie {title} added: during {completion_time - initial_time:.2f}sec.")
    print(f"Completion Time...{ct}")


async def get_actual_time(initial_time):
    dt = datetime.datetime.fromtimestamp(initial_time)
    st = dt.strftime("%Y_%m_%d_%H_%M_%S.") + f"{dt.microsecond // 1000:03d}"
    return st


if __name__ == "__main__":
    asyncio.run(put_movie("The New Movie", 2015, "It happens at all.", 0))
