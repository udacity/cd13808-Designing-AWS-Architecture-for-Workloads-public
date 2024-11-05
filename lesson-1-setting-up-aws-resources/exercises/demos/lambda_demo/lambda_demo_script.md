# Converting an On-Premises File Monitor to AWS Lambda with SNS Notifications

## Step 1: Convert On-Premises Function
In this demo, we'll convert an on-premises function that monitors a directory for new files to an AWS Lambda function that monitors an S3 bucket and sends notifications using Amazon SNS when a new file is uploaded.



This script watches a directory for new files and prints a message when a new file is detected.

## Step 2: Plan the AWS Lambda Conversion
To convert this to AWS Lambda, we need to make several changes:
- Remove the continuous loop (Lambda functions are event-driven)
- Replace file system operations with S3 event handling
- Implement SNS notifications using the AWS SDK for SNS

## Step 3: Import Required Libraries
First, let's import the necessary AWS libraries:
```python
import boto3
```

- Boto3 is the official AWS Software Development Kit (SDK) for Python. 
- It provides a Python API that allows developers to create, configure, and manage AWS services programmatically. 
- With Boto3, you can interact with various AWS services like Lambda, SNS and SES 
- We'll leverage boto3 to interact with AWS Simple Notificaiton Service or SNS.

## Step 4: Set Up SNS Configuration
We'll use environment variables to configure the SNS topic:
```python
sns_client = boto3.client('sns')
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']
```

Here, we're creating an SNS client using boto3 and getting the SNS topic ARN from an environment variable.

## Step 5: Create the Lambda Handler
Now, let's create the main Lambda function:

```python
def lambda_handler(event, context):
    
    print(event)
    
    # Extract bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['eventName']

    # Send an SNS notification
    response = sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=f'A new file has been uploaded to {bucket_name}: {object_key}',
        Subject='New File Uploaded'
    )

    return {
        'statusCode': 200,
        'body': f'Notification sent for file: {object_key}'
    }
```

This function extracts the S3 bucket and object information from the event and sends an SNS notification using the AWS SDK for SNS.

## Step 6: Configure IAM Role with Lambda, and S3 Permissions

## Step 7: Create SNS Topic 


## Step 7: Deploy the Lambda Function
  1. Go to the AWS Management Console and navigate to Lambda.
  2. Click "Create function" and choose "Author from scratch".
  3. Name your function and select Python 3.8 as the runtime.
  4. In the "Function code" section, paste our Lambda code.
  5. Set up an environment variable:
  - Key: SNS_TOPIC_ARN
  - Value: [Your SNS Topic ARN]
In the "Execution role" section, create or select a role with permissions for S3 and SNS.

## Step 8: Configure S3 Trigger
  1. In the Lambda function designer, click "Add trigger" and Select S3.
  2. Choose the S3 bucket you want to monitor.
  3. Set the event type to "All object create events".

## Step 9: Set Up Amazon SNS
  1. Go to the Amazon SNS console.
  2. Create a new topic or select an existing one.
  3. Note the Topic ARN and use it in your Lambda function's environment variable.
  4. Add subscriptions to the topic (e.g., email, SMS) to receive notifications.

## Step 10: Test the Function
1. Upload a file to your S3 bucket.
2. Check the subscribed endpoints (e.g., email inbox) for the SNS notification.
3. Review the CloudWatch logs for your Lambda function to ensure it executed correctly.

