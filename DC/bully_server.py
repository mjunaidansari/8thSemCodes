import socket
import threading

processes = {}

# Simulate Bully Election (Election message is sent to processes with higher IDs)
def election(client_socket, client_addr, current_process_id):
    print(f"Election started by process {current_process_id}")
    for pid, process_socket in processes.items():
        if pid > current_process_id:
            message = f"Election from {current_process_id}"
            process_socket.send(message.encode())

def handle_client(client_socket, client_addr):
    global processes
    process_id = int(client_addr[1])
    processes[process_id] = client_socket
    print(f"Process {process_id} joined.")
    
    # If process is the highest ID, initiate the election
    if process_id == max(processes.keys()):
        election(client_socket, client_addr, process_id)
        
    while True:
        msg = client_socket.recv(1024).decode()
        if not msg:
            break
        print(f"Received from {client_addr}: {msg}")
    
    processes.pop(process_id)
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(5)

print("Bully Election Server running on port 5000...")

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client, addr)).start()
