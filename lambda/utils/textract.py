import boto3

textract = boto3.client('textract')

def extract_text_from_textract(bucket, key):
    response = textract.detect_document_text(
        Document={'S3Object': {'Bucket': bucket, 'Name': key}}
    )
    
    text_blocks = [item['Text'] for item in response['Blocks'] if item['BlockType'] == 'LINE']
    full_text = "\n".join(text_blocks)
    
    return full_text
