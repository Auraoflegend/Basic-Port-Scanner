import socket
import sys
from datetime import datetime
import requests

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False



def tcp_scan(ip, start_port, end_port):
    open_ports = []
    print(f"\n[*] Starting TCP scan on target from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
        except socket.error:
            continue
    return open_ports

def udp_scan(ip, start_port, end_port):
    open_ports = []
    print(f"\n[*] Starting UDP scan on target from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(1)
                s.sendto(b"", (ip, port))
                try:
                    data, _ = s.recvfrom(1024)
                    open_ports.append(port)
                except socket.timeout:
                    open_ports.append(port)
        except socket.error:
            continue
    return open_ports

def generate_report(ip, scan_type, open_ports, start_port, end_port):
    filename = "scan_report.txt"
    with open(filename, "a+") as f:
        f.write("===== Port Scan Report =====\n")
        f.write(f"Target IP       : {ip}\n")
        f.write(f"Scan Type       : {scan_type}\n")
        f.write(f"Port Range      : {start_port}-{end_port}\n")
        f.write(f"Scan Time       : {datetime.now()}\n")
        f.write("Open Ports      :\n")
        for port in open_ports:
            try:
                service = socket.getservbyport(port, scan_type.lower())
            except:
                service = "unknown"
            f.write(f"  - Port {port} ({service})\n")
    print(f"\n[+] Report saved as {filename}")

def main():
    try:
        print("===== Python Port Scanner =====\n")
        

        ip = input("Enter target IP address: ").strip()
        if not validate_ip(ip):
            print("Invalid IP address.")
            return

        range_choice = input("Scan (1) Custom port range or (2) All ports? [1/2]: ").strip()
        if range_choice == '1':
            try:
                start_port = int(input("Enter start port: ").strip())
                end_port = int(input("Enter end port: ").strip())
                if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535):
                    print("Port numbers must be in range 0–65535.")
                    return
                if start_port > end_port:
                    print("Start port must be less than or equal to end port.")
                    return
            except ValueError:
                print("Invalid port input.")
                return
        elif range_choice == '2':
            start_port = 0
            end_port = 65535
        else:
            print("Invalid option. Choose 1 or 2.")
            return

        scan_type = input("Scan type? (TCP/UDP): ").strip().upper()
        if scan_type == "TCP":
            open_ports = tcp_scan(ip, start_port, end_port)
        elif scan_type == "UDP":
            open_ports = udp_scan(ip, start_port, end_port)
        else:
            print("Invalid scan type. Choose TCP or UDP.")
            return

        if open_ports:
            print("\n[+] Open Ports:")
            for port in open_ports:
                try:
                    service = socket.getservbyport(port, scan_type.lower())
                except:
                    service = "unknown"
                print(f"  - Port {port} ({service}) is open")
        else:
            print("\n[-] No open ports found.")

        generate = input("\nGenerate report? (y/n): ").strip().lower()
        if generate == 'y':
            generate_report(ip, scan_type, open_ports, start_port, end_port)

    except KeyboardInterrupt:
        print("\n[!] Scan cancelled by user.")
        sys.exit()

if __name__ == "__main__":
    main()
