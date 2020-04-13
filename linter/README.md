# Linter

This package holds the code for the Dockerfile linter.

The way it is included is we build a wheel from it, install that wheel, and then PyInstaller builds said wheel into distributions.

This process is done by running `make build-packages` in the root directory.
