# TCP server — simulated telecom device
import socket
import struct

HOST = "127.0.0.1"
PORT = 5555

def parse_request(data):
    # Header:
    # message_type  -> 1 byte
    # transaction   -> 1 byte
    # subscriber_id -> 2 bytes
    # command       -> 1 byte
    # payload_len   -> 1 byte

    message_type, transaction_id, subscriber_id, command, payload_length = (
        struct.unpack("!BBHBB", data[:6])
    )

    payload = data[6:6 + payload_length]

    return {
        "message_type": message_type,
        "transaction_id": transaction_id,
        "subscriber_id": subscriber_id,
        "command": command,
        "payload": payload,
    }


def create_response(request):
    # Response:
    # message_type  -> 1 byte
    # transaction   -> 1 byte
    # result        -> 1 byte
    # payload_len   -> 1 byte
    # payload       -> N bytes

    response_payload = b"OK"

    return struct.pack(
        "!BBBB",
        0x02,                       # response message
        request["transaction_id"],  # same transaction ID
        0x00,                       # result = SUCCESS
        len(response_payload),
    ) + response_payload


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(3)

    print(f"Server listen: server {HOST}:{PORT}")

    connection, address = server.accept()

    with connection:
        print(f"Client connected: {address}")

        data = connection.recv(1024)

        print("RAW request:")
        print(data.hex(" "))

        request = parse_request(data)

        print("\nParsed request:")
        print(f"Message type:  0x{request['message_type']:02X}")
        print(f"Transaction ID: 0x{request['transaction_id']:02X}")
        print(f"Subscriber ID:  0x{request['subscriber_id']:04X}")
        print(f"Command:       0x{request['command']:02X}")
        print(f"Payload:       {request['payload']}")

        response = create_response(request)

        print("\nRAW response:")
        print(response.hex(" "))

        connection.sendall(response)
