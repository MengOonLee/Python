# Import function from setuptools module
from setuptools import setup, find_packages

setup(
    name = 'packaging',
    version = '0.0.1',
    package_dir = {'': 'packaging'},
    packages = find_packages(where='packaging'),
    install_requires=['numpy']
)
