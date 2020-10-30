# Kode Blue, 10/29/2020
# Combines several of the other scripts here to provide a super tool that
# can tell you a bunch of stuff about a particular machine
# HostInfo.py

import argparse
import socket
import sys
from datetime import datetime
#from dns import reversename,resolver
from PortScanner import scan_ports,scan_port

def name_info(host):
    """
    Prints Hostname and IP Addr, Returns <IP Address>
    """
    hostIP = socket.gethostbyname(host)
    hostName = socket.gethostbyaddr(hostIP)
    print("Hostname:    ",hostName[0])
    print("IP Addrs:    ",hostIP)
    return hostIP

# TODO: add SMB funtionality

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Scan for information about a remote host")
    parser.add_argument("-n", "--hostname", help="Host to Scan", default="null")
    parser.add_argument("-S", "--scan-ports", help="Scan for Open Ports, enter max port to scan", default="null")
    parser.add_argument("-p", "--scan-port", help="Scan a particular port", default="null")
    parser.add_argument("--whois", help="Perform whois querey on host")

    args = parser.parse_args()

    if args.hostname == "null":
        host = input("Enter the host to scan: ")
    else:
        host = args.hostname

    ipAddr = name_info(host)

    if not (args.scan_ports == "null"):
        #scan_ports(ipAddr,int(args.scan_ports))
        print("debug")
    if not (args.scan_port == "null"):
        #scan_port(ipAddr,int(args.scan_ports))
        print("debug")
    
    if args.whois:
        print("="*10,"[WHOIS]","="*10)
        whois_Information(hostName)
