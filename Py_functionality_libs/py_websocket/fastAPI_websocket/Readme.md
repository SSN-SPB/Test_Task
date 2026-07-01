In order to test websocket functionality, we should 
1 install the following libraries:
pip install fastapi uvicorn
2 run the server from fastAPI_websocket_server.py by using the following command:
uvicorn fastAPI_websocket_server:app --reload
3 run the client: fastAPI_websocket_client.py (in a separate terminal)
# 4 open the browser and navigate to http://localhost:8000/docs to see the websocket documentation

# WebSockets → a protocol (like HTTP)
# FastAPI WebSocket → a way to use that protocol inside FastAPI
