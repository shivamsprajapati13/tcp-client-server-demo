from cryptography.fernet import Fernet


SHARED_KEY = "mKusklbD-L1WWvDpZh5dO5aUwAxnTf5SzDhJQa1_X_4="
fernet = Fernet(SHARED_KEY)

def encrypt_message(message: str) -> bytes:
    return fernet.encrypt(message.encode())

def decrypt_message(token: bytes) -> str:
    return fernet.decrypt(token).decode()
