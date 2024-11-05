# Demo: Data Validation for AWS Database Migration Service (DMS)

## Introduction

This demo will walk you through the process of validating data migrated using AWS Database Migration Service (DMS). We'll cover setting up validation, running validation tasks, and interpreting the results.

## Prerequisites

- AWS account with DMS configured
- Source and target databases set up
- DMS replication instance and tasks created

## Step 1: Enable Validation

1. Open the AWS DMS console
2. Select your replication task
3. Click "Modify"
4. Under "Table mappings", enable "Validation"
5. Choose validation settings:
   - Full LOB mode: Validates full LOB columns
   - Limited LOB mode: Validates LOB columns up to a specified size
   - Validation only: Performs validation without migrating data
6. Save the changes

## Step 2: Configure Validation Rules

1. In the task settings, go to "Validation settings"
2. Add validation rules:
   - Compare row counts
   - Checksum validation for specific columns
   - Custom SQL queries for complex validations

## Step 3: Run Validation Task

1. Start or restart your DMS task
2. Monitor the task progress in the DMS console

## Step 4: Review Validation Results

1. Once the task completes, go to the "Table statistics" tab
2. Look for the "Validation state" column
3. Check for any tables marked as "Failed validation"

## Step 5: Investigate Validation Failures

1. For failed tables, click on the table name
2. Review the "Validation failures" section
3. Analyze the specific rows or columns that failed validation

## Step 6: Resolve Discrepancies

1. Investigate the root cause of validation failures
2. Common issues include:
   - Data type mismatches
   - Character encoding differences
   - Truncated data
3. Make necessary adjustments to your migration task or source/target schemas

## Step 7: Re-run Validation

1. After making adjustments, re-run the validation task
2. Repeat the process until all tables pass validation

## Conclusion

By following these steps, you can ensure the integrity and accuracy of your data migration using AWS DMS. Regular validation helps maintain data quality and consistency throughout the migration process.