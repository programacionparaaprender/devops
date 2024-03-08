#!/usr/bin/python
# -*- coding: utf-8 -*-
# program python connect with s3

import boto3

# instance a client
client = boto3.client('s3')

# retrieve all bucker Metadata
response = client.list_buckets()

# loop trough bucket data and display bucket names
for b in response['Buckets']:
    print(b['Name'])
