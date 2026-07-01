# This is a basic example of using the asyncio
# library in Python to run asynchronous tasks.
import asyncio


async def async_task(task_id, delay):
    print(f"Task {task_id} started, will take {delay} seconds.")
    await asyncio.sleep(delay)
    print(f"Hello {task_id} completed after {delay} seconds.")


async def main():
    name7 = async_task("name7", 7)
    name5 = async_task("name5", 5)
    name4 = async_task("name4", 4)
    await name7
    await name5
    await name4


if __name__ == "__main__":
    asyncio.run(main())
