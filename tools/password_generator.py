import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("=" * 30)
print(" PASSWORD GENERATOR ")
print("=" * 30)

length = int(input("Enter password length: "))

password = generate_password(length)

print("\nGenerated Password:")
print(password)
