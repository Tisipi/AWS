#!/usr/bin/env python3

import boto3

print("List all S3 buckets in your AWS account using resources:")
s3 = boto3.resource("s3")
for bucket in s3.buckets.all():
    print(bucket.name)

print("List all S3 buckets in your AWS account using client:")
s3_client = boto3.client("s3")
bucket_data = s3_client.list_buckets()
for bucket in bucket_data["Buckets"]:
    print(bucket["Name"])
