#!/usr/bin/python
# -*- coding: utf-8 -*-
# program python connect with upload s3

import os
import boto3

# client instance
client = boto3.client('s3')

# vars
bucket = 's3-osk-empty-bucket'

# retrieve the bucket list
response = client.list_buckets()

for n in response['Buckets']:
    print(n['Name'])

client.delete_bucket(
    Bucket=bucket
)

# retrieve the bucket list
response = client.list_buckets()

for n in response['Buckets']:
    print(n['Name'])