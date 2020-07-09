import setuptools

setuptools.setup(
    name="dockerlint",
    version="0.3.0",
    packages=setuptools.find_packages(),
    description="A linter for Docker images.",
    url="https://github.com/RDIL/dockerlint",
    author="Reece Dunham",
    author_email="me@rdil.rocks",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "click",
        "colorama",
        "junit-xml",
    ],
    entry_points="""
        [console_scripts]
        dockerlint=dockerlint:main
    """,
)
