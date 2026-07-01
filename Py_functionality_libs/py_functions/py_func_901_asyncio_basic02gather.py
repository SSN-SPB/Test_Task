# This is a basic example of using the asyncio
# library in Python to run asynchronous tasks.
import asyncio


async def async_task(task_id, delay):
    print(f"Task {task_id} started, will take {delay} seconds.")
    await asyncio.sleep(delay)
    print(f"Hello {task_id} completed after {delay} seconds.")


async def main():
    tasks = [
        async_task("Id3", 3),
        async_task("Id1", 1),
        async_task("Id2", 2),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
