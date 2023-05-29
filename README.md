# ai-bhagavad-gita-lambda
Backend for [Bhagavad Gita AI Guru](https://rai-sandeep.github.io/ai-guru/).

**UI repo**: [ai-guru](https://github.com/rai-sandeep/ai-guru)

## CICD Deploy to AWS Lambda

Automatic deploy to AWS Lambda through GitHub Actions and SAM CLI.  
- GitHub Action config file: [sam-pipeline.yml](.github/workflows/sam-pipeline.yml)  
- SAM template file for creating AWS Lambda function: [template.yaml](template.yaml)  

Needs the following repository secrets (Settings > Secrets and variables > Actions):
- AWS_ACCESS_KEY_ID: AWS Security Credentials access key ID
- AWS_SECRET_ACCESS_KEY: AWS Security Credentials secret access key
- OPENAI_API_KEY: API Key for Open AI API call from the Lambda function

## Stage changes, Commit and Push to remote
Using script: `sh cicd.sh`