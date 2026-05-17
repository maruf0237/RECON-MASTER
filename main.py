from modules.portscan import scan_ports
from modules.subdomain import find_subdomains
from modules.crawler import crawl_site
from modules.jsfinder import find_js
from modules.techdetect import detect_technology, get_headers
from modules.nikto_scan import run_nikto
from modules.nuclei_scan import run_nuclei
from modules.report import generate_report

target = input("Enter Target URL: ")

find_subdomains(target)
scan_ports(target)

crawl_site(target)
find_js(target)

detect_technology(target)
get_headers(target)

run_nikto(target)
run_nuclei(target)

generate_report(target)
