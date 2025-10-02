from pyspark.sql import SparkSession
import logging

import boto3

S3_BUCKET = "alok-chaturvedi-demo"

def get_spark(logger = None):
    if not logger:
        logger = logging.getLogger(__name__)

    logger.info("Buidling the spark Session")
    try:
        spark = SparkSession.builder.master("local[*]")\
                                   .appName("retail_company")\
                                   .config("spark.executor.instances", "8")\
                                   .config("spark.executor.cores", "8")\
                                   .config("spark.executor.memory", "2g")\
                                   .config("spark.driver.memory", "1g")\
                                   .config("spark.sql.parquet.filterPushdown", True)\
                                   .config("spark.hadoop.fs.s3a.aws.credentials.provider", 
                                           "com.amazonaws.auth.DefaultAWSCredentialsProviderChain") \
                                   .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
                                   .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.1") \
                                   .getOrCreate()

        return spark

    except Exception as e:
        logger.error("Failed to Create spark Session")
        logger.error(str(e))

def get_s3_filelist(prefix):
    client = boto3.client("s3")
    try:
        all_files = client.list_objects(Bucket=S3_BUCKET, Prefix=prefix)
        all_files = [key["Key"] for key in all_files["Contents"]]
    except KeyError:
        all_files = []

    return all_files


