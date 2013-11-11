#!/usr/bin/env python

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.3.2'

setup(name='fake-factory',
      version=version,
      description="Faker is a Python package that generates fake data for you.",
      long_description=README + '\n\n' + NEWS,
      classifiers=[
          # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
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
      )
