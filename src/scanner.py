import socket
import sys


def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.2)

    result = sock.connect_ex((target, port))

    sock.close()

    return result == 0


if len(sys.argv) < 2:
    print("Usage: python scanner.py <target>")
    sys.exit(1)

target = sys.argv[1]

try:
    ip = socket.gethostbyname(target)
    print(f"Target: {target}")
    print(f"IP: {ip}")
except socket.gaierror:
    print(f"[!] Could not resolve target: {target}")
    sys.exit(1)

print(f"Scanning {target}...")

for port in range(7995, 8005):
    if scan_port(target, port):
        print(f"[+] Port {port} OPEN")

print("Scan complete!")