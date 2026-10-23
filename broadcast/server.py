import socket
s=socket.socket()
s.bind(("localhost",5000))
s.listen()
while True:
    c,addr=s.accept()
    msg=c.recv(1024).decode()
    print("message",msg)
    c.send("message received".encode())
    c.close()