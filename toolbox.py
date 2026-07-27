import os

while True:
    print("=" * 35)
    print("    TERMUX SECURITY TOOLBOX")
    print("=" * 35)

    print("\n1. Password Generator")
print("2. Security Scanner")
print("3. System Information")
print("4. Network Diagnostics")
print("5. Storage Analyzer")
print("6. IP Calculator")
print("0. Exit")
    choice = input("\nSelect an option: ")

    if choice == "1":
        os.system("python tools/password_generator.py")
    elif choice == "2":
        os.system("python tools/security_scanner.py")
    elif choice == "3":
        os.system("python tools/system_info.py")
    elif choice == "4":
        os.system("python tools/network_tools.py")
    elif choice == "5":
    os.system("python tools/storage_checker.py")
elif choice == "6":
    os.system("python tools/ip_calculator.py")
elif choice == "0":
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid option.")
