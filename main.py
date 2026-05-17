from modules.report import generate_report
from modules.nuclei_scan import run_nuclei
from modules.nikto_scan import run_nikto
from modules.jsfinder import find_js
from modules.crawler import crawl_site
from modules.subdomain import find_subdomains
from modules.portscan import scan_ports
target = input("Enter Target: ")

print("Target Selected:", target)
print("Starting Scan...")

target = input("Enter Target: ")

find_subdomains(target)
scan_ports(target)
crawl_site(target)
find_js(target)
run_nikto(target)
run_nuclei(target)
generate_report(target)
