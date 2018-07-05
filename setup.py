#!/usr/bin/env python
from setuptools import setup

setup(
    name='propsd',
    version='0.1.2',
    description='propsd python client',
    author='Rapid7',
    author_email='R7_Labs@rapid7.com',
    url='https://www.rapid7.com/',
    packages=['propsd'],
    setup_requires=['pytest-runner'],
    install_requires=[
      'APScheduler',
      'requests',
      'objectpath'
    ],
    tests_require=[
        'mock',
        'pytest'
    ]
)
