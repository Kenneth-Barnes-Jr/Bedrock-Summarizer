# This is the entry point for the Lambda function

import boto3

s3 = boto3.client("s3")

def get_s3_object_text(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    return response['Body'].read().decode('utf-8')

def save_summary_to_s3(bucket, key, summary_text):
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=summary_text.encode('utf-8'),
        ContentType='text/plain'
    )
    print(f"Saved summary to s3://{bucket}/{key}")