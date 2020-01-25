#!/usr/bin/env bash
echo "mypy"
mypy --config-file=mypy.ini spamwatch

echo -e "\nflake8"
flake8 --config=.flake8 spamwatch

echo -e "\npylint"
pylint --rcfile=.pylintrc spamwatch
