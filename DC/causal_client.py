import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5001))

lamport_clock = 0

for i in range(5):
    lamport_clock += 1  # Increment clock
    client.send(f"{lamport_clock}:Message {i}".encode())
    time.sleep(1)

client.close()
