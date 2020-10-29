# Kode Blue, 10/29/2020
# Tool for finding links on a domain (domain.com/link, /link/lowerlink, etc)

import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama

# initalize colorama, used for making the resulting links pretty
colorama.init()
GREEN = colorama.Fore.GREEN
BLUE = colorama.Fore.BLUE
RESET = colorama.Fore.RESET

internal_urls = set()
external_urls = set()

def is_valid(url):
    # Check if URL is valid
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_links(url):
    # Returns URL's found on 'url' which belongs to the same website
    urls = set()
    #domain name of the url sans protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue
        # join url if it's a relative url
        href = urljoin(url,href)
        parsed_href = urlparse(href)
        # remove URL GET params, URL fragments, other trash
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

        if not is_valid(href):
            # Not a vaild URL
            continue
        if href in internal_urls:
            # already in the set
            continue
        if domain_name not in href:
            # this is an external link
            if href not in external_urls:
                print(f"{BLUE}[!] External link: {href}{RESET}")
                external_urls.add(href)
            continue
        print(f"{GREEN}[*] Internal link: {href}{RESET}")
        urls.add(href)
        internal_urls.add(href)
    return urls

total_urls_visited = 0

def crawl(url,max_urls=50):
    #Crawl a web page to extract links
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)

if __name__ == "__main__":
    crawl("https://www.colostate.edu")
    print("[+] Total External Links: ",len(external_urls))
    print("[+] Total Internal Links: ",len(internal_urls))
    print("[+] Total: ",len(external_urls)+len(internal_urls))
