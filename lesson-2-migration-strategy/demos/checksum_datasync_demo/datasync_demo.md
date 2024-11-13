# Demo: Checksum Validation with AWS DataSync

This demo will guide you through the process of using AWS DataSync to transfer data and perform checksum validation to ensure data integrity.

## Prerequisites

- AWS account with necessary permissions
- Source data location (e.g., on-premises storage, Amazon S3 bucket)
- Destination location in AWS (e.g., Amazon S3 bucket, Amazon EFS)

## Step 1: Set Up AWS DataSync

1. Open the AWS Management Console and navigate to DataSync.
2. Click "Create agent" if transferring from on-premises, or skip this step for AWS to AWS transfers.
3. Follow the wizard to deploy the DataSync agent in your source environment.

## Step 2: Create a DataSync Task

1. In the DataSync console, click "Create task".
2. Choose your source location type (on-premises or AWS storage).
3. Select or create the source location.
4. Choose your destination location type.
5. Select or create the destination location.

## Step 3: Configure Task Settings

1. In the "Configure settings" section, ensure "Verify data integrity" is enabled.
2. Choose the verification method:
   - NONE: No additional verification (not recommended for this demo)
   - CHECK_SUM: Performs checksum comparison (recommended)
   - POSIX: Verifies metadata (ownership, permissions) for POSIX-compliant file systems
3. Set other options as needed (e.g., task scheduling, bandwidth limits).

## Step 4: Start the DataSync Task

1. Review your task configuration.
2. Click "Create task".
3. Once created, select the task and click "Start".

## Step 5: Monitor the Transfer

1. In the DataSync console, go to the "History" tab of your task.
2. Monitor the progress of your transfer.
3. Check the "Status" column for any errors or warnings.

## Step 6: Verify Checksum Validation

1. After the task completes, check the "Results" section.
2. Look for "Verify data integrity" in the results.
3. If successful, it will show "Integrity verified" or similar message.
4. If there are any integrity issues, DataSync will report them here.

## Step 7: Review Detailed Logs (Optional)

1. For more detailed information, go to the CloudWatch Logs.
2. Find the log group for your DataSync task.
3. Search for entries related to checksum validation or data integrity.

## Best Practices

- Always enable data integrity verification for important transfers.
- Use CHECK_SUM for general-purpose verification.
- For file systems where ownership and permissions are crucial, use POSIX verification.
- Regularly review and clean up your