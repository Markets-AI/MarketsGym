#!/usr/bin/env python
from setuptools import setup, find_packages

TEST_GLOB_PATTERNS = ['*.tests', '*.tests.*', 'tests.*', 'tests']

setup(
    name='marketsgym',
    version='0.1',
    description='Gym Environments for Trading',
    author='Mahmoud Mahfouz, Rohan Tangri',
    url='https://github.com/Markets-AI/MarketsGym',
    packages=find_packages(exclude=TEST_GLOB_PATTERNS),
)
