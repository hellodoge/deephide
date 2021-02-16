import zipfile
from io import BytesIO


def pack_files(files: list) -> bytes:
    packed = BytesIO()
    with zipfile.ZipFile(packed, 'w') as archive:
        for file in files:
            archive.write(file)
    packed.seek(0)
    return packed.read()


def unpack_files(packed: bytes, folder: str):
    with zipfile.ZipFile(BytesIO(packed), 'r') as archive:
        archive.extractall(folder)
