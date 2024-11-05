# On-premises Spark ETL Job
# This job reads a CSV file, performs a simple transformation, and writes the result to parquet format

# TODO: Import the required libraries for AWS Glue
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper

# TODO: Change this to initialize the Spark and GlueContext
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read data from S3
input_path = "s3://demo-bucket-architecting-workloads/netflix_titles.csv"
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Transformation: Convert 'type' column to uppercase and filter for movies
df_transformed = df.withColumn("type", upper(col("type"))).filter(col("type") == "MOVIE")

# Write to S3 in Parquet format
output_path = "s3://demo-bucket-architecting-workloads/output/"
df_transformed.write.parquet(output_path, mode="overwrite")

job.commit()