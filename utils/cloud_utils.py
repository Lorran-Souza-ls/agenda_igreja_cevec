import boto3
from config.cloud_config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, AWS_S3_BUCKET

def upload_file(file, object_name):
    s3_client = boto3.client('s3', 
                             aws_access_key_id=AWS_ACCESS_KEY,
                             aws_secret_access_key=AWS_SECRET_KEY,
                             region_name=AWS_REGION)
    s3_client.upload_fileobj(file, AWS_S3_BUCKET, object_name)
