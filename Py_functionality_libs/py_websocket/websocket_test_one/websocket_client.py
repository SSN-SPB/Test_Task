import asyncio
import websockets

tested_list = [1, 2, 3, 4, 5]


async def test():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello server!")
        response = await websocket.recv()
        print(f"Server replied: {response}")


async def test_list():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(f"The tested list2: {tested_list}")
        response = await websocket.recv()
        print(f"Server replied: {response}")


asyncio.run(test())
asyncio.run(test_list())
