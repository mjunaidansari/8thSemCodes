import socket
import threading

lamport_clocks = {}

def handle_client(client_socket, addr):
    global lamport_clocks

    sender_id = addr[1]  # Use port as sender ID
    if sender_id not in lamport_clocks:
        lamport_clocks[sender_id] = 0

    while True:
        msg = client_socket.recv(1024).decode()
        if not msg:
            break

        # Extract timestamp
        timestamp, message = msg.split(":", 1)
        timestamp = int(timestamp)
        lamport_clocks[sender_id] = max(lamport_clocks[sender_id], timestamp) + 1

        print(f"Received from {sender_id} at time {lamport_clocks[sender_id]}: {message}")

    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5001))
server.listen(5)

print("Causal Order Server running on port 5001...")

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client, addr)).start()
