#!/usr/bin/python
# -*- coding: utf-8 -*-
# program python connect with upload s3

import os
import boto3

# client instance
client = boto3.client('s3')


# variables
target_bucket = 's3-osk-bucket-3000'
subfolder_01 = 'example/'
subfolder_02 = 'test_folder/'

# create subfolder (objects)
client.put_object(Bucker=target_bucket, Key=subfolder_01)
client.put_object(Bucker=target_bucket, Key=subfolder_02)

# retrieve object info from bucket
all_objects = client.list_objects(Bucket=target_bucket)

# iterate through Metadata and list objects
for a in all_objects['Contents']:
    print(a['Key'], a['LastModified'])
