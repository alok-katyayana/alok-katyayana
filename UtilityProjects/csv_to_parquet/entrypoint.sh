#!/bin/bash

set -e

echo "Running Tests...."

pytest -v

echo "Tests passed, starting application..."

exec python ./main.py
#     --packages org.apache.hadoop:hadoop-aws:3.3.1, org.apache.hadoop.fs.s3a.S3AFileSystem, com.amazonaws.auth.DefaultAWSCredentialsProviderChain
