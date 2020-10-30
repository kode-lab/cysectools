# Kode Blue, 10/29/2020
# Mostly followed this tutorial: https://www.thepythoncode.com/article/building-network-scanner-using-scapy
# Cheers!

# TODO include info for CIDR notation

from scapy.all import ARP, Ether, srp  # import tools from scapy (no need to reinvent the wheel :)

target_ip = input("Which IP to scan? Default 192.164.1.1/24 : ")
if target_ip == "":
    target_ip = "192.164.1.1/24"      # IP address for the destination. 

arp = ARP(pdst=target_ip)   # Create the ARP packet

ether = Ether(dst="ff:ff:ff:ff:ff:ff")     # Create Ether broadcast packet (MAC here indicates broadcasting)

packet = ether/arp     # Stack the two packets

result = srp(packet, timeout=3)[0]     # send the packets (srp()) over Layer 2, timeout 3 so the script dont get stuck

clients = []

for sent, received in result:
    # For each response, append ip and mac address to the list 'clients'
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# PRINT the resulting list of clients
print("Available Devices on the network:")
print("IP"+" "*18+"MAC")

for client in clients:
    print("{:16}      {}".format(client['ip'], client['mac']))


