"""
This module is used to install the GUM package.

GUM allows you to swicth between git users via command line


To install the package in editable mode, run the following command in the terminal:
    pip install -e .

Author: 
    - Enes Can Guven
"""

from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()


def __setup_package():
    setup(
        name="gum",
        version="0.1.0",
        description="Switch between git users via command line",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Enes Can Guven",
        url="https://github.com/enescanguven/gum",
        packages=find_packages(),
        entry_points={"console_scripts": ["gum = gum.gum:main"]},
    )


if __name__ == "__main__":
    __setup_package()
