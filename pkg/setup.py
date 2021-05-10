# Import function from setuptools module
from setuptools import setup, find_packages

setup(
    name = "pkg",
    version = "0.0.1",
    author = "MengOonLee",
    author_email = "darklemon2000@gmail.com",
    description = "Learn Python packaging",
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
)
