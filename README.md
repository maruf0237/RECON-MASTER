# ⚡ RECONE-MASTER  
### Automated Reconnaissance & Vulnerability Scanner

RECONE-MASTER is a modular, CLI-based cybersecurity tool that automates the full reconnaissance → crawling → vulnerability scanning → reporting workflow against authorized web targets.

The tool is designed for penetration testing practice, attack surface discovery, vulnerability assessment, and educational cybersecurity projects.

---

# ⚠️ Legal Notice

This tool is created strictly for educational and authorized security testing purposes only.

Use RECONE-MASTER only on:

- Systems you own
- Local lab environments
- Authorized bug bounty targets
- Targets with explicit written permission

Unauthorized scanning is illegal in many jurisdictions.

The developer is not responsible for misuse of this project.

---

# 📸 Screenshots

## Main Interface

![Main Interface](screenshots/main.png)

## HTML Report

![HTML Report](screenshots/report.png)

---

# 🚀 Features

| Module | Capabilities |
|--------|--------------|
| Recon | DNS Enumeration, Subdomain Discovery, WHOIS Lookup, HTTP Header Analysis, Technology Fingerprinting, Port Scanning |
| Crawler | Recursive Crawling, JS Extraction, Parameter Discovery, Form Enumeration |
| Vulnerability Scanner | Custom Checks + Nikto Integration + Nuclei Integration |
| Reporter | TXT Report, JSON Report, HTML Report (Optional) |

---

# 🔍 Reconnaissance Features

- Subdomain Enumeration
- Open Port Scanning
- Banner Grabbing
- DNS Information Gathering
- WHOIS Lookup
- HTTP Header Collection
- Web Technology Detection
- Target Fingerprinting
- JavaScript File Discovery
- Endpoint Collection
- URL Extraction

---

# 🕷️ Crawling Features

- Recursive BFS Crawling
- Link Extraction
- Form Detection
- Parameter Collection
- JavaScript Analysis
- Interesting Path Discovery
- Sensitive File Detection
- Secret Pattern Detection

---

# 🛡️ Vulnerability Scanning Features

## Custom Vulnerability Checks

- Security Header Analysis
- Missing CSP Detection
- Missing HSTS Detection
- Missing X-Frame-Options
- CORS Misconfiguration
- Clickjacking Detection
- Cookie Security Analysis
- Information Disclosure
- Dangerous HTTP Methods
- SSL/TLS Enforcement Check
- Directory Listing Detection
- Default Credential Detection
- Open Redirect Detection
- SQL Injection Testing
- Reflected XSS Detection
- XXE Detection
- SSRF Detection
- Local File Inclusion Detection

---

# ⚡ External Tool Integrations

## Nikto Integration

RECONE-MASTER integrates with:

- Nikto Web Scanner
- Web Server Misconfiguration Detection
- Sensitive File Detection
- Outdated Server Detection

Example:

```bash
nikto -h example.com
```

---

## Nuclei Integration

RECONE-MASTER integrates with:

- Nuclei Templates
- CVE Detection
- Exposure Detection
- Misconfiguration Detection
- Technology Detection

Example:

```bash
nuclei -u https://example.com
```

---

# 🎁 Bonus Features

✅ Recursive Crawling  
✅ Multi-threading Support  
✅ Smart Result Deduplication  
✅ HTML Report Generation  
✅ JSON Export  
✅ Docker Support  
✅ AI-assisted Executive Summary  
✅ Stealth / Rate Limiting  
✅ Modular Architecture  

---

# 📦 Installation

# Option 1 — Local Installation (Python 3.10+)

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/RECONE-MASTER.git

cd RECONE-MASTER
```

---

## Create Virtual Environment (Recommended)

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📥 Install Nikto

## Kali Linux / Ubuntu

```bash
sudo apt update

sudo apt install nikto
```

---

# 📥 Install Nuclei

## Ubuntu / Kali

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
python main.py -t example.com
```

---

# 📌 Required Argument

| Argument | Description |
|----------|-------------|
| -t, --target | Domain, URL, Subdomain, or IP Address |

---

# ⚙️ Scan Options

| Argument | Default | Description |
|----------|---------|-------------|
| --ports | Common Web Ports | Custom Ports / Range |
| --threads | 10 | Number of Threads |
| --depth | 2 | Crawling Depth |
| --timeout | 10 | Request Timeout |
| --rate-limit | 0.1 | Delay Between Requests |
| --user-agent | RECONE-MASTER | Custom User-Agent |

---

# 🧩 Module Toggles

| Argument | Description |
|----------|-------------|
| --skip-recon | Skip Recon Phase |
| --skip-crawl | Skip Crawling |
| --skip-vuln | Skip Vulnerability Scanning |
| --skip-nikto | Skip Nikto |
| --skip-nuclei | Skip Nuclei |

---

# 📤 Output Options

| Argument | Description |
|----------|-------------|
| --output-dir | Custom Report Directory |
| --html | Generate HTML Report |
| --json | Generate JSON Report |
| --ai-summary | AI Executive Summary |
| --quiet | Quiet Mode |
| --no-color | Disable ANSI Colors |

---

# 💻 Examples

## Basic Scan

```bash
python main.py -t example.com
```

---

## Full Scan with HTML Report

```bash
python main.py -t example.com --html
```

---

## Aggressive Scan

```bash
python main.py -t 192.168.1.1 --ports 1-65535 --depth 4 --threads 20
```

---

## Stealth Mode

```bash
python main.py -t example.com --rate-limit 1.0 --threads 3
```

---

## Custom Checks Only

```bash
python main.py -t example.com --skip-nikto --skip-nuclei
```

---

# 🏗️ Project Architecture

```text
RECONE-MASTER/
├── main.py
├── requirements.txt
├── README.md
├── Dockerfile
├── docker-compose.yml
│
├── modules/
│   ├── recon.py
│   ├── crawler.py
│   ├── vuln_scanner.py
│   ├── nikto_scan.py
│   ├── nuclei_scan.py
│   └── report_generator.py
│
├── utils/
│   ├── console.py
│   ├── validator.py
│   └── http_client.py
│
├── reports/
│   └── sample_report.json
│
└── screenshots/
```

---

# 📄 Report Format

## JSON Report

Generated File:

```text
report_<target>_<timestamp>.json
```

### Structure

```json
{
  "meta": {},
  "recon": {},
  "crawl": {},
  "vulns": {}
}
```

---

# 🌙 HTML Report

Professional dark-mode HTML report including:

- Severity Statistics
- Vulnerability Tables
- Open Ports
- DNS Information
- Technology Badges
- JS Files
- Parameters
- Findings Summary

---

# 🤖 AI Executive Summary

RECONE-MASTER supports AI-generated executive summaries.

Requires:

```bash
export ANTHROPIC_API_KEY=YOUR_API_KEY
```

The AI summary provides:

- Risk Assessment
- Top Vulnerabilities
- Business Impact
- Recommended Fixes

---

# 🐳 Docker Support

## Build Docker Image

```bash
docker build -t recone-master .
```

---

## Run Container

```bash
docker run recone-master
```

---

# ✅ Tested Environments

- Python 3.10
- Python 3.11
- Ubuntu 22.04
- Kali Linux
- Windows 11 (WSL)
- Docker

---

# 📚 Educational Purpose

This project was developed for:

- Cybersecurity Learning
- Penetration Testing Practice
- Web Security Assessment
- Academic Project Submission

---

# 🤝 Contributing

Contributions are welcome.

## Steps

1. Fork Repository
2. Create Feature Branch
3. Add Improvements
4. Submit Pull Request

---

# 📜 License

MIT License © 2026 RECONE-MASTER

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to use, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

The Software is provided "AS IS", without warranty of any kind.

---

# 👨‍💻 Author

Name: Your Name  
Project: RECONE-MASTER  
Course: Cyber Security / Penetration Testing  
Department: Computer Science & Engineering  

---

# ⭐ Support

If you like this project:

⭐ Star the repository  
🍴 Fork the project  
🐛 Report issues  
📢 Share with others  
