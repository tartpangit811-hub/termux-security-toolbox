import socket

print("=" * 30)
print(" NETWORK TOOLS ")
print("=" * 30)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"\nHostname: {hostname}")
print(f"IP Address: {ip_address}")
