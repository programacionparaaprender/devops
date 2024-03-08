#!/usr/bin/python
# -*- coding: utf-8 -*-
# program python connect with upload s3

import os
import boto3

# client instance
client = boto3.client('s3')

# path and other vars
bucket = 's3-osk-bucket-3000'
cur_path = os.getcwd()
file = 'profile_007.csv'
filename = os.path.join(cur_path, 'downloads', file)

# object method to download file
client.download_file(
    Bucket=bucket,
    Key=file,
    Filename=filename
)

# list the contents of DL dir
downloads_dir = os.path.join(cur_path, 'downloads')
for root, dirs, files in os.walk(downloads_dir):
    for fnames in files:
        print (fnames)