import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))  # Bind to localhost and port 12345
    server_socket.listen(1)  # Listen for incoming connections

    print("Server is listening on port 12345...")
    
    conn, addr = server_socket.accept()  # Accept a client connection
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)  # Receive data from client
        if not data:
            break  # Exit if no data
        print(f"Client says: {data.decode()}")
        
        response = input("Enter reply: ")
        conn.send(response.encode())  # Send response back to client

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
