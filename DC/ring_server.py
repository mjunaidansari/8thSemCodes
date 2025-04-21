import socket
import threading

# Store process IDs and their corresponding sockets
processes = {}

def start_election(client_socket, client_addr, current_process_id):
    print(f"Election started by process {current_process_id}")
    next_process = processes[(current_process_id % len(processes)) + 1]
    next_process.send(f"Election from {current_process_id}".encode())

def handle_client(client_socket, client_addr):
    global processes
    process_id = int(client_addr[1])
    processes[process_id] = client_socket
    print(f"Process {process_id} joined.")
    
    # Start the election if the process is the first in the ring
    if process_id == 1:
        start_election(client_socket, client_addr, process_id)
        
    while True:
        msg = client_socket.recv(1024).decode()
        if not msg:
            break
        print(f"Received from {client_addr}: {msg}")
    
    processes.pop(process_id)
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 6000))
server.listen(5)

print("Ring Election Server running on port 6000...")

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client, addr)).start()
