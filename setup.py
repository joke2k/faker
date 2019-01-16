#!/usr/bin/env python
# coding=utf-8

import os
import io

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as fp:
    README = fp.read()


version = '1.0.1'

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
        # See https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
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
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    setup_requires=["pytest-runner"],
    install_requires=[
        "python-dateutil>=2.4",
        "six>=1.10",
        "text-unidecode==1.2",
    ],
    tests_require=[
        "email_validator>=1.0.1,<1.1.0",
        "ukpostcodeparser>=1.1.1",
        "mock",
        "pytest>=3.8.0,<3.9",
    ],
    extras_require={
        ':python_version=="2.7"': [
            'ipaddress',
        ],
    }
)
