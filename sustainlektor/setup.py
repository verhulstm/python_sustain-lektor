import sys
from setuptools import setup

from sustainlektor.settings import *

assert sys.version_info >= MINIMUM_PYTHON_VERSION

setup(
    name="sustain-lektor",
    version=VERSION,
    description="sustain lektor",
    url="https://github.com/verhulstm/sustain-lektor",
    author="Terminal Labs",
    author_email="michael@terminallabs.com",
    license="see LICENSE file",
    packages=["sustainlektor"],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "setuptools",
        "Lektor",
        "click",
        "black",
        "flake8",
    ],
    entry_points="""
        [console_scripts]
        sustainlektor=sustainlektor.__main__:main
    """,
)
