#!/bin/bash

docker run -v ${PWD}:/code -e INSTALL_REQUIREMENTS=${INSTALL_REQUIREMENTS} i386/ubuntu bash -c "
    apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq python3 locales python3-pip debianutils \
    && pip3 install tox coveralls \
    && locale-gen en_US.UTF-8 \
    && cd /code \
    && coverage run --source=faker setup.py test \
    && coverage report"
