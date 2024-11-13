# Deploying a Notification Lambda Function on AWS

## Prerequisites

- AWS account with access to Lambda, S3, and SES (Simple Email Service).
- AWS CLI installed and configured on your local machine.

## Step-by-Step Instructions

### Step 1: Set Up Amazon S3 and SES

1. **Create an S3 Bucket:**
   - Navigate to the **S3 Console**.
   - Click **Create bucket** and provide a unique name.
   - Configure settings as needed and create the bucket.

2. **Verify an Email Address in SES:**
   - Navigate to the **SES Console**.
   - In the **Email Addresses** section, click **Verify a New Email Address**.
   - Enter the email address you want to use for notifications and verify it.

### Step 2: Create the Lambda Function

1. **Navigate to the Lambda Console:**
   - Go to the AWS Management Console and select **Lambda**.

2. **Create a New Lambda Function:**
   - Click **Create function**.
   - Choose **Author from scratch**.
   - Name the function (e.g., `S3UploadNotifier`).
   - Choose **Python 3.x** as the runtime.
   - Create a new execution role with basic Lambda permissions.

3. **Configure the Function:**
   - Use the provided Lambda function code (see solution below).
   - Set the environment variables for the S3 bucket name and SES email address.

4. **Add an S3 Trigger:**
   - Under **Function overview**, click **Add trigger**.
   - Select **S3** and configure it to trigger on object creation events in your bucket.

### Step 3: Test the Lambda Function

1. **Upload a File to the S3 Bucket:**
   - Use the AWS Console or CLI to upload a file to the bucket.

2. **Check for Notification:**
   - Verify that an email notification is sent to the specified email address.

## Conclusion

By following these steps, you will have a Lambda function that sends an email notification whenever a file is uploaded to a specified S3 bucket.