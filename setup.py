#!/usr/bin/env python
# coding=utf-8

import os
import io
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.rst'), encoding="utf8").read()
NEWS = io.open(os.path.join(here, 'CHANGELOG.rst'), encoding="utf8").read()


version = '0.5.0'

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
zip_safe = not on_rtd

setup(
    name='fake-factory',
    version=version,
    description="Faker is a Python package that generates fake data for you.",
    long_description=README + '\n\n' + NEWS,
    scripts=['faker/bin/faker'],
    classifiers=[
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
    ],
    keywords='faker fixtures data test mock generator',
    author='joke2k',
    author_email='joke2k@gmail.com',
    url='http://github.com/joke2k/faker',
    license='MIT License',
    packages=find_packages(exclude=['*.tests']),
    platforms=["any"],
    test_suite='faker.tests',
    zip_safe=zip_safe,
)
