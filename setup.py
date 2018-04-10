from setuptools import setup

PACKAGE = "cmq"
NAME = "cmqPython"
DESCRIPTION = "cmq python sdk"
AUTHOR = "zhongzq"
VERSION = '0.1'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    license="BSD",
    packages=[PACKAGE],
    zip_safe=False,
)
