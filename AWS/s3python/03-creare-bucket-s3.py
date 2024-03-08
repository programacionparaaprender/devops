#!/usr/bin/python
# -*- coding: utf-8 -*-
# program python connect with upload s3

import os
import boto3

# instance a client
client = boto3.client('s3')

# set the new bucket name
bucker = 's3-osk-bucket-5000'

# create new bucket
client.create_bucket(
    Bucket=bucker
)

response = client.list_buckets()

# loop trough bucket data and display bucket names
for b in response['Buckets']:
    print(b['Name'])
