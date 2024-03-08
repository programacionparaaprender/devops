#!/usr/bin/python
# -*- coding: utf-8 -*-
# program python connect with upload s3

import os
import boto3

# client instance
client = boto3.client('s3')

# variable
bucket = 's3-osk-bucket-3000'

# list all objs in bucket
all_objects = client.list_objects(Bucket=bucket)

# print the contents
print(f"List of obj in {bucket}: ")
for a in all_objects['Contents']:
    print(a['Key'])

# func for deleting files
def del_file(filename):
    client.delete_object(
        Bucket=bucket,
        Key=filename
    )

# cli message
print('\nList of files to be deleted:')
for a in all_objects['Contents']:
    if 'example/' in a['Key'] and a['Key'] != 'example/':
        print(f"file to be deleted {a['Key']}")
        del_file(a['Key'])
print("Deletion Processed")

# refresh object metadata
all_objects = client.list_objects(Bucket=bucket)

# print the contents
print(f"List of obj in {bucket}: ")
for a in all_objects['Contents']:
    print(a['Key'])