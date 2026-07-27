import socket

print("=" * 30)
print(" NETWORK TOOLS ")
print("=" * 30)

hostname = socket.gethostname()

try:
    ip_address = socket.gethostbyname(hostname)

    print(f"\nHostname   : {hostname}")
    print(f"IP Address : {ip_address}")
    print("\nNetwork Status: Connected")

except:
    print("\nNetwork Status: Unable to retrieve network information")
