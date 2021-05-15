#!/usr/bin/env python3

import boto3

MY_FILE = "bucketTest.txt"
MY_BUCKET = "tisipi-com"

print("Upload a file to your S3 bucket")

with open(MY_FILE, "rb") as file_data:
    s3 = boto3.resource("s3")
    try:
        s3.Bucket(MY_BUCKET).put_object(Key=MY_FILE, Body=file_data)
    except:
        print("Error. Bucket does not exist")
