import setuptools

setuptools.setup(
    name="dockerfile_linter_pkg",
    version="0.1.0",
    packages=setuptools.find_packages(),
    description="A Dockerfile linter.",
    url="https://github.com/RDIL/dockerlint",
    author="Reece Dunham",
    author_email="me@rdil.rocks",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
)
