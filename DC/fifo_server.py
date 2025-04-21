import socket
import threading

# FIFO Message Queue for each sender
message_queues = {}

def handle_client(client_socket, addr):
    global message_queues

    sender_id = addr[1]  # Use port as sender ID
    if sender_id not in message_queues:
        message_queues[sender_id] = []

    while True:
        msg = client_socket.recv(1024).decode()
        if not msg:
            break

        # Store message in sender's FIFO queue
        message_queues[sender_id].append(msg)

        # Process messages in order
        while message_queues[sender_id]:
            print(f"Received from {sender_id}: {message_queues[sender_id].pop(0)}")

    client_socket.close()

# Start FIFO Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(5)

print("FIFO Server running on port 5000...")

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client, addr)).start()
