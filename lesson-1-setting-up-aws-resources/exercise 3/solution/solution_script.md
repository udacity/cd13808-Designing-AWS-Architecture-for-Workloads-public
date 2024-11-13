# Converting On-Premises File Monitoring to AWS Lambda

## Introduction

In this lesson, we'll convert an on-premises function that monitors a directory for new files to an AWS Lambda function that monitors an S3 bucket and sends an email notification when a new file is uploaded.

## Part 1: Code Conversion

Let's start by examining our on-premises code and then convert it to work with AWS Lambda and S3.

### On-Premises Code

```python
import os
import time

WATCH_DIR = '/path/to/watch'

def watch_directory():
    print(f"Watching directory: {WATCH_DIR}")
    initial_files = set(os.listdir(WATCH_DIR))

    while True:
        current_files = set(os.listdir(WATCH_DIR))
        new_files = current_files - initial_files
        if new_files:
            for file_name in new_files:
                print(f"New file uploaded: {file_name}")  # TODO: Replace with a notification email
            initial_files = current_files
        time.sleep(5)

# watch_directory()
```

### Step-by-Step Conversion
- Remove unnecessary imports:
  - We don't need os and time modules for the Lambda function.
  - Instead, we'll import boto3 for AWS SDK functionality.
- Replace the main function:
  - Instead of watch_directory(), we'll create a lambda_handler(event, context) function.
  - This is the entry point for our Lambda function.
- Remove the continuous loop:
  - Lambda functions are event-driven, so we don't need a while True loop.
- Parse S3 event information:
  - Extract the bucket name and object key from the Lambda event.
- Replace print statements with email notifications:
  - Use Amazon SES (Simple Email Service) to send email notifications.
- Add environment variables:
  - Use environment variables for email addresses to keep the code flexible.

### Converted Lambda Code
```python
import boto3
import os

ses_client = boto3.client('ses')

SENDER_EMAIL = os.environ['SENDER_EMAIL']
RECIPIENT_EMAIL = os.environ['RECIPIENT_EMAIL']

def lambda_handler(event, context):
    bucket_name = event['Records']['s3']['bucket']['name']
    object_key = event['Records']['s3']['object']['key']

    response = ses_client.send_email(
        Source=SENDER_EMAIL,
        Destination={
            'ToAddresses': [RECIPIENT_EMAIL]
        },
        Message={
            'Subject': {
                'Data': 'New File Uploaded'
            },
            'Body': {
                'Text': {
                    'Data': f'A new file has been uploaded to {bucket_name}: {object_key}'
                }
            }
        }
    )

    return {
        'statusCode': 200,
        'body': f'Notification sent for file: {object_key}'
    }
```

## Part 2: Deployment
Now that we've converted our code, let's deploy it to AWS Lambda and test it.
1. Step 1: Create a new Lambda function
  - Go to the AWS Management Console and navigate to the Lambda service.
  - Click "Create function".
  - Choose "Author from scratch".
  - Enter a name for your function (e.g., "S3FileUploadNotifier").
  - Select Python 3.8 (or later) as the runtime.
  - For execution role, choose "Create a new role with basic Lambda permissions".
  - Click "Create function".
2. Step 2: Configure the Lambda function
  - In the "Function code" section, replace the default code with our converted code.
  - Scroll down to the "Environment variables" section and add two variables:
    - Key: SENDER_EMAIL, Value: your-verified-email@example.com
    - Key: RECIPIENT_EMAIL, Value: recipient@example.com
  - In the "Basic settings" section, increase the timeout to 10 seconds.
  - Click "Save" at the top of the page.
3. Step 3: Configure S3 trigger
  - In the "Designer" section, click "Add trigger".
  - Select "S3" from the dropdown.
  - Choose the S3 bucket you want to monitor.
  - For "Event type", select "All object create events".
  - Acknowledge the recursive invocation warning if your function will be writing to the same bucket.
  - Click "Add".
4. Step 4: Configure SES
  - Go to the Amazon SES console.
  - Verify the email addresses you're using for SENDER_EMAIL and RECIPIENT_EMAIL.
  - If your account is in the SES sandbox, you can only send to verified email addresses.
5. Step 5: Update IAM role
  - Go to the IAM console.
  - Find the role created for your Lambda function.
  - Add the AmazonSESFullAccess policy to the role (Note: In a production environment, you should create a more restrictive policy).
6. Step 6: Test the function
  - Upload a file to your configured S3 bucket.
  - Check your email for the notification.
