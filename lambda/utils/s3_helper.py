# This module provides helper functions to interact with AWS S3.

import boto3
import csv
import io

s3 = boto3.client("s3")

def get_s3_object_text(bucket, key):
    """
    Reads a plain text (.txt) file from S3 and returns its contents as a string.
    """
    obj = s3.get_object(Bucket=bucket, Key=key)
    text = obj["Body"].read().decode("utf-8")
    return text

def get_csv_text_from_s3(bucket, key):
    """
    Reads a CSV file from S3, converts it into plain text for summarization.
    Returns a string with each row as a comma-separated line.
    """
    obj = s3.get_object(Bucket=bucket, Key=key)
    csv_file = obj['Body'].read().decode('utf-8')   # Decode the byte stream to string
    reader = csv.reader(io.StringIO(csv_file))      # Use StringIO to simulate a file object

    lines = []
    for row in reader:
        # Convert each row list into a string and add to lines
        lines.append(', '.join(row))

    # Join all rows with line breaks
    return '\n'.join(lines)

def save_summary_to_s3(bucket, key, summary):
    """
    Saves the generated summary back to S3 under the specified key.
    """
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=summary.encode("utf-8")  # Ensure content is in byte format
    )
    