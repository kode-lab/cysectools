# Kode Blue, 10/29/2020
# A tool to scan for subdomains of a domain.
# TODO: add method for input of prefered domain

import requests
from threading  import Thread   # I'm impatient, ok?
from queue import Queue

q = Queue()      # thread-safe queue initalization
#exists = []

def scan_subdomains(domain):
    global q
    #global exists
    while True:
        # Get subdomain from queue
        subdomain = q.get()
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
        # done scanning that subdomain
        q.task_done()

def main(domain, n_threads, subdomains):
    global q

    # fill queue with all subdomains
    for subdomain in subdomains:
        q.put(subdomain)

    for t in range(n_threads):
        # Start all threads
        worker = Thread(target=scan_subdomains,args=(domain,))
        # this dameon thread will end when the main thread ends
        worker.daemon = True
        worker.start()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Faster Subdomain Scanner (it uses Threads!)")
    parser.add_argument("domain", help="Domain to scan for subdomains (don't include http://)")
    parser.add_argument("-l", "--wordlist" , help="File containing subdomains to scan, line by line.Default is subdomains.txt",
            default="subdomains.txt")
    parser.add_argument("-t", "--num-threads", help="Number of threads to use. Default is 10",
            default=10, type=int)
    args = parser.parse_args()
    domain = args.domain
    wordlist = args.wordlist
    num_threads = args.num_threads

    main (domain=domain, n_threads=num_threads, subdomains=open(wordlist).read().splitlines())
    q.join

