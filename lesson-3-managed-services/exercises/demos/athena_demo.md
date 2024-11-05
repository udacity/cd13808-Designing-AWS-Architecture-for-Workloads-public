# Demo: Amazon Athena - Efficient Serverless Query Service

## Introduction

Welcome to our demonstration of Amazon Athena, a powerful serverless query service that allows you to efficiently analyze data directly in Amazon S3 without the need for complex ETL processes.

## Step 1: Preparing Your Data

First, let's ensure we have some data to work with:

1. Open the AWS Management Console and navigate to S3.
2. Create a new bucket called "data-analysis-bucket".
3. Upload a CSV file named "sales_data.csv" with the following columns:
   - ProductID
   - ProductName
   - Category
   - Price
   - SaleDate
   - Quantity

## Step 2: Setting Up Athena

Now, let's configure Amazon Athena:

1. In the AWS Console, navigate to Amazon Athena.
2. Set up a query result location in S3:
   - Click on "Settings"
   - Enter "s3://data-analysis-bucket/athena-results/" as the query result location.

## Step 3: Creating a Table

Let's create a table schema to interpret our data:

1. In the Athena Query Editor, run the following SQL command:

```sql
CREATE EXTERNAL TABLE sales_data (
    ProductID STRING,
    ProductName STRING,
    Category STRING,
    Price DECIMAL(10,2),
    SaleDate DATE,
    Quantity INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://data-analysis-bucket/'
TBLPROPERTIES ('skip.header.line.count'='1');
```

## Step 4: Running Queries
Now, let's demonstrate Athena's querying capabilities:
  1. Calculate total sales by category:
    ```sql
    SELECT Category, SUM(Price * Quantity) as TotalSales
    FROM sales_data
    GROUP BY Category
    ORDER BY TotalSales DESC;
    ```
  2. Find the top 5 best-selling products:
    ``` sql
    SELECT ProductName, SUM(Quantity) as TotalSold
    FROM sales_data
    GROUP BY ProductName
    ORDER BY TotalSold DESC
    LIMIT 5;
    ``` 
  3. Analyze sales trends over time:
    ```sql
    SELECT DATE_TRUNC('month', SaleDate) as Month, SUM(Price * Quantity) as MonthlySales
    FROM sales_data
    GROUP BY DATE_TRUNC('month', SaleDate)
    ORDER BY Month;
    ```

## Step 5:  Performance Optimization
To optimize our Athena queries:
  1. Partition the data:
    - Create a new table partitioned by year and month
    - Demonstrate how this improves query performance for date-based queries
  2. Convert data to Parquet format:
    - Show how to convert the CSV to Parquet
    - Create a new table for the Parquet data
    - Compare query performance between CSV and Parquet

## Conclusion:
  - We've seen how Amazon Athena allows us to efficiently query our sales data directly from our S3 data lake, without the need for complex ETL processes or separate compute resources. 
  - Athena's serverless nature means you only pay for the queries you run, making it perfect for ad-hoc analysis, quick insights, and when you need to analyze data without setting up and managing a full data warehouse.