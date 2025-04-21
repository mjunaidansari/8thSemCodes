import socket
import threading

sequence_number = 0
message_queue = []

def handle_client(client_socket):
    global sequence_number

    while True:
        msg = client_socket.recv(1024).decode()
        if not msg:
            break

        sequence_number += 1  # Assign unique sequence number
        ordered_message = f"[Seq {sequence_number}] {msg}"
        
        message_queue.append(ordered_message)

        print(f"Ordered Message: {ordered_message}")

    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5002))
server.listen(5)

print("Total Order Server running on port 5002...")

while True:
    client, _ = server.accept()
    threading.Thread(target=handle_client, args=(client,)).start()
