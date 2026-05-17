import socket


def scan_ports(target):
    print("\n[+] Scanning Open Ports...")

    ports = [21, 22, 80, 443, 8080]

    for port in ports:
        s = socket.socket()
        s.settimeout(1)

        if s.connect_ex((target, port)) == 0:
            print(f"Port {port} is OPEN")

        s.close()
