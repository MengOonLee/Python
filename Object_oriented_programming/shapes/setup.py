from setuptools import setup, find_packages

setup(
    name = "shapes",
    version = "0.0.1",
    author = "MengOonLee",
    author_email = "darklemon2000@gmail.com",
    description = "A drawing package",
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
)
