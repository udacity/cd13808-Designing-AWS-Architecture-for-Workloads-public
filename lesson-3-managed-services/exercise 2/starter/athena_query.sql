CREATE EXTERNAL TABLE netflix_titles (
    show_id STRING,
    type STRING,
    title STRING,
    director STRING,
    cast STRING,
    country STRING,
    date_added DATE,
    release_year INT,
    rating STRING,
    duration STRING,
    listed_in STRING,
    description STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 's3://your-bucket-name/path/to/netflix_titles/'
TBLPROPERTIES ('skip.header.line.count'='1');