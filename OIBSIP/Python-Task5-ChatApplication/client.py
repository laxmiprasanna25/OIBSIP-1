
import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter your username: ")

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")

            if message == "USERNAME":
                client.send(username.encode("utf-8"))
            else:
                print("\n" + message)

        except:
            print("Connection closed.")
            client.close()
            break

def send_messages():
    while True:
        message = input()

        if message.lower() == "exit":
            client.close()
            break

        full_message = username + ": " + message
        try:
            client.send(full_message.encode("utf-8"))
        except:
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
