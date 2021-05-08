from setuptools import setup

__project__ = "my_drawing"
__version__ = "0.0.1"
__description__ = "A drawing package"
__packages__ = ["shapes"]
__author__ = "MengOonLee"
__author_email__ = "darklemon2000@gmail.com"
__requires__ = ["tkinter", "random"]

setup(
    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    author = __author__,
    author_email = __author_email__,
    requires = __requires__
)
