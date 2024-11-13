import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql import SparkSession
# TODO: Import the required libraries

# TODO: Change this to initialize the Spark and GlueContext
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# TODO: Change the file path to read from S3
df = spark.read.csv("s3://demo-bucket-architecting-workloads/input/global_EV_Data_2024.csv", header=True)

# Transformation: Drop a column
df_transformed = df.drop("region")

# TODO: Change the file path to write to S3 in Parquet format
df_transformed.write.parquet("s3://demo-bucket-architecting-workloads/output/transformed_global_EV_Data_2024.csv")