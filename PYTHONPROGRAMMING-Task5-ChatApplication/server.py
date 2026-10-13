import socket
import threading
from datetime import datetime

HOST = "localhost"
PORT = 5555

clients = []


def get_time():
    return datetime.now().strftime("%H:%M")


def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                pass


def handle_client(client, address):
    print(f"Client connected: {address}")

    try:
        # Receive client's name
        name = client.recv(1024).decode()

        client.send("Connected to the chat server!".encode())

        # Tell everyone else that this user joined
        join_message = f"[{get_time()}] {name} joined the chat."
        print(join_message)
        broadcast(join_message, client)

        while True:
            message = client.recv(1024).decode()

            if not message:
                break

            formatted_message = f"[{get_time()}] {name}: {message}"

            print(formatted_message)
            broadcast(formatted_message, client)

    except:
        pass

    finally:
        if client in clients:
            clients.remove(client)

        disconnect_message = f"[{get_time()}] {name} disconnected."
        print(disconnect_message)

        broadcast(disconnect_message, client)

        client.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))
    server.listen(2)

    print("================================")
    print("      CHAT SERVER STARTED")
    print("================================")
    print(f"Listening on {HOST}:{PORT}")
    print("Waiting for clients...\n")

    while True:
        client, address = server.accept()

        if len(clients) >= 2:
            client.send("Chat room is full.".encode())
            client.close()
            continue

        clients.append(client)

        thread = threading.Thread(
            target=handle_client,
            args=(client, address)
        )

        thread.start()


start_server()