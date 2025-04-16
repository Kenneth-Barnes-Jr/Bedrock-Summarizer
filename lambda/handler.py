# This is the entry point for the Lambda function

import json
from utils.s3_helper import get_s3_object_text, get_csv_text_from_s3, save_summary_to_s3
from utils.bedrock_client import summarize_text
from utils.textract import extract_text_from_textract

def lambda_handler(event, context):
    # Parse S3 event info
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f"Processing file: s3://{bucket}/{key}")

    #Decide how to process the document based on its extension.
    if key.lower().endswith(('png', 'jpg', 'jpeg', 'pdf')):
        document_text = extract_text_from_textract(bucket, key)
    elif key.lower().endswith('.csv'):
        document_text = get_csv_text_from_s3(bucket, key)
    else:
        document_text = get_s3_object_text(bucket, key)
    
    # Get summary from Bedrock
    summary = summarize_text(document_text)
    
    # Save summary back to S3
    summary_key = key.replace("uploads/", "summaries/").rsplit('.', 1)[0] + "_summary.txt"
    save_summary_to_s3(bucket, summary_key, summary)
    
    return {
        "statusCode": 200,
        "body": json.dumps("Summary created and uploaded to S3.")
    }