# Kode Blue, 10/31/2020
# I feel like trash. If you want to know what this does, its basically ansible.
# Exec.py

import paramiko

# initialize SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname,username=username,password=password)
except:
    print("[!] Unable to connect to SSH Server. Exiting...")
    exit()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Execute shell commands on remote host")
    parser.add_argument("hostname", help="Host to exec commands on", default="127.0.0.1")
    parser.add_argument("username", help="User on host")
    parser.add_argument("password", help="Password of user")
    parser.add_argument("commands", "--scan-port", help="Scan a particular port", default="null")
    parser.add_argument("--whois", help="Perform whois querey on host", action = 'store_true')

    args = parser.parse_args()
