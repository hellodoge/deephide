import os
from zlib import crc32

from deephide.preferences import *


def set_secret(file: str, secret: bytes):

    def int_to_bytes(x: int, n: int = DEFAULT_INT_SIZE,
                     byteorder: str = BYTEORDER) -> bytes:
        if x.bit_length() > n * 8:
            raise ValueError('Integer is too big')
        return x.to_bytes(n, byteorder)

    def append_bytes(x: bytes):
        with open(file, 'ab') as fp:
            fp.write(x)

    append_bytes(secret)
    append_bytes(int_to_bytes(crc32(secret)))
    append_bytes(int_to_bytes(len(secret)))


def get_secret(file: str) -> bytes:

    def bytes_to_int(x: bytes, byteorder: str = BYTEORDER) -> int:
        return int.from_bytes(x, byteorder)

    def get_last_n_bytes(n: int = DEFAULT_INT_SIZE) -> bytes:
        with open(file, 'rb') as fp:
            fp.seek(0, os.SEEK_END)
            if n > fp.tell():
                return b''
            fp.seek(-n, os.SEEK_END)
            return fp.read()

    secret_size = bytes_to_int(get_last_n_bytes())
    crc = bytes_to_int(get_last_n_bytes(
        DEFAULT_INT_SIZE * 2)[:-DEFAULT_INT_SIZE])
    secret = get_last_n_bytes(secret_size +
                              DEFAULT_INT_SIZE * 2)[:-DEFAULT_INT_SIZE * 2]
    return secret if secret and crc32(secret) == crc else None
