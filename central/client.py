import socket
s=socket.socket()
s.connect(("localhost",8000))
s.send("REquest for resouce".encode())
msg=s.recv(1024).decode()
print(msg)
s.close()