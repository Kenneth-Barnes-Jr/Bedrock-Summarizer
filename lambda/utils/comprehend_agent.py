import boto3

comprehend = boto3.client("comprehend")

def analyze_summarize_documentation(summary):
    """
    Extracts document key phrases from the summary using Amazon Comprehend and returns a dictionary with key points.
    """
    if not summary or len(summary.strip()) == 0:
        return {"key_points": []}

    try:
        # Detect key phrases in the summary text
        response = comprehend.detect_key_phrases(
            Text=summary,
            LanguageCode="en"
        )

        # Extract and deduplicate key phrases
        key_phrases = [phrase['Text'] for phrase in response['KeyPhrases']]
        unique_phrases = list(set(key_phrases))[:5]  # Limit to top 5 for clarity

        return {
            "key_points": unique_phrases
        }

    except Exception as e:
        print(f"Error analyzing summary with Comprehend: {e}")
        return {
            "key_points": []
        }
