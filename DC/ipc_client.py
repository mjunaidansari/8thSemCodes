import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))  # Connect to server

    while True:
        message = input("Enter message to server: ")
        if message.lower() == "exit":
            break  # Exit the loop if "exit" is entered
        client_socket.send(message.encode())  # Send message to server

        response = client_socket.recv(1024)  # Receive response from server
        print(f"Server replies: {response.decode()}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
