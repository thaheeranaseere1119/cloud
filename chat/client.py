import socket

s = socket.socket()
s.connect(("localhost", 8000))

while True:
    msg = input("Client: ")
    s.send(msg.encode())

    if msg.lower() == "bye":
        break

    reply = s.recv(1024).decode()
    print("Server:", reply)

    if reply.lower() == "bye":
        break

s.close()