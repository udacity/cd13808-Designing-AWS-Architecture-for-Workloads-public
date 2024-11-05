# Converting Spark Job to Run on AWS Glue

## Intro
- In this video we're going to walk through the soluton for converting our on-premises Spark job to run on AWS Glue. 

## Modifying On-Prem Code
- Let's begin by looking at our original Spark code. 
- This job 
  - reads a CSV file, 
  - performs a simple transformation by dropping a column 
  - and writes the result back as a parquet file. 
- Now, let's convert this to work with AWS Glue.

## Converting to Work with Glue

1. First, we need to import the necessary AWS Glue libraries. We'll add these at the top of our script:
  ```python
  import sys
  from pyspark.context import SparkContext
  from awsglue.context import GlueContext
  from awsglue.job import Job
  from awsglue.utils import getResolvedOptions
  ```

2. Next, we need to initialize the Glue context. This replaces our original SparkSession initialization:

  ```
  args = getResolvedOptions(sys.argv, ['JOB_NAME'])
  sc = SparkContext()
  glueContext = GlueContext(sc)
  spark = glueContext.spark_session
  job = Job(glueContext)
  job.init(args['JOB_NAME'], args)
  ```

3. Now, let's modify our input and output paths to use S3. We'll change the file paths to S3 URIs

  - Input:
    ```python
    # Read CSV from S3
    df = spark.read.csv("s3://demo-bucket-architecting-workloads/input/global_EV_Data_2024.csv", header=True)
    ```
  - Output:
    ```python
    # Write to S3 in Parquet format
    df_transformed.write.parquet("s3://demo-bucket-architecting-workloads/output/transformed_global_EV_Data_2024.csv")
    ```

   Notice that we're now reading from and writing to S3 buckets instead of local file paths.

   Our transformation logic remains the same, so we don't need to change anything there.

4. Finally, we need to add a job commit at the end to properly finish the Glue job:
   ```python
   job.commit()
   ```

5. Now that we've modified our Spark job to work with AWS Glue, let's deploy it to the AWS environment. Follow these steps carefully:

  - Log into the AWS Management Console
     - Open your web browser and navigate to the AWS Management Console
     - Sign in with your AWS account credentials

  - Navigate to AWS Glue
    - In the AWS Management Console, search for "Glue" in the search bar
    - Click on "AWS Glue" to open the Glue console
  - Create a new Glue job
    - In the AWS Glue console, click on "Jobs" in the left sidebar
    - Click the "Create job" button
    - Choose "Spark script editor" as the job type
    - Give your job a meaningful name, e.g., "MyFirstGlueJob"
  - Set up the script
    - In the script editor, delete any existing boilerplate code
    - Copy our modified Glue script and paste it into the editor
    - Click "Save" to save the script
  -  Configure job details
    - Scroll down to the "Job details" section
    - Set the IAM role:
      - If you have an existing IAM role with appropriate permissions, select it
      - If not, click "Create IAM role" and follow the prompts to create a new role
    - Choose the Glue version (e.g., Glue 3.0)
    - Set the language to "Python 3"
    - Set the worker type (e.g., "G.1X")
    - Set the number of workers (e.g., 2)
  -  Set up job parameters
    - Scroll to the "Job parameters" section
    - Add any necessary job parameters, such as:
      - --JOB_NAME: ${job_name}
      - --input_path: s3://your-bucket/input/
      - --output_path: s3://your-bucket/output/
  -  Configure job bookmarks (optional)
    - Scroll to the "Advanced properties" section
    - Set "Job bookmark" to "Enable" if you want to use job bookmarks
  - Save the job
    - Click the "Save" button at the top of the page to save all your job configurations
  - Run the job
    - After saving, click the "Run job" button
    - In the confirmation dialog, review the settings and click "Run job" to start the Glue job

  - Monitor the job
    - You'll be taken to the job run details page
    - Here you can monitor the progress of your job
    - Check the logs for any errors or output
  - Verify the results
    - Once the job completes successfully, navigate to your output S3 bucket
    - Verify that the transformed data has been written correctly