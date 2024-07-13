import argparse
import re


def symbol_exists(symbol, lines):
    pattern = re.compile(rf'symbol "{symbol}"')
    return any(re.search(pattern, line) for line in lines)


def combine_libs(source_lib, target_lib, overwrite_footprint_lib=None):
    with open(source_lib) as fi:
        with open(target_lib) as fo:
            fi_lines = fi.readlines()
            fo_lines = fo.readlines()

    if not fi_lines[0]:
        fi_lines.pop(0)

    source_symbols = re.findall(r'symbol "([^"]+)"', ''.join(fi_lines))

    for symbol in source_symbols:
        if symbol_exists(symbol, fo_lines):
            print(
                f'Symbol "{symbol}" already exists in target library. Quitting.')
            return

    if overwrite_footprint_lib:
        pattern = re.compile(r'"[^:"]*?:')
        fi_lines = [
            re.sub(pattern, f'"{overwrite_footprint_lib}:', line) for line in fi_lines]

    with open(target_lib, "w") as fo_w:
        fo_w.seek(0)
        lines = fo_lines[:-1] + fi_lines[1:]

        for line in lines:
            fo_w.write(line)

    print(f'Library "{source_lib}" merged into "{target_lib}".')


def main():
    parser = argparse.ArgumentParser(
        prog='merge-kicad-sym',
        description='Combine two KiCad symbol libraries.')
    parser.add_argument('target_lib', type=str,
                        help='Path to the target KiCad symbol library file that the source library will be merged into.')
    parser.add_argument('source_lib', type=str,
                        help='Path to the source KiCad symbol library file that will be merged into the target library.')
    parser.add_argument('--overwrite-footprint-lib-name', type=str,
                        help='String to overwrite the footprint library this symbol refereces to.')

    args = parser.parse_args()

    combine_libs(args.source_lib, args.target_lib,
                 args.overwrite_footprint_lib_name)


if __name__ == "__main__":
    main()
