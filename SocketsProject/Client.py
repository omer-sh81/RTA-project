import socket
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))
while True:
    print("Enter any command, if you are willing to stop send exit.")
    command= input()
    s.send(base64.b64encode((command).encode()))
    if command == "exit":
        s.close()
        break
    data = (base64.b64decode(s.recv(4096))).decode()
    print(data)
