import setuptools

setuptools.setup(
    name="dockerlint_tools",
    version="0.2.1",
    packages=setuptools.find_packages(),
    description="The packages that power dockerlint.",
    url="https://github.com/RDIL/dockerlint",
    author="Reece Dunham",
    author_email="me@rdil.rocks",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
)
