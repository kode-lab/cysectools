# Kode Blue, 10/29/2020
# Script for scanning for Open ports on a machine
# PortScanner.py

import socket
import sys

def scanPorts(host):
    print("Scanning host ", host)
    try:
        for port in range(1,1024):
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

# Get user input
remoteServer = input("Enter the remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

scanPorts(remoteServerIP)
