
import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

clients = []
usernames = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                client.close()

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            break

    if client in clients:
        index = clients.index(client)
        username = usernames[index]
        clients.remove(client)
        usernames.remove(username)
        broadcast(f"{username} left the chat.".encode("utf-8"), client)
        print(f"{username} disconnected.")

    client.close()

def receive_connections():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print("Chat server is running...")
    print(f"Listening on port {PORT}")

    while True:
        client, address = server.accept()
        client.send("USERNAME".encode("utf-8"))

        username = client.recv(1024).decode("utf-8")

        clients.append(client)
        usernames.append(username)

        print(f"{username} connected from {address}")

        broadcast(f"{username} joined the chat.".encode("utf-8"), client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive_connections()
