import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama

internal_urls = set()
external_urls = set()

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    urls = set()
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        if href in internal_urls:
            # already in the set
            continue
        if domain_name not in href:
            # external link
            continue
        urls.add(href)
        internal_urls.add(href)
    return urls


total_urls_visited = 0

def crawl(url, max_urls=50):
    """
    Crawls a web page and extracts all links.
    You'll find all links in `external_urls` and `internal_urls` global set variables.
    params:
        max_urls (int): number of max urls to crawl, default is 50.
    """
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)


if __name__ == "__main__":
    crawl("https://www.nytimes.com/")
    print("[+] Total Internal links:", len(internal_urls))
    with open('urls.txt', 'w') as output:
        for link in internal_urls:
            if link.endswith("html"):
                output.write(link+"\n")



