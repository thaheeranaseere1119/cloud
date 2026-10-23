import socket

s = socket.socket()
s.bind(("localhost", 8000))
s.listen()

print("Waiting for client...")
c, addr = s.accept()
print("Client connected")

while True:
    msg = c.recv(1024).decode()
    print("Client:", msg)

    if msg.lower() == "bye":
        break

    reply = input("Server: ")
    c.send(reply.encode())

    if reply.lower() == "bye":
        break

c.close()
s.close()