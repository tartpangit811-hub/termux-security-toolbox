import ipaddress

print("=" * 30)
print(" IP CALCULATOR ")
print("=" * 30)

ip = input("\nEnter IP Address (example: 192.168.1.10/24): ")

try:
    network = ipaddress.ip_interface(ip)

    print(f"\nIP Address : {network.ip}")
    print(f"Network    : {network.network.network_address}")
    print(f"Netmask    : {network.network.netmask}")
    print(f"Broadcast  : {network.network.broadcast_address}")

except ValueError:
    print("\nInvalid IP address format.")
