# Converting the Local Function to AWS Lambda

## Step-by-Step Instructions

### Step 1: Prepare the Lambda Function Code

1. **Modify the Local Code:**
   - Replace the local directory watching logic with S3 event handling.
   - Use the provided Lambda function code to send an email via SES.

2. **Set Environment Variables:**
   - In the Lambda Console, set environment variables for `SENDER_EMAIL` and `RECIPIENT_EMAIL`.

### Step 2: Configure AWS Services

1. **Set Up SES:**
   - Ensure the sender and recipient emails are verified in SES.
   - Adjust SES sending limits if necessary.

2. **Configure S3 Trigger:**
   - Ensure the S3 bucket is set to trigger the Lambda function on object creation.

### Step 3: Deploy and Test

1. **Deploy the Lambda Function:**
   - Save the function code in the Lambda Console and deploy it.

2. **Test the Function:**
   - Upload a test file to the S3 bucket.
   - Verify that the notification email is received.

## Conclusion

By converting the local function to an AWS Lambda function, you can automate notifications for file uploads to S3, leveraging AWS's scalable and serverless infrastructure.