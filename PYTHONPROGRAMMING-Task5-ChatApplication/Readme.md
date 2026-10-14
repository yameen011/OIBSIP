# Basic Chat Application

A simple two-person, terminal-based chat application built with Python sockets and threads. One server accepts up to two clients, and messages sent by one client are broadcast to the other with a timestamp.

## Features

- Client-server architecture using TCP sockets
- Real-time messaging using threads (sending and receiving happen at the same time)
- Timestamped messages in `[HH:MM] name: message` format
- Join and disconnect notifications for other users
- Chat room limited to 2 clients; extra connections are told "Chat room is full."
- Type `quit` to leave the chat cleanly
- Friendly error message if the server is not running

## Project Structure

```
.
├── server.py   # Chat server
├── client.py   # Chat client
└── README.md
```

## Requirements

- Python 3.6 or newer
- No external packages needed (uses only `socket`, `threading` and `datetime` from the standard library)

## Usage

### 1. Start the server

Open a terminal and run:

```bash
python server.py
```

You should see:

```
================================
      CHAT SERVER STARTED
================================
Listening on localhost:5555
Waiting for clients...
```

### 2. Start the clients

Open two more terminals (one per user) and run in each:

```bash
python client.py
```

Enter a name when asked, then start typing messages.

### Example

**Client 1 (Ali)**

```
Enter your name: Ali
Connected to the chat server!

Type your messages below.
Type 'quit' to leave the chat.

You: Hello!

[22:50] Sara: Hi Ali!
You:
```

**Client 2 (Sara)**

```
Enter your name: Sara
Connected to the chat server!

[22:49] Ali joined the chat.
[22:50] Ali: Hello!
You: Hi Ali!
```

## How It Works

**Server (`server.py`)**

1. Creates a TCP socket, binds it to `localhost:5555` and listens for connections.
2. For every new client, checks that the room is not full (max 2), then starts a new thread running `handle_client()`.
3. `handle_client()` reads the user's name, announces the join, and then keeps receiving messages and forwarding them to the other client with `broadcast()`.
4. When a client disconnects, it is removed from the list and the other user is notified.

**Client (`client.py`)**

1. Connects to the server and sends the user's name.
2. Starts a background thread (`receive_messages`) that prints incoming messages.
3. The main thread reads user input and sends it to the server until the user types `quit`.

## Configuration

Both files have these values at the top:

```python
HOST = "localhost"
PORT = 5555
```

- To chat across different computers on the same network, set the server's `HOST` to `"0.0.0.0"` and the client's `HOST` to the server machine's local IP address.
- Make sure the port is allowed through the firewall.
- Both files must use the same `PORT`.

## Troubleshooting

- **"Could not connect to the server."**: start `server.py` first and check that `HOST` and `PORT` match.
- **"Chat room is full."**: the server accepts only 2 clients at a time. Change the limit in `start_server()` (`len(clients) >= 2`) and `server.listen()` to allow more.
- **"Address already in use"**: a previous server instance is still running. Close it or change the port.

## Known Limitations and Ideas for Improvement

- Only text messages up to 1024 bytes are supported
- No encryption, so don't use it for sensitive messages
- If a client disconnects before sending its name, the server's cleanup code can fail because `name` is not defined yet
- Ideas: support more users, private messages, a user list command, message history, or a GUI with Tkinter

## License

This project is free to use and modify for personal and educational purposes.