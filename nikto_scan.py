import os


def run_nikto(target):
    print("\n[+] Running Nikto Scan...")
    os.system(f"nikto -h {target}")
