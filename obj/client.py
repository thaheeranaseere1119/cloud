import socket
import pickle

s = socket.socket()
s.connect(("localhost", 8000))

arr = [10, 20, 30, 40]
s.send(pickle.dumps(arr))

msg = s.recv(1024).decode()
print("Sum:", msg)

s.close()