# Kode Blue, 10/29/2020
# Script for scanning for Open ports on a machine
# PortScanner.py

import socket
import sys

def scan_ports(host,maxPorts=1024):
    try:
        for port in range(1,maxPorts):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            if result == 0:
                print("Port {}:    Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("Keyboard Interrupt...Exiting")
        sys.exit()

    except socket.gaierror:
        print("Unable to resolve Hostname. Exiting")
        sys.exit()

    except socket.error:
        print("Unable to reach server.")
        sys.exit()

def scan_port(host,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host,port))
        if result == 0:
            print("Port {}:    Open".format(port))
        sock.close()
    except:
        print("Port {}:    Closed".format(port))

def main():
    # Get user input
    remoteServer = input("Enter the remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("Scanning Host: ", remoteServerIP)
    scan_ports(remoteServerIP)

if __name__ == "__main__":
   main() 
