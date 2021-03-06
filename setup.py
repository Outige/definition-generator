import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
REQUIREMENTS = (HERE / "requirements.txt").read_text()

# This call to setup() does all the work
setup(
    name="defgen",
    version="0.0.0",
    description="Tool to create stylish definitions from structured input",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Outige/definition-generator",
    author="Tieg O'Sullivan",
    author_email="tiegosullivanpsnl@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8.5",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[REQUIREMENTS], # this might be wrong
    # entry_points={
    #     "console_scripts": [
    #         "realpython=reader.__main__:main",
    #     ]
    # },
)