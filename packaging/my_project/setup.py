# Import setup function from setuptools module
from setuptools import setup
# Create module level dunders
__project__ = "motivate"
__version__ = "0.0.1"
__description__ = "a Python module to motivate you"
__packages__ = ["motivate"]
__author__ = "Mickey Mouse"
__author_email__ = "mickey@disney.com"
__classifiers__ = ["Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3"]
__keywords__ = ["motivation", "learning"]
__requires__ = ["twine"]
# Pass the variables
setup(name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    author = __author__,
    author_email = __author_email__,
    classifiers = __classifiers__,
    keywords = __keywords__)