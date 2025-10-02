#!/bin/bash

set -e

echo "Running Tests...."

pytest -v

echo "Tests passed, starting application..."

exec spark-submit ./main.py
