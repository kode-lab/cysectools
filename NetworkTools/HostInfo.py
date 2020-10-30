# Kode Blue, 10/29/2020
# Combines several of the other scripts here to provide a super tool that
# can tell you a bunch of stuff about a machine

import argparse
import socket
import sys
from datetime import datetime
#from dns import reversename,resolver
import PortScanner.py

host = input("Enter the host to scan: ")
hostIP = socket.gethostbyname(host)
hostName = socket.gethostbyaddr(hostIP)

print("Hostname:   ",hostName[0])
print("IP Address: ",hostIP)

scanPorts(hostIP)

# TODO: add SMB funtionality
