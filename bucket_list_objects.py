#!/usr/bin/env python3

import boto3

MY_BUCKET = "tisipi-com"

s3 = boto3.resource("s3")
bucket = s3.Bucket(MY_BUCKET)
for obj in bucket.objects.all():
    print(obj.key)
