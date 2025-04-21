# Slave Nodes (Clients)
import socket
import time
import threading

HOST = 'localhost'
PORT = 12345

def berkeley_slave(node_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    
    request = client.recv(1024).decode()
    if request == "REQUEST_TIME":
        local_time = time.time()
        client.sendall(str(local_time).encode())
    
    adjustment = float(client.recv(1024).decode())
    adjusted_time = local_time - adjustment
    print(f"Slave {node_id}: Original time: {local_time}, Adjusted time: {adjusted_time}")
    
    client.close()

# Simulating 3 clients concurrently
threads = []
for i in range(1, 4):
    t = threading.Thread(target=berkeley_slave, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
