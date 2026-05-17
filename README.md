# ⚡ RECONE-MASTER
### Automated Reconnaissance & Vulnerability Scanner

RECONE-MASTER is a lightweight, modular, CLI-based cybersecurity tool designed to automate reconnaissance and vulnerability scanning against authorized web targets.

The project performs:

- Reconnaissance
- Web Crawling
- JavaScript Extraction
- Technology Detection
- Port Scanning
- Vulnerability Scanning
- Report Generation

This tool was developed as an academic cybersecurity project for practical security assessment and attack surface discovery.

---

# ⚠️ Legal Notice

This project is intended strictly for:

- Educational purposes
- Lab environments
- Authorized penetration testing

Do NOT scan systems without permission.

The developer is not responsible for any misuse of this tool.

---

# 🚀 Features

| Module | Capabilities |
|--------|--------------|
| Reconnaissance | Subdomain Discovery, Port Scanning, HTTP Header Collection, Technology Detection |
| Web Crawling | URL Crawling, Endpoint Collection, Form & Parameter Discovery |
| JavaScript Analysis | JavaScript File Extraction |
| Vulnerability Scanning | Nikto Integration + Nuclei Integration |
| Reporting | TXT Report Generation |

---

# 🔍 Reconnaissance Features

- Subdomain Enumeration
- Open Port Scanning
- HTTP Header Collection
- Technology Fingerprinting
- Target Enumeration
- Basic Service Detection

---

# 🕷️ Crawling Features

- Link Crawling
- Endpoint Discovery
- Parameter Collection
- Form Enumeration
- JavaScript File Extraction

---

# 🛡️ Vulnerability Scanning Features

## Nikto Integration

RECONE-MASTER integrates with:

- Nikto Web Scanner
- Web Server Security Checks
- Misconfiguration Detection
- Outdated Service Detection

---

## Nuclei Integration

RECONE-MASTER integrates with:

- Nuclei Templates
- Vulnerability Detection
- Exposure Detection
- Security Misconfiguration Detection

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/RECONE-MASTER.git

cd RECONE-MASTER
```

---

# 🐍 Create Virtual Environment (Recommended)

## Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

## Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

# 📥 Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# 📥 Install Nikto

## Ubuntu / Kali Linux

```bash
sudo apt update

sudo apt install nikto
```

---

# 📥 Install Nuclei

```bash
sudo apt install nuclei
```

Update Templates:

```bash
nuclei -update-templates
```

---

# ⚙️ Usage

## Basic Usage

```bash
python main.py
```

Then enter target:

```text
https://testphp.vulnweb.com
```

---

# 💻 Example Output

```text
[+] Finding Subdomains...

www.testphp.vulnweb.com
api.testphp.vulnweb.com

[+] Scanning Open Ports...

Port 80 is OPEN
Port 443 is OPEN

[+] Crawling Website...

/login.php
/register.php

[+] Finding JavaScript Files...

/js/main.js

[+] Detecting Technologies...

Apache
PHP
jQuery

[+] Running Nikto Scan...

[+] Running Nuclei Scan...

[+] Report Saved: reports/report.txt
```

---

# 🏗️ Project Structure

```text
RECONE-MASTER/
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
└── reports/
    └── report.txt
```

---

# 📄 Report Generation

RECONE-MASTER generates a report containing:

- Target Information
- Open Ports
- Subdomains
- HTTP Headers
- Technologies
- Crawled URLs
- JavaScript Files
- Nikto Findings
- Nuclei Findings
- Scan Timestamp

Generated Report Location:

```text
reports/report.txt
```

---

# 🧪 Tested Environment

- Python 3.10+
- VS Code
- Kali Linux
- Ubuntu
- Windows 11 (WSL)

---

# 📚 Educational Purpose

This project was developed for:

- Cybersecurity Learning
- Penetration Testing Practice
- Web Security Assessment
- Academic Project Submission

---

# 🤝 Future Improvements

Planned future improvements:

- Recursive Crawling
- HTML Report Generation
- Multi-threading
- Better Vulnerability Detection
- JSON Report Support
- Docker Support

---

# 👨‍💻 Author

Name: Md. Maruful Islam
Project: RECONE-MASTER  
Course: Cyber Security / Penetration Testing  

---

# 📜 License

MIT License © 2026 RECONE-MASTER

This project is free to use for educational and research purposes.

---
