# Automating Document Intelligence with AWS Bedrock and Serverless AI

## 🏗️**Techinal Architecture**
- WORK IN PROGRESS! -

## 📜**Project Overview**
This project is a serverless, AI-driven pipeline designed to **automate the summarization and analysis of documents** using AWS cloud services. Leveraging **AWS Bedrock**, **Amazon Textract**, and **Amazon Comprehend**, the system processes uploaded documents (PDFs, text files), extracts their content, generates concise summaries, and identifies key insights. Doing all of this without the need for manual review.

## 🛠️**Technologies**
- **AWS Bedrock** : For natural language summarization using foundation models.
- **Amazon S3** : Document storage and event triggering.
- **AWS Lambda (Python)** : Serverless compute to orchestrate the flow.
- **Amazon Textract** : Optical character recognition (OCR) for scanned documents.
- **Amazon Comprehend (Optional)** : Entity extraction, sentiment, key phrases.
- **Amazon DynamoDB (Optional)** : Storing summaries and metadata.
- **Amazon API Gateway (Optional)** : Accessing insights via REST API.