def find_subdomains(domain):
    print("\n[+] Finding Subdomains...")

    common = ["www", "mail", "api", "admin"]

    for sub in common:
        print(f"{sub}.{domain}")
