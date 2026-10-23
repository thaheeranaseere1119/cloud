import socket
s=socket.socket()
s.connect(("localhost",5000))
msg=input("enter message")
s.send(msg.encode())
print(s.recv(1024).decode())
s.close()