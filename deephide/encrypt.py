import base64
import hashlib

from cryptography.fernet import Fernet


PASSWORD_ENCODING = 'utf-8'
ITERATIONS_COUNT = 1 << 13


def generate_key(password: str, salt: bytes = b'') -> bytes:
    key = hashlib.pbkdf2_hmac(
        'sha256', password.encode(PASSWORD_ENCODING),
        salt, ITERATIONS_COUNT, 32)
    return base64.urlsafe_b64encode(key)


def encrypt(data: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(data)


def decrypt(data: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(data)
