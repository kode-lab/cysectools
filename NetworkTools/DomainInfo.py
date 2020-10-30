# Kode Blue, 10/29/30
# Script for getting whois informaiton about a Domain Name
# DomainInfo.py

import requests
import whois 
from threading import Thread
from queue import Queue
import sys

q = Queue()

def scan_subdomains(domain):
    global q
    while True:
        # Get subdomain from Queue
        subdomain = q.get()
        # scan subdomain
        url= f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        except KeyboardInterrupt:
            print("Keyboard Interrupt. Exiting.")
            sys.exit()
        else:
            print("[+] Discovered Subdomain: ", url)

        q.task_done()

def is_registered(domain_name):
    """
    Returns boolean indicating if 'domain_name' is registered
    """
    try: 
        w= whois.whois(domain_name)
    except Exception:
        return FALSE
    else:
        return bool(w.domain_name)

def main(domain,n_threads,subdomains):
    global q
    
    # Domain Information
    print("Domain Information for: ", domain)
    domain_information(domain)
    
    for subdomain in subdomains:
        q.put(subdomain)
    for t in range(n_threads):
        # Start all threads
        worker = Thread(target=scan_subdomains, args=(domain,))
        worker.daemon = True
        worker.start()

def domain_information(domain):
    if is_registered(domain):
        whois_info = whois.whois(domain)
        print("Domain Registrar: ", whois_info.registrar)
        print("WHOIS Server: ", whois_info.whois_server)
        print("Creation Date: ", whois_info.creation_date)
        print("Expiration Date: ", whois_info.expiration_date)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Faster Subdomain Scanner")
    parser.add_argument("-d")
    parser.add_argument("-l", default="subdomains.txt")
    parser.add_argument("-n", default=10)

    args = parser.parse_args()
    domain = args.d
    wordlist = args.l
    num_threads = int(args.n)

    main(domain=domain,n_threads=num_threads,subdomains=open(wordlist).read().splitlines())
    q.join()
    print("Done")
