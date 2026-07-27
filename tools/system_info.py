import platform
import socket

print("=" * 30)
print(" SYSTEM INFORMATION ")
print("=" * 30)

print(f"\nOperating System : {platform.system()}")
print(f"Release          : {platform.release()}")
print(f"Version          : {platform.version()}")
print(f"Machine          : {platform.machine()}")
print(f"Processor        : {platform.processor()}")
print(f"Hostname         : {socket.gethostname()}")
print(f"Python Version   : {platform.python_version()}")
