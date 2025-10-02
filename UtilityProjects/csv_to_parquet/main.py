import logging
from helper import get_spark, convert_to_parquet

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")

    logger = logging.getLogger("csv_to_parquet")
    logger.setLevel(logging.DEBUG)



    spark = get_spark(logger)

    input_path = "s3a://alok-chaturvedi-demo/csv-to-parquet/input/retail_data.csv"
    output_path = "s3a://alok-chaturvedi-demo/csv-to-parquet/output/retail_data.parquet"

    res = convert_to_parquet(spark, input_path, output_path, "Country", logger)

    if res:
        logger.info("Conversion Successful")
    else:
        logger.error("Aborting")

    spark.stop()
    logger.info("Spark Session Stopped")


