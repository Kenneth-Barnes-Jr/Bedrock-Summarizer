# This is the entry point for the Lambda function

import json
from utils.s3_helper import get_s3_object_text, save_summary_to_s3
from utils.bedrock_client import summarize_text

def lambda_handler(event, context):
    # Parse S3 event info
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f"Processing file: s3://{bucket}/{key}")
    
    # Get document text from S3
    document_text = get_s3_object_text(bucket, key)
    
    # Get summary from Bedrock
    summary = summarize_text(document_text)
    
    # Save summary back to S3
    summary_key = key.replace("uploads/", "summaries/").replace(".txt", "_summary.txt")
    save_summary_to_s3(bucket, summary_key, summary)
    
    return {
        "statusCode": 200,
        "body": json.dumps("Summary created and uploaded to S3.")
    }