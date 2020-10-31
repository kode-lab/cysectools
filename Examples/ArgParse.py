# Kode Blue, 10/29/2020
# How to use ArgParse. yay!
# ArgParse.py

import argparse

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Scan for information about a remote host")
    parser.add_argument("-n", "--hostname", help="Host to Scan", default="null")
    parser.add_argument("-m", "--max-port", help="Scan for Open Ports, enter max port to scan", default="null")
    parser.add_argument("--min-port", help="Scan for Open ports, enter min port to scan", default = "null")
    parser.add_argument("-p", "--scan-port", help="Scan a particular port", default="null")
    parser.add_argument("--whois", help="Perform whois querey on host", action = 'store_true')

    args = parser.parse_args()
