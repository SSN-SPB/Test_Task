import socket

HOST = "127.0.0.1"
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    message = "Hello from Python client!"
    client.sendall(message.encode("utf-8"))
    print(f"Server listen: server {HOST}:{PORT}")
    data = client.recv(1024)

    print(f"Server's response: {data.decode('utf-8')}")
