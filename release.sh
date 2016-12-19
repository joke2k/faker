#!/bin/bash

rm -rf dist
python setup.py sdist bdist_wheel
twine upload dist/*