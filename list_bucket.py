#!/usr/bin/env python3

import boto3

print('List all S3 buckets in your AWS account')
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(f'  {bucket.name}')

# # Upload a file to a bucket
# s3 = boto3.resource('s3')
# data = open('bucketTest.txt', 'rb')
# s3.Bucket('tisipi-com').put_object(Key='bucketTest.txt', Body=data)


# # Retrieve the list of existing buckets
# s3 = boto3.client('s3')
# response = s3.list_buckets()
# for bucket in response['Buckets']:
#     print(f'  {bucket["Name"]}')