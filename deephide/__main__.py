import zlib

import deephide.encrypt
import deephide.packager
import deephide.processor
import deephide.parser
import deephide.util

from deephide.preferences import *


def main():
    args = deephide.parser.parser.parse_args()

    box_files = deephide.util.get_files(args.box)
    key = deephide.encrypt.generate_key(args.password) if args.password is not None else None

    if args.action == 'hide':
        if args.input is None:
            raise ValueError('-i/--input argument required')
        input_files = deephide.util.get_files(args.input)
        hide(input_files, box_files, key=key, compression_level=args.compress)
    elif args.action == 'reveal':
        output_dir = args.output if args.output is not None else DEFAULT_OUTPUT_NAME
        reveal(box_files, output_dir, key=key)


def hide(input_files, box, *, key=None, compression_level=0):
    data = deephide.packager.pack_files(input_files)
    if compression_level != 0:
        data = zlib.compress(data, compression_level)
    if key is not None:
        data = deephide.encrypt.encrypt(data, key)
    deephide.processor.write_secret(box, data)


def reveal(box, output_dir, *, key=None):
    data = deephide.processor.read_secret(box)
    if key is not None:
        data = deephide.encrypt.decrypt(data, key)
    try:
        data = zlib.decompress(data)
    except zlib.error:
        pass  # the data seems to be uncompressed
    deephide.packager.unpack_files(data, output_dir)


if __name__ == '__main__':
    main()
