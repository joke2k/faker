#!/usr/bin/env python
# coding=utf-8

import os
import io

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.rst'), encoding="utf8").read()


version = '0.7.9'

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
    name='Faker',
    version=version,
    description="Faker is a Python package that generates fake data for you.",
    long_description=README,
    entry_points={
        'console_scripts': ['faker=faker.cli:execute_from_command_line'],
    },
    classifiers=[
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
    ],
    keywords='faker fixtures data test mock generator',
    author='joke2k',
    author_email='joke2k@gmail.com',
    url='https://github.com/joke2k/faker',
    license='MIT License',
    packages=find_packages(exclude=["docs", "tests", "tests.*"]),
    platforms=["any"],
    test_suite='tests',
    zip_safe=zip_safe,
    install_requires=[
        "python-dateutil>=2.4",
        "six",
    ],
    extras_require={
        ':python_version=="2.7"': [
            'ipaddress',
        ],
        ':python_version=="3.0"': [
            'importlib',
        ],
        ':python_version=="3.2"': [
            'ipaddress',
        ],
    }
)
