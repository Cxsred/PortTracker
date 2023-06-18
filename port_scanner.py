import socket

def port_scan(target_host, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((target_host, target_port))
        if result == 0:
            print(f"Port {target_port} is open")
        sock.close()
    except socket.error:
        print("An error occurred.")

def main():
    target_host = input("Enter the target host IP: ")
    target_ports = [80, 443, 22, 21, 3389]  # Add more ports to scan

    for port in target_ports:
        port_scan(target_host, port)

if __name__ == '__main__':
    main()
