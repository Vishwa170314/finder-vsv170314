from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Helps reduce code'

# Setting up
setup(
    name="finder-vsv170314",
    version=VERSION,
    author="VSV170314 (Vishwa S Vikram)",
    install_requires=[],
)
