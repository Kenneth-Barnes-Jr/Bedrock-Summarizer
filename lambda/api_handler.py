import json
from utils.s3_helper import get_s3_object_text, get_csv_text_from_s3
from utils.bedrock_client import summarize_text
from utils.textract import extract_text_from_textract
from utils.comprehend_agent import analyze_summarize_documentation
from utils.dynamodb_helper import summarize_metadata

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    bucket = body.get("bucket")
    key = body.get("key")

    if not bucket or not key:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing bucket or key"})
        }

    # Process the document
    if key.lower().endswith(('png', 'jpg', 'jpeg', 'pdf')):
        document_text = extract_text_from_textract(bucket, key)
    elif key.lower().endswith('.csv'):
        document_text = get_csv_text_from_s3(bucket, key)
    else:
        document_text = get_s3_object_text(bucket, key)

    # Summarize with Bedrock
    summary = summarize_text(document_text)

    # Analyze summary with Comprehend
    analysis = analyze_summarize_documentation(summary)

    # Save to S3
    summary_key = key.replace("uploads/", "summaries/").rsplit('.', 1)[0] + "_summary.txt"
    s3_summary_url = f"s3://{bucket}/{summary_key}"
    
    from utils.s3_helper import save_summary_to_s3
    save_summary_to_s3(bucket, summary_key, summary)

    # Save to DynamoDB
    summarize_metadata(
        original_filename=key,
        summary=summary,
        key_points=analysis.get("key_points", []),
        s3_summary_url=s3_summary_url
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "summary": summary,
            "key_points": analysis.get("key_points", []),
            "s3_summary_url": s3_summary_url
        })
    }
