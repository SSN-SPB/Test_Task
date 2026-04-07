# This is a basic example of using the asyncio
# library in Python to run asynchronous tasks.
import asyncio
import aiohttp


urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
]

async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        for result in results:
            print(f'Title of result.id {result["id"]}: {result["title"]}')



if __name__ == "__main__":
    asyncio.run(main())
