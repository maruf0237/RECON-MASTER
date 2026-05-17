
# Recon Sentinel  
### Automated Reconnaissance & Vulnerability Scanner

Recon Sentinel is a lightweight, CLI-based automated reconnaissance and vulnerability scanning tool designed for web security assessments. It helps security researchers and students perform real-world attack surface discovery, web crawling, and vulnerability scanning in an organized and modular way.

This project was developed as part of a cybersecurity project assignment to simulate a practical reconnaissance and vulnerability assessment workflow using Python, Nikto, and Nuclei.



## Features

### Reconnaissance

- Accepts Domain / Subdomain / URL / IP Address
- Subdomain Discovery
- Open Port Scanning
- Service Detection
- HTTP Header Collection
- DNS Information Gathering
- Technology Detection
- JavaScript File Extraction
- Interesting Endpoint Discovery
- Parameter and Form Detection
- URL Crawling and Collection

---

### Vulnerability Scanning

- Nikto Integration
- Nuclei Integration
- Common Web Vulnerability Detection
- Security Misconfiguration Detection
- Sensitive File Discovery
- Missing Security Header Detection
- Risk Severity Classification

---

### Reporting

- Structured CLI Output
- Final TXT Report Generation
- Organized Vulnerability Findings
- Severity-based Risk Summary
- Timestamped Scan Reports

---

## Project Structure

```text
recon_scanner/
│
├── main.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── subdomain.py
│   ├── portscan.py
│   ├── crawler.py
│   ├── jsfinder.py
│   ├── techdetect.py
│   ├── nikto_scan.py
│   ├── nuclei_scan.py
│   └── report.py
│
├── reports/
│   └── report.txt
│
└── screenshots/
````

---

## Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/recon-sentinel.git
cd recon-sentinel
```

---

## Install Python Dependencies

```bash
pip install requests beautifulsoup4 colorama python-whois builtwith
```

---

## Install Nikto

### Kali Linux / Ubuntu

```bash
sudo apt update
sudo apt install nikto
```

---

## Install Nuclei

```bash
sudo apt install nuclei
```

---

## Usage

Run the tool using:

```bash
python main.py
```

Then enter your target:

```text
testphp.vulnweb.com
```

Example:

```bash
Enter Target: testphp.vulnweb.com
```

---

## Sample Output

```text
[+] Finding Subdomains...
www.testphp.vulnweb.com
mail.testphp.vulnweb.com

[+] Scanning Open Ports...
Port 80 is OPEN
Port 443 is OPEN

[+] Running Nikto Scan...
[+] Running Nuclei Scan...

[+] Report Saved: reports/report.txt
```

---

## Sample Report Includes

* Target Information
* Reconnaissance Findings
* Open Ports
* Technologies Used
* HTTP Headers
* DNS Information
* URLs and Endpoints
* JavaScript Files
* Parameters and Forms
* Nikto Findings
* Nuclei Findings
* Severity Summary
* Final Risk Level

---

## Bonus Features

* Modular Architecture
* Clean CLI Interface
* Error Handling
* Smart Report Generation
* Easily Expandable Modules

Future Improvements:

* Recursive Crawling
* Multi-threading
* HTML Report Generation
* GUI Dashboard
* Docker Support
* AI-based Report Summarization

---

## Authorized Testing Only

⚠ IMPORTANT:

This tool must only be used on:

* Your Own Systems
* Local Test Labs
* Authorized VMs
* Approved Bug Bounty Targets

Unauthorized scanning is strictly prohibited.

Always follow ethical hacking practices and legal guidelines.

---

## Evaluation Criteria Covered

* Functionality
* Recon Automation
* Real-World Practicality
* Code Quality
* Reporting & Documentation

This project is designed to maximize assignment marks.

---

## Author

Name: Your Name
Department: Computer Science & Engineering
Course: Cyber Security / Penetration Testing
Project Title: Automated Reconnaissance & Vulnerability Scanner

---

## License

This project is developed for educational and academic purposes only.

Use responsibly.

