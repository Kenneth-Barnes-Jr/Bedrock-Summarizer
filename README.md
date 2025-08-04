# Serverless Pipeline for Intelligent Document Summarization on AWS.

## 🏗️**Techinal Architecture**
- ![AWS_Ai](<Serverless Pipeline for Intelligent Document Summarization.drawio.png>)

1. **Lambda Triggered**
    - This can come from either an S3 event or an API Gateway request.
    - Lambda receives the bucket and key.

2. **Determine File Type**
    - If it's a PDF or image, the function invokes Amazon Textract.
    - If it's a .txt or .csv, it reads directly from the S3 object.

3. **Text Extraction**
    - Textract performs OCR and returns the raw text.
    - For text files or CSVs, S3 file contents are read directly.

4. **Text Summarization with Bedrock**
    - Cleaned document text is sent to Amazon Bedrock using the Claude Instant model.
    - The summarizer returns a concise summary.

5. **Key Insight Extraction with Comprehend**
    - The summary is analyzed by Amazon Comprehend to pull out key phrases (max 5 in this case).

6. **Store Results**
    - The summary is saved to S3 in the summaries/ folder.
    - The metadata (filename, summary, key points, timestamp, S3 URL) is saved to DynamoDB.
    - CloudWatch logs every step, which helps with debugging and monitoring.

---

## 📜**Project Overview**
This project is a **serverless**, **AI-driven document processing pipeline** built on AWS. It automates the extraction, summarization, 
and analysis of various document formats (PDF, TXT, CSV, images) without requiring manual review. Users can trigger the pipeline by 
uploading files to an S3 bucket or sending a request via API Gateway.

At the core, the system uses **Amazon Textract** to extract text from scanned documents and images, **Amazon Bedrock** to generate 
summaries using a foundation model, and **Amazon Comprehend** to extract key insights from the generated summary. All output is then 
stored in **Amazon S3** for archival and **Amazon DynamoDB** for structured metadata storage. The logic is orchestrated through **AWS 
Lambda** functions written in Python (Boto3).

During development and deployment, tools such as **IAM** for permissions management, **CloudWatch** for monitoring, and **API Gateway 
(HTTP API)** for triggering the process via HTTP requests were also integrated. This setup ensures scalability, low operational 
overhead, and flexibility in how users can interact with the system.

---

## 🛠️**Technologies**
- **Amazon S3**            = Document uploads, summary output storage
- **Amazon Lambda**        = Serverless function to process documents and trigger summarization
- **Amazon Bedrock**       = Foundation model for text summarization
- **Amazon Textract**      = Optical character recognition (OCR) for extracting text from scanned PDFs or images
- **Amazon Comprehend**    = NLP for extracting key phrases, entities, and sentiment
- **Amazon DynamoDB**      = Metadata storage (filename, summary, timestamp, etc.)
- **Amazon API Gateway**   = Exposes HTTP endpoint to trigger Lambda manually
- **IAM Roles/Policies**   = Secure access between services
- **CloudWatch**           = Logging and debugging

---

## **Project Structure**
```bash
📁 Automate_Doc/Bedrock-Summarizer
│
├── lambda/
│   ├── api_handler.py                    # Lambda function triggered by API Gateway (manual trigger)
│   ├── handler.py                        # Main Lambda function triggered by S3 uploads
│   └── utils/
│       ├── s3_helper.py                  # S3 read/write helpers
│       ├── bedrock_client.py             # Amazon Bedrock client for summarizing
│       ├── textract.py                   # Extract text from PDFs/images via Textract
│       ├── comprehend_agent.py           # Analyze summary text using Amazon Comprehend
│       └── dynamodb_helper.py            # Store metadata (summary, key points, etc.) to DynamoDB
│
├── templates/
│   └── prompt.txt                        # Customizable prompt template used with Bedrock
│
├── README.md                             # Project overview and setup guide
└── requirements.txt                      # Python dependencies for development or packaging
```
---
## **Resoruces**


---

## **Future Enhancements**

- Add an S3 lifecycle rule to automatically archive or delete processed documents and summaries after a certain period.
- Add notifications with SNS or SES so users can receive emails or messages when summaries are ready.
- Support additional file types like DOCX or XLSX using Amazon Textract's expanded capabilities or third-party libraries.
- Add versioning or history tracking in DynamoDB so users can reprocess or compare older summaries.
- Create a front-end dashboard (e.g., using React or Streamlit) to upload documents and view summaries directly.
- Secure the API endpoint with IAM roles, Cognito, or API keys to prevent unauthorized access.