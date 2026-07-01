# pip install websocket-client
import websocket

ws = websocket.create_connection("ws://localhost:8765", timeout=5)
ws.send("Not asyncio message")
response = ws.recv()
print(response)
ws.close()
