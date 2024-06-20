# password_vault.py
import hashlib
import os
from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet instance
def generate_key():
    return Fernet.generate_key()

def load_key():
    return os.environ.get('VAULT_KEY').encode()

def save_password(site_name, password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())

    with open("vault.txt", "a") as vault:
        vault.write(f"{site_name}:{encrypted_password.decode()}\n")

def get_password(site_name, key):
    f = Fernet(key)
    with open("vault.txt", "r") as vault:
        for line in vault:
            stored_site_name, encrypted_password = line.strip().split(":")
            if stored_site_name == site_name:
                return f.decrypt(encrypted_password.encode()).decode()
    return None

# Example usage
if __name__ == "__main__":
    key = load_key()
    save_password("example.com", "password123", key)
    print(get_password("example.com", key))
