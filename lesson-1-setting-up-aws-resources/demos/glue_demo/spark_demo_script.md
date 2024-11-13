# Converting a Spark ETL Job to AWS Glue

In this demo, we'll walk through the process of converting an on-premises Spark ETL job to run on AWS Glue. 
We'll use a simple ETL job that processes Netflix titles data as an example.

## Step 1: Review the On-premises Spark Job

Let's start by looking at our on-premises Spark job (on_prem_spark_job.py):

[Show the on-premises code]

This job reads a CSV file, converts the 'type' column to uppercase, filters for movies, and writes the result in Parquet format.

## Step 2: Import AWS Glue Libraries

In the AWS Glue job, we need to import specific libraries:

```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper
```

These imports allow us to use AWS Glue's context and job management features.

## Step 3: Initialize GlueContext and Job
Replace the SparkSession initialization with GlueContext and Job initialization:

```python
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
```

This sets up the Glue job and provides access to the Spark session.

## Step 4: Update File Paths
Change the input and output paths to use S3 URIs:

```python
input_path = "s3://your-bucket/data/netflix_titles.csv"
output_path = "s3://your-bucket/output/netflix_movies"
```

Make sure to replace 'your-bucket' with your actual S3 bucket name.

## Step 5: Add Job Commit
At the end of the script, add:

```python
job.commit()
```

This tells Glue that the job has completed successfully.

## Step 6:
Remove the spark.stop() line as Glue manages the Spark session lifecycle.

## Step 7: Deploying the AWS Glue Job

Now that we've modified our Spark job to work with AWS Glue, let's deploy it to the AWS environment. Follow these steps carefully:

1. Log into the AWS Management Console
   - Open your web browser and navigate to the AWS Management Console
   - Sign in with your AWS account credentials

2. Navigate to AWS Glue
   - In the AWS Management Console, search for "Glue" in the search bar
   - Click on "AWS Glue" to open the Glue console

3. Create a new Glue job
   - In the AWS Glue console, click on "Jobs" in the left sidebar
   - Click the "Create job" button
   - Choose "Spark script editor" as the job type
   - Give your job a meaningful name, e.g., "MyFirstGlueJob"

4. Set up the script
   - In the script editor, delete any existing boilerplate code
   - Copy our modified Glue script and paste it into the editor
   - Click "Save" to save the script

5. Configure job details
   - Scroll down to the "Job details" section
   - Set the IAM role:
     - If you have an existing IAM role with appropriate permissions, select it
     - If not, click "Create IAM role" and follow the prompts to create a new role
   - Choose the Glue version (e.g., Glue 3.0)
   - Set the language to "Python 3"
   - Set the worker type (e.g., "G.1X")
   - Set the number of workers (e.g., 2)

6. Set up job parameters
   - Scroll to the "Job parameters" section
   - Add any necessary job parameters, such as:
     - --JOB_NAME: ${job_name}
     - --input_path: s3://your-bucket/input/
     - --output_path: s3://your-bucket/output/

7. Configure job bookmarks (optional)
   - Scroll to the "Advanced properties" section
   - Set "Job bookmark" to "Enable" if you want to use job bookmarks

8. Save the job
   - Click the "Save" button at the top of the page to save all your job configurations

9. Run the job
   - After saving, click the "Run job" button
   - In the confirmation dialog, review the settings and click "Run job" to start the Glue job

10. Monitor the job
    - You'll be taken to the job run details page
    - Here you can monitor the progress of your job
    - Check the logs for any errors or output

11. Verify the results
    - Once the job completes successfully, navigate to your output S3 bucket
    - Verify that the transformed data has been written correctly

Congratulations! You've successfully deployed and run your first AWS Glue job. 
Remember to monitor your AWS usage and costs, and delete any resources you no longer need.
