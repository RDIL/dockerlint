# dockerlint

Lint a Dockerfile for potential issues related to image size and functionality.

## How to Use

1. Download the latest release (in `xz` tar format).
1. Decompress it.
1. Run the `dockerlint` executable file.
1. Start seeing results.

## Development Guide

> NOTE: this only works on Linux right now (and potentially macOS? - haven't tested)

You will need to have Python 3.6 or above installed on your system.

### Install Dependencies

To install the needed dependencies, run `make install-deps`.

### Build Executable

To build your changes into the executable, just run `make`.

### Run Cleanup

To clean up the unneeded files, you can run `make clean`.

## License

MIT - Copyright (c) 2020-present Reece Dunham. See the [LICENSE file](LICENSE) for more information.
