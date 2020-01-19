#!/bin/bash

if [[ -z "${TEST_32BIT}" ]]; then
    echo "Not on Travis"
    exit 0
fi

docker run -v ${PWD}:/code -e INSTALL_REQUIREMENTS=${INSTALL_REQUIREMENTS} i386/ubuntu bash -c "
    apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq python3 locales python3-pip debianutils \
    && pip3 install tox coveralls \
    && locale-gen en_US.UTF-8 \
    && export LANG='en_US.UTF-8' \
    && cd /code \
    && tox -e py \
    && coverage report"
