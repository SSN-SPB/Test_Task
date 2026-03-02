import asyncio


async def async_range(start, stop):
    for i in range(start, stop):
        await asyncio.sleep(1)
        yield i


async def main():
    async for num in async_range(0, 5):
        print(num)


if __name__ == "__main__":
    asyncio.run(main())
