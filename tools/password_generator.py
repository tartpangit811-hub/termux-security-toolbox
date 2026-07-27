import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print("=" * 30)
print(" PASSWORD GENERATOR ")
print("=" * 30)

print("\n1. Weak Password")
print("2. Medium Password")
print("3. Strong Password")

choice = input("\nSelect option: ")

if choice == "1":
    password = generate_password(8)
    print("\nWeak Password:")
    print(password)

elif choice == "2":
    password = generate_password(12)
    print("\nMedium Password:")
    print(password)

elif choice == "3":
    password = generate_password(16)
    print("\nStrong Password:")
    print(password)

else:
    print("\nInvalid option.")
