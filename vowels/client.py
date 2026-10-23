import socket

s = socket.socket()
s.connect(("localhost", 8000))

msg = input("Enter a string: ")
s.send(msg.encode())

print("Distinct vowels:", s.recv(1024).decode())
s.close()