import requests
import builtwith

def detect_technology(url):

    print("\n[+] Detecting Technologies...")

    try:
        tech = builtwith.parse(url)

        if tech:
            for key, value in tech.items():
                print(f"{key}: {', '.join(value)}")

        else:
            print("No technology detected")

    except Exception as e:
        print("Technology detection failed:", e)


def get_headers(url):

    print("\n[+] Collecting HTTP Headers...")

    try:
        response = requests.get(url)

        headers = response.headers

        for key, value in headers.items():
            print(f"{key}: {value}")

    except Exception as e:
        print("Header collection failed:", e)
