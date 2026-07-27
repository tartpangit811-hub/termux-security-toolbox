import platform
import getpass
import socket

print("=" * 30)
print(" SECURITY SCANNER ")
print("=" * 30)

print(f"\nSystem: {platform.system()}")
print(f"Release: {platform.release()}")
print(f"Machine: {platform.machine()}")
print(f"User: {getpass.getuser()}")
print(f"Hostname: {socket.gethostname()}")
print(f"Python Version: {platform.python_version()}")

print("\nSecurity Checks:")
print("[✓] Python Installed")
print("[✓] User Account Detected")
print("[✓] System Information Retrieved")
print("[✓] Hostname Retrieved")

print("\nSecurity Status: Basic Check Complete")
