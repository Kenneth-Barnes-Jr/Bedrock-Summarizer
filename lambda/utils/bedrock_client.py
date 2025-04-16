import boto3
import json

bedrock = boto3.client("bedrock-runtime")

def summarize_text(text):
    prompt = f"\n\nHuman: Simplify and summarize the following document:\n\n{text}\n\nAssistant:"

    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 800,
        "temperature": 0.5,
    })

    try:
        response = bedrock.invoke_model(
            modelId="anthropic.claude-instant-v1", # This is the AI/LM model of your choice.
            contentType="application/json",
            accept="application/json",
            body=body,
        )

        result = json.loads(response['body'].read())
        return result.get("completion", "[No summary returned]")

    except Exception as e:
        print(f"Error calling Bedrock model: {e}")
        return "[Error occurred while generating summary]"