import socket
import threading

HOST = "localhost"
PORT = 5555


def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                print("\nDisconnected from server.")
                break

            print("\n" + message)
            print("You: ", end="", flush=True)

        except:
            print("\nDisconnected from server.")
            break


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
    except:
        print("Could not connect to the server.")
        return

    print("================================")
    print("       CHAT APPLICATION")
    print("================================")

    name = input("Enter your name: ")

    # Send name to server
    client.send(name.encode())

    # Receive connection message
    message = client.recv(1024).decode()
    print(message)

    # Start receiving messages in another thread
    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client,),
        daemon=True
    )

    receive_thread.start()

    print("\nType your messages below.")
    print("Type 'quit' to leave the chat.\n")

    while True:
        try:
            message = input("You: ")

            if message.lower() == "quit":
                break

            if message.strip():
                client.send(message.encode())

        except:
            break

    print("Disconnecting...")
    client.close()


start_client()