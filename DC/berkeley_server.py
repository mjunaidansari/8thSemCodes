# Master Node (Server)
import socket
import time

HOST = 'localhost'
PORT = 12345

def berkeley_master():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(3)
    print("Master: Waiting for connections...")
    
    nodes = []
    times = []
    
    while len(nodes) < 3:  # Expecting 3 slave nodes
        conn, addr = server.accept()
        print(f"Connected to {addr}")
        conn.sendall(b"REQUEST_TIME")
        node_time = float(conn.recv(1024).decode())
        nodes.append(conn)
        times.append(node_time)
    
    master_time = time.time()
    avg_diff = sum(t - master_time for t in times) / len(times)
    
    for conn in nodes:
        conn.sendall(str(avg_diff).encode())
        conn.close()
    
    print("Master: Synchronization complete.")
    server.close()

berkeley_master()
