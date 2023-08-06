#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from setuptools import setup

setup(
    name='pytest-unstable',
    version='0.2.1',
    author='Salamandar',
    author_email='felix@piedallu.me',
    maintainer='Salamandar',
    maintainer_email='felix@piedallu.me',
    license='MIT',
    url='https://github.com/Salamandar/pytest-unstable',
    description='Set a test as unstable to return 0 even if it failed',
    long_description=(Path(__file__).parent /'README.rst').read_text(),
    long_description_content_type='text/x-rst',
    py_modules=['pytest_unstable'],
    python_requires='>=3.5',
    install_requires=['pytest>=3.5.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'unstable = pytest_unstable',
        ],
    },
)
