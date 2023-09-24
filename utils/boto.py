from models import File
import boto3
from decouple import config
from flask import request


s3 = boto3.client('s3', aws_access_key_id=config('AWS_ACCESS_KEY'),
                        aws_secret_access_key=config('AWP_SECRET_KEY'))

response = s3.list_buckets()

def get_bucket():
    for bucket in response['Buckets']:
        print(bucket['Name'])
    return bucket['Name']