# Running a Custom AWS Glue Job

## Prerequisites

- AWS account with access to AWS Glue and S3.
- IAM role with permissions for AWS Glue and S3.

## Steps to Set Up Amazon S3

1. **Create an S3 Bucket:**
   - Log in to your AWS Management Console.
   - Navigate to the **S3** service.
   - Click on **Create bucket**.
   - Enter a unique bucket name (e.g., `your-bucket-name`).
   - Choose a region and configure any additional settings as needed.
   - Click **Create bucket**.

2. **Upload Input Data:**
   - Click on your newly created bucket to open it.
   - Click **Create folder** and name it `LandingZone`.
   - Open the `LandingZone` folder and click **Upload**.
   - Select the `global_electric_vehicle_sales.csv` file you downloaded from Kaggle and upload it.

3. **Create Output Folder:**
   - Go back to the root of your bucket.
   - Click **Create folder** and name it `TransformedZone`.
   - This folder will store the output data after the transformation.

## Steps to Create an IAM Role

1. **Create an IAM Policy:**
   - Navigate to the IAM Console.
   - Select **Policies** and click **Create policy**.
   - Choose the **JSON** tab and enter the following policy that follows the principle of least privilege:

     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": [
             "s3:GetObject",
             "s3:PutObject"
           ],
           "Resource": [
             "arn:aws:s3:::your-bucket-name/LandingZone/*",
             "arn:aws:s3:::your-bucket-name/TransformedZone/*"
           ]
         },
         {
           "Effect": "Allow",
           "Action": [
             "glue:GetJob",
             "glue:CreateJob",
             "glue:StartJobRun",
             "glue:GetJobRun"
           ],
           "Resource": "*"
         }
       ]
     }
     ```

   - Click **Review policy**, give it a name (e.g., `GlueJobPolicy`), and create the policy.

2. **Create an IAM Role:**
   - Go to the **Roles** section in the IAM Console and click **Create role**.
   - Select **Glue** as the service that will use this role.
   - Attach the policy you created (`GlueJobPolicy`).
   - Name the role (e.g., `GlueJobRole`) and create it.

## Steps to Run the AWS Glue Job

1. **Upload the Script:**
   - Save the modified AWS Glue script as a `.py` file and upload it to an S3 bucket.

2. **Create a Glue Job:**
   - Navigate to the AWS Glue Console.
   - Select **Jobs** under the ETL section.
   - Click **Add Job** and fill in the job details:
     - Name: Provide a name for your job.
     - IAM Role: Select the role you created (`GlueJobRole`).
     - Type: Choose **Spark**.
     - Script location: Provide the S3 path to your script file.
     - Temporary directory: Specify an S3 path for temporary storage.

3. **Configure the Job:**
   - Set the **Maximum capacity** and **Worker type** according to your needs.
   - Under **Advanced properties**, set any additional configurations if required.

4. **Run the Job:**
   - Click **Save** and then **Run**.
   - Monitor the job execution in the AWS Glue Console under the **Runs** tab.

5. **Verify Output:**
   - Check the S3 bucket specified in the script for the output Parquet files.

## Conclusion

This exercise demonstrates how to convert an on-premises PySpark job to an AWS Glue job, leveraging AWS's serverless capabilities for scalable ETL operations.