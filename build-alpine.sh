#!/bin/bash

if [[ -z "${TEST_ALPINE}" ]]; then
    echo "Not on Travis"
    exit 0
fi

docker run -v ${PWD}:/code -e INSTALL_REQUIREMENTS=${INSTALL_REQUIREMENTS} python:3-alpine sh -c "
    apk update \
    && apk add git build-base jpeg-dev zlib-dev \
    && pip install tox coveralls \
    && export LANG='en_US.UTF-8' \
    && cd /code \
    && tox -e py\
    && coverage report"
