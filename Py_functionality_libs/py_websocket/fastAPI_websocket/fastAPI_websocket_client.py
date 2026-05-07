import asyncio
import websockets


async def test():
    uri = "ws://127.0.0.1:8000/ws"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hi FastAPI again!")
        response = await websocket.recv()
        print(response)


asyncio.run(test())
