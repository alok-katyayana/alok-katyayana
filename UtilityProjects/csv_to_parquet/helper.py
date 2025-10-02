import logging
from pyspark.sql import SparkSession
from pyspark.errors import AnalysisException


def get_spark(logger=None):
    if logger is None:
        logger = logging.getLogger("default")

    spark = SparkSession.builder.master("local").appName("csv_to_parquet")\
                .config("spark.hadoop.fs.s3a.aws.credentials.provider", 
                        "com.amazonaws.auth.DefaultAWSCredentialsProviderChain")\
                .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")\
                .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.1")\
             .getOrCreate()
    logger.info("Spark Session Created")
    return spark


def convert_to_parquet(spark, ipath, opath, partb, logger=None):
    if logger is None:
        logger = logging.getLogger("default")
    
    options_dict = {"header": True,
                    "inferSchema": True}
    try:
        df = spark.read.options(**options_dict).csv(ipath)
    except AnalysisException as e:
        logger.error(f"File not present at the path: {ipath}")
        logger.error(str(e))
        return False

    df.write.format("parquet").mode("overwrite")\
            .partitionBy(partb).save(opath)


    return True


