from datetime import datetime


def generate_report(target):
    filename = "reports/report.txt"

    with open(filename, "w") as file:
        file.write("Recon Report\n")
        file.write(f"Target: {target}\n")
        file.write(f"Time: {datetime.now()}\n")

    print("\n[+] Report Saved:", filename)
