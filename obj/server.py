import socket
import pickle

s = socket.socket()
s.bind(("localhost", 8000))
s.listen()

print("Server started")

c, addr = s.accept()

data = c.recv(1024)
arr = pickle.loads(data)

total = sum(arr)
c.send(str(total).encode())

c.close()
