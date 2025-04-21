import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

client.send(f"Hello from process {client.getsockname()[1]}".encode())

time.sleep(1)  # Simulate delay before sending next message

client.close()
