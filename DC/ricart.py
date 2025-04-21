import socket
import threading
import time
import random

peers = []
port = 0
requesting_cs = False
reply_count = 0
lock = threading.Lock()

def listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", port))
    server.listen(5)
    print(f"[{port}] Listening for connections...")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_request, args=(conn,)).start()

def handle_request(conn):
    global reply_count, requesting_cs
    with conn:
        data = conn.recv(1024).decode().strip()
        if not data:
            return
        message_type, sender_port = data.split()
        sender_port = int(sender_port)
        if message_type == "REQUEST":
            with lock:
                if requesting_cs:
                    time.sleep(random.uniform(0.5, 2))
                    print(f"[{port}] Deferring request from {sender_port}")
                else:
                    send_message(sender_port, "REPLY")
        elif message_type == "REPLY":
            with lock:
                reply_count += 1

def send_message(peer_port, message_type):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", peer_port))
        client.sendall(f"{message_type} {port}".encode())
        client.close()
    except:
        print(f"[{port}] Could not reach peer {peer_port}")

def request_critical_section():
    global requesting_cs, reply_count
    with lock:
        requesting_cs = True
        reply_count = 0
    print(f"[{port}] Requesting access to the critical section...")
    for peer in peers:
        send_message(peer, "REQUEST")
    while reply_count < len(peers):
        time.sleep(0.5)
    print(f"[{port}] ENTERED Critical Section")
    time.sleep(10)
    print(f"[{port}] EXITING Critical Section")
    with lock:
        requesting_cs = False
    for peer in peers:
        send_message(peer, "REPLY")

if __name__ == "__main__":
    port = int(input("Enter unique port number for this client: "))
    peers = list(map(int, input("Enter peer ports (space-separated): ").split()))
    threading.Thread(target=listener, daemon=True).start()
    while True:
        cmd = input("Type 'enter' to request critical section:").strip()
        if cmd == "enter":
            request_critical_section()
        elif cmd == "exit":
            break
