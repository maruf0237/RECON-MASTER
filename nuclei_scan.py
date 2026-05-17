import os


def run_nuclei(target):
    print("\n[+] Running Nuclei Scan...")
    os.system(f"nuclei -u {target}")
