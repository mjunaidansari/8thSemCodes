import socket
import threading
import time

ports = [5001, 5002, 5003]
port = 0
peers = []
request_queue = []
has_token = False
lock = threading.Lock()
waiting_for_token = False

def listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", port))
    server.listen(5)
    print(f"[{port}] Listening for connections...")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_request, args=(conn,)).start()

def handle_request(conn):
    global has_token, waiting_for_token
    with conn:
        data = conn.recv(1024).decode().strip()
        if not data:
            return

        message_type, sender_port = data.split()
        sender_port = int(sender_port)

        if message_type == "REQUEST":
            with lock:
                request_queue.append(sender_port)
                print(f"[{port}] Received REQUEST from {sender_port}")

            if has_token and not waiting_for_token:
                send_token()

        elif message_type == "TOKEN":
            with lock:
                has_token = True
                waiting_for_token = False
                print(f"[{port}] Received TOKEN")
            enter_critical_section()

def send_message(peer_port, message_type):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", peer_port))
        client.sendall(f"{message_type} {port}".encode())
        client.close()
    except:
        print(f"[{port}] Could not reach peer {peer_port}")

def request_critical_section():
    global has_token, waiting_for_token
    if has_token:
        enter_critical_section()
    else:
        print(f"[{port}] Requesting token...")
        with lock:
            waiting_for_token = True
        for peer in peers:
            send_message(peer, "REQUEST")

def send_token():
    global has_token
    if request_queue:
        next_holder = request_queue.pop(0)
        send_message(next_holder, "TOKEN")
        with lock:
            has_token = False
        print(f"[{port}] Sent TOKEN to {next_holder}")

def enter_critical_section():
    print(f"[{port}] ENTERED Critical Section")
    time.sleep(2)
    print(f"[{port}] EXITING Critical Section")
    send_token()

if __name__ == "__main__":
    instance_number = int(input("Enter instance number (1, 2, 3): "))
    port = ports[instance_number - 1]
    peers = [p for p in ports if p != port]

    has_token = input("Token? ").strip().lower() == "yes"
    threading.Thread(target=listener, daemon=True).start()

    while True:
        cmd = input("\nRequest critical section?\n").strip()
        if cmd == "yes":
            request_critical_section()
        elif cmd == "exit":
            break
