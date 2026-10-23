import socket

s = socket.socket()
s.bind(("localhost", 8000))
s.listen()

print("Server started")

c, addr = s.accept()
msg = c.recv(1024).decode()

vowels = set("aeiou")
count = len(set(msg.lower()) & vowels)

c.send(str(count).encode())
c.close()
s.close()