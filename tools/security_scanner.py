import platform
import getpass

print("=" * 30)
print(" SECURITY SCANNER ")
print("=" * 30)

print(f"\nSystem: {platform.system()}")
print(f"Release: {platform.release()}")
print(f"User: {getpass.getuser()}")

print("\nSecurity Checks:")
print("[✓] Python Installed")
print("[✓] User Account Detected")
print("[✓] System Information Retrieved")

print("\nSecurity Status: Basic Check Complete")
