from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

if __name__ == "__main__":
    generate_key()
    password = "my_secure_password"
    encrypted_password = encrypt_password(password)
    print(f"Encrypted: {encrypted_password}")
    decrypted_password = decrypt_password(encrypted_password)
    print(f"Decrypted: {decrypted_password}")
