# merge-kicad-sym

A script to merge KiCad symbol libraries.

## Installation

```sh
pip install combine_libs
```

## Usage

```sh
usage: merge-kicad-sym [-h] [--overwrite-footprint-lib-name OVERWRITE_FOOTPRINT_LIB_NAME] target_lib source_lib

Combine two KiCad symbol libraries.

positional arguments:
  target_lib            Path to the target KiCad symbol library file that the source library will be merged into.
  source_lib            Path to the source KiCad symbol library file that will be merged into the target library.

options:
  -h, --help            show this help message and exit
  --overwrite-footprint-lib-name OVERWRITE_FOOTPRINT_LIB_NAME
                        String to overwrite the footprint library this symbol refereces to.

```