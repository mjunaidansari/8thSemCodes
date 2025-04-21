import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

for i in range(5):
    client.send(f"Message {i}".encode())
    time.sleep(1)

client.close()
