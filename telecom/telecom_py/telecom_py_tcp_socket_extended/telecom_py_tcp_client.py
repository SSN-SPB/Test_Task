import socket
import struct

HOST = "127.0.0.1"
PORT = 5555

transaction_id = 0x42
subscriber_id = 0x1234
command = 0x10
payload = b"ABC"

request = struct.pack(
    "!BBHBB",
    0x01,                  # message type
    transaction_id,        # transaction ID
    subscriber_id,        # subscriber ID
    command,               # command
    len(payload),          # payload length
) + payload


print("Sending:")
print(request.hex(" "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    # message = "Hello from Python client!"
    client.sendall(request)
    print(f"Server listen: server {HOST}:{PORT}")
    response = client.recv(1024)

    print(f"Server's response: {response.decode('utf-8')}")

print("\nReceived:")
print(response.hex(" "))


# Parse response

message_type, transaction_id, result, payload_length = struct.unpack(
    "!BBBB",
    response[:4],
)

payload = response[4:4 + payload_length]


print("\nParsed response:")
print(f"Message type:   0x{message_type:02X}")
print(f"Transaction ID: 0x{transaction_id:02X}")
print(f"Result:         0x{result:02X}")
print(f"Payload:        {payload}")
