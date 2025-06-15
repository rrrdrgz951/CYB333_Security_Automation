import socket
import time

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"Port {port}: OPEN")
                else:
                    print(f"Port {port}: CLOSED")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
        time.sleep(0.1)  # Respectful delay

if __name__ == "__main__":
    try:
        target = input("Enter host (127.0.0.1 or scanme.nmap.org): ")
        start = int(input("Enter start port: "))
        end = int(input("Enter end port: "))
        if start < 1 or end > 65535 or start > end:
            raise ValueError("Invalid port range.")
        scan_ports(target, start, end)
    except Exception as e:
        print(f"Input error: {e}")
