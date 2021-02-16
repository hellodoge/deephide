from deephide.secret import set_secret, get_secret
from io import BytesIO


def write_secret(files: list, secret: bytes):

    def get_sizes(s: int, n: int):
        # returns list of n numbers of the sum s
        o = [s // n] * n
        h = n // 2
        r = s % n
        return [j + h - i + (r > i) for i, j in enumerate(o)] \
            if n % 2 else [j + h - i - (i >= h) + (r + h > i >= h) +
                           (r > i + h and i < h) for i, j in enumerate(o)]

    sizes = get_sizes(len(secret), len(files))
    for size, file in zip(sizes, files):
        local_secret = secret[:size]
        set_secret(file, local_secret)
        secret = secret[size:]


def read_secret(files: list) -> bytes:
    secrets = dict()
    for file in files:
        secret = get_secret(file)
        if not secret:
            continue
        if len(secret) not in secrets:
            secrets.setdefault(len(secret), secret)
    output = BytesIO()
    for secret in sorted(secrets.keys(), reverse=True):
        output.write(secrets.get(secret))
    output.seek(0)
    return output.read()
