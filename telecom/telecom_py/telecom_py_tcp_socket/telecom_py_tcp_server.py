import socket

HOST = "127.0.0.1"
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(3)

    print(f"Server listen: server {HOST}:{PORT}")

    connection, address = server.accept()

    with connection:
        print(f"Client connected: {address}")

        while True:
            data = connection.recv(1024)
            if not data:
                print("No data found during connection")
                break
            message = data.decode("utf-8")
            response = f"Message: {message}"
            print(response)
            connection.sendall(response.encode("utf-8"))
