import boto3
import os

# Initialize the SES client
ses_client = boto3.client('ses')

# Environment variables
SENDER_EMAIL = os.environ['SENDER_EMAIL']
RECIPIENT_EMAIL = os.environ['RECIPIENT_EMAIL']

def lambda_handler(event, context):
    # Extract bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Send an email notification
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