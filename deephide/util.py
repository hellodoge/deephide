from glob import glob
from os import path, walk


def get_files(x: list) -> list:
    output = list()
    for i in x:
        if path.isfile(i):
            output.append(i)
        elif path.isdir(i):
            for root, dirs, files in walk(i):
                for name in files:
                    output.append(path.join(root, name))
        else:
            output.extend([i for i in glob(i, recursive=True) if path.isfile(i)])
    return output
