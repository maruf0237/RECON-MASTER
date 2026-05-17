import requests
from bs4 import BeautifulSoup


def find_js(url):
    print("\n[+] Finding JavaScript Files...")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for script in soup.find_all("script"):
            src = script.get("src")

            if src:
                print(src)

    except:
        print("JS scan failed")
