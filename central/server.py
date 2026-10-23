import socket
s=socket.socket()
s.bind(("localhost",8000))
s.listen()
while True:
    c,addr=s.accept()
    msg=c.recv(1024).decode()
    print("Task:", msg)
    c.send("Task send by the controller".encode())
    c.close()
