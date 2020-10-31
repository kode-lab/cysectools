# Kode Blue, 10/31/2020
# WMIC tools, Finally!
# WMIC.py

#!/usr/bin/python3

import wmi_client_wrapper as wmi

wmic = wmi.WmiClientWrapper(username=username,password=password,host=host,namespace=namespace,)

output = wmic.query("SELECT * FROM Win32_Processor")

print(output)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Use WMIC to scan for information about a remote host")
    parser.add_argument("n", "node", help="Node (host)  to Scan", default="localhost") #technically, Windows calls this a "node" (Its a host)
    parser.add_argument("--namespace", help="Namespace the alias will operate Against", default="null")

    parser.add_argument("--whois", help="Perform whois querey on host", action = 'store_true')

    args = parser.parse_args()
