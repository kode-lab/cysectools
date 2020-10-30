# Kode Blue, 10/29/2020
# A tool to scan for subdomains of a domain.
# TODO: add method for input of prefered domain

import requests

domain="colostate.edu"

file = open("subdomains.txt")

subdomains=file.read().splitlines()

for subdomain in subdomains:
    # Make the url;scan the subdomain
    url = f"http://{subdomain}.{domain}"
    try:
        # If there is an error, the subdomain (probably) doesn't exist
        requests.get(url)
    except requests.ConnectionError:
        # Assume subdomain doesn't exist, do nothing
        pass
    else:
        #exists.append("Subdomain Exists:", url)
        print("[+] Subdomain exists: ",url)
