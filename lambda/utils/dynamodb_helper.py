import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('<dynamodb-table>')

def summarize_metadata(original_filename, summary, key_points, s3_summary_url):
    document_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    item = {
        'document_id': document_id,
        'original_filename': original_filename,
        'summary': summary,
        'key_points': key_points,
        's3_summary_url': s3_summary_url,
        'timestamp': timestamp
    }

    table.put_item(Item=item)
    return document_id
