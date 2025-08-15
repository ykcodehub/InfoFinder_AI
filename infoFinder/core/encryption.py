import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class EncryptionManager:
    def __init__(self, password: str):
        self.password = password.encode()
        self.backend = default_backend()

    def _derive_key(self, salt: bytes) -> bytes:
        """Derive AES key from password using PBKDF2"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # AES-256
            salt=salt,
            iterations=100_000,
            backend=self.backend
        )
        return kdf.derive(self.password)

    def encrypt(self, plaintext: str) -> str:
        """Encrypt text and return base64(salt + iv + ciphertext)"""
        salt = os.urandom(16)
        key = self._derive_key(salt)
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
        return base64.urlsafe_b64encode(salt + iv + ciphertext).decode()

    def decrypt(self, encrypted_text: str) -> str:
        """Decrypt base64(salt + iv + ciphertext)"""
        raw = base64.urlsafe_b64decode(encrypted_text.encode())
        salt, iv, ciphertext = raw[:16], raw[16:32], raw[32:]
        key = self._derive_key(salt)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        return (decryptor.update(ciphertext) + decryptor.finalize()).decode()

# Temporary test code
if __name__ == "__main__":
    manager = EncryptionManager(password="TestPass123")
    secret = "MySensitiveData"

    enc = manager.encrypt(secret)
    print("Encrypted:", enc)

    dec = manager.decrypt(enc)
    print("Decrypted:", dec)
