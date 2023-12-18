from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("secret.key", "rb").read()


def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message


generate_key()
key = load_key()
message = "Hello, World!"
encrypted = encrypt_message(message, key)
print("Encrypted message:", encrypted)
decrypted = decrypt_message(encrypted, key)
print("Decrypted message:", decrypted)

