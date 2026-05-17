import requests
from bs4 import BeautifulSoup


def crawl_site(url):
    print("\n[+] Crawling Website...")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href")

            if href:
                print(href)

    except:
        print("Crawling failed")
