#!/usr/bin/env python3

import boto3


# MY_BUCKET = "www.tisipi.nl"
MY_BUCKET = "tisipi.nl"

print("Retrieve the website configuration of S3 bucket")
s3 = boto3.client("s3")
result = s3.get_bucket_website(Bucket="MY_BUCKET")
