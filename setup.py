#!/usr/bin/env python

import os

from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).resolve().parent
README = (here / 'README.rst').read_text(encoding='utf-8')
VERSION = (here / 'VERSION').read_text(encoding='utf-8').strip()

excluded_packages = ["docs", "tests", "tests.*"]
if not os.environ.get('READTHEDOCS', False):
    excluded_packages += ["faker.sphinx", "faker.sphinx.*"]


# this module can be zip-safe if the zipimporter implements iter_modules or if
# pkgutil.iter_importer_modules has registered a dispatch for the zipimporter.
try:
    import pkgutil
    import zipimport
    zip_safe = hasattr(zipimport.zipimporter, "iter_modules") or \
        zipimport.zipimporter in pkgutil.iter_importer_modules.registry.keys()
except AttributeError:
    zip_safe = False

setup(
    name='Faker',
    version=VERSION,
    description="Faker is a Python package that generates fake data for you.",
    long_description=README,
    entry_points={
        'console_scripts': ['faker=faker.cli:execute_from_command_line'],
        'pytest11': ['faker = faker.contrib.pytest.plugin'],
    },
    classifiers=[
        # See https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='faker fixtures data test mock generator',
    author='joke2k',
    author_email='joke2k@gmail.com',
    url='https://github.com/joke2k/faker',
    license='MIT License',
    packages=find_packages(exclude=excluded_packages),
    platforms=["any"],
    zip_safe=zip_safe,
    python_requires=">=3.6",
    install_requires=[
        "python-dateutil>=2.4",
        "text-unidecode==1.3",
    ],
)
