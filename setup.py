#!/usr/bin/env python
# coding=utf-8

import os
import io
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.rst'), encoding="utf8").read()
NEWS = io.open(os.path.join(here, 'CHANGELOG.rst'), encoding="utf8").read()


version = '0.5.1'

install_requires = []
if ((sys.version_info[0] == 2 and sys.version_info[1] < 7) or
        (sys.version_info[0] == 3 and sys.version_info[1] < 1)):
    install_requires.append('importlib')

# this module can be zip-safe if the zipimporter implements iter_modules or if
# pkgutil.iter_importer_modules has registered a dispatch for the zipimporter.
try:
    import pkgutil
    import zipimport
    zip_safe = hasattr(zipimport.zipimporter, "iter_modules") or \
        zipimport.zipimporter in pkgutil.iter_importer_modules.registry.keys()
except (ImportError, AttributeError):
    zip_safe = False

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
    install_requires=install_requires
)
