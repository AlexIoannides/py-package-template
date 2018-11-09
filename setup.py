#!/usr/bin/env python3

import os

from setuptools import setup

# get package details from mds/__version__.py
about = {}  # type: ignore
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'py_pkg', '__version__.py')) as f:
    exec(f.read(), about)

print(about)

setup(
    name=about['__title__'],
    description=about['__description__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    install_requires=['numpy', 'requests'],
    packages=['py_pkg'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['py-package-template=py_pkg.entry_points:main'],
    },
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ]
)
