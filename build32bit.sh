#!/bin/bash

if [[ -z "${TEST_32BIT}" ]]; then
    echo "Not on CI"
    exit 0
fi

docker run -v ${PWD}:/code -e INSTALL_REQUIREMENTS=${INSTALL_REQUIREMENTS} i386/ubuntu bash -c "
    apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq python3.8 locales python3-pip python3-pillow debianutils \
    && python3.8 -m pip install tox coveralls \
    && locale-gen en_US.UTF-8 \
    && export LANG='en_US.UTF-8' \
    && cd /code \
    && python3.8 -m tox -e py \
    && coverage report"
