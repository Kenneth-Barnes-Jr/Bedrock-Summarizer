import boto3
import json

bedrock = boto3.client("bedrock-runtime")

def summarize_text(text):
    prompt = f"Simplify and summarize the following document:\n\n{text}"

    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 500,
        "temperature": 0.5,
        "stop_sequences": ["\n\n"]
    })

    response = bedrock.invoke_model(
        modelId="anthropic.claude-3-7-sonnet-20250219-v1:0",  # This is the model of your choice.
        contentType="application/json",
        accept="application/json",
        body=body
    )

    result = json.loads(response['body'].read())
    return result.get("completion", "[No summary returned]")