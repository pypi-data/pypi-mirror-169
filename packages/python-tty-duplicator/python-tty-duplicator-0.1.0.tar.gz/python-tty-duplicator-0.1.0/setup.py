#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from setuptools import setup

setup(
    name='python-tty-duplicator',
    version='0.1.0',
    author='Salamandar',
    author_email='felix@piedallu.me',
    maintainer='Salamandar',
    maintainer_email='felix@piedallu.me',
    license='MIT',
    url='https://github.com/Salamandar/python-tty-duplicator',
    description='Utility to duplicate a tty for logging purposes',
    long_description=(Path(__file__).parent /'README.rst').read_text(),
    long_description_content_type='text/x-rst',
    py_modules=['tty_duplicator'],
    python_requires='>=3.6',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
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
)
