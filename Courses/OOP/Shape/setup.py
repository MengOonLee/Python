from setuptools import setup, find_packages

setup(
    name = 'shape',
    version = '0.0.1',
    package_dir = {'': 'src'},
    packages = find_packages(where='src')
)