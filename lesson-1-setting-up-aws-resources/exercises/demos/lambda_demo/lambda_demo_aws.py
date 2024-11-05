import json
import boto3
import os

sns_client = boto3.client('sns')
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

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