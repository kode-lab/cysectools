# Kode Blue, 10/29/2020
# Tool for scanning for hosts on a network
# Cheers!
# NetworkScanner.py

# TODO what the heck kind of datatype is "clients"?

from scapy.all import ARP, Ether, srp  # import tools from scapy (no need to reinvent the wheel :)

def scan_network(target):
    """
    Returns data of clients on the scanned network
    """
    arp = ARP(pdst=target)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    packet = ether/arp
    
    result = srp (packet, timeout=3)[0]
    
    clients=[]
    
    for sent, received in result:
        clients.append({"ip": received.psrc, 'mac': received.hwsrc})
    
    return clients

def main(target):
    clients = scan_network(target)
    
    print("Available Devices on the Network: ")
    print("IP" + " "*18 + "MAC")
    
    for client in clients:
        print("{:16}      {}".format(client['ip'], client['mac']))

if __name__ == "__main__":
    target_ip = input("Which IP to scan? Default 192.168.1.1/24 : ")
    if target_ip == "":
        target_ip = "192.168.1.1/24"      # IP address for the destination. 
    main(target_ip)
