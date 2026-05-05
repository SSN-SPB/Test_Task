from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # print("Client connected")
    logger.info("Client connected")

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received: {data}")
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        # print("Client disconnected")
        logger.info("Client now disconnected")
