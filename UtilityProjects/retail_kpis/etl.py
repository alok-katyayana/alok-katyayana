import logging
import os
from pyspark.errors import AnalysisException
from pyspark.storagelevel import StorageLevel 

def extract(logger:logging, spark, table:str, input_schema, output_schema:dict):
    if not logger:
        logger = logging.getLogger(__name__)

    
    logger.info("Mining raw data")
    try:
        s3_loc = "s3a://alok-chaturvedi-demo/retail-kpi"
        raw_data = spark.read.option("enforceSchema", False)\
                             .option("header", True)\
                             .schema(input_schema)\
                             .format("csv")\
                             .load(f"{s3_loc}/raw/{table}.csv")\
                             .sample(fraction=1) ## Because of my 8GB ram Arch Linux

        raw_data.persist(StorageLevel.DISK_ONLY)

        logger.info("Raw Data")
        raw_data.show(5)
                
    except AnalysisException as e:
        logger.error("Error Reading the raw file")
        logger.error(str(e))
        return False

    try:
        for tab, col in output_schema.items():
            output_data = raw_data.select(col)
            logger.info(f"{tab}: data")
            output_data.show(5)

            output_data.write\
                       .format("parquet")\
                       .mode("overwrite")\
                       .save(f"{s3_loc}/stage/{tab}.parquet")

            logger.info(f"Table {tab} created in Pool Schema.")

        return True

    except Exception as e:
        logger.error("Error Writing stage tables")
        logger.error(str(e))

    finally:
        raw_data.unpersist()



def transform(logger, spark, pool_tables:dict):
    if not logger:
        logger = logging.getLogger(__name__)
    
    res = True

    for k,v in pool_tables.items():
        try:
            s3_loc = "s3a://alok-chaturvedi-demo/retail-kpi"
            data = spark.read.parquet(f"{s3_loc}/stage/{k}.parquet")
            data.createOrReplaceTempView(k)
            output = spark.sql(v[0])
            output.persist(StorageLevel.DISK_ONLY)
            logger.info(f"{k}: data")
            logger.info(f"{v}: query")
            output.show(5)
            output.write\
                        .format("parquet")\
                        .mode("overwrite")\
                        .partitionBy(v[1])\
                        .save(f"{s3_loc}/pool/{k}.parquet")
            with open("meta", "a", encoding="utf-8") as meta:
                meta.write(f"{k}.parquet\n")
    
            logger.info("Transformation Successful")

        except Exception as e:
            logger.error(f"Error Transforming {k} tables")
            logger.error(str(e))
            res = False
        finally:
            output.unpersist()

    return res


def analytics(logger, spark,  report_names, queries):
    if not logger:
        logger = logging.getLogger(__name__)

    s3_loc = "s3a://alok-chaturvedi-demo/retail-kpi"

    with open("meta") as meta:
        tables = meta.readlines()
    all_data = {table.strip(): 1 for table in tables}

    logger.info(f"All Tables: {all_data}")
    try:
        for elm in all_data.keys():
            if ".parquet" not in elm:
                continue
            logger.info(f"Reading file pool/{elm}") 
            data = spark.read.parquet(f"{s3_loc}/pool/{elm}")
            data.createOrReplaceTempView(elm.replace(".parquet", ""))
            logger.info(f"Data Loaded: {elm}")
            data.show(5)


    except Exception as e:
        logger.error("Cannot Load datasets")
        logger.error(str(e))
        return False

    try:
        for report_name, query in zip(report_names, queries):
            data = spark.sql(query)
            data.persist(StorageLevel.DISK_ONLY)
            logger.info("Report Data")
            data.show(5)
            data.repartition(1).write.format("csv")\
                                     .option("header", True)\
                                     .mode("overwrite")\
                                     .save(f"{s3_loc}/analytics/{report_name}.csv")
            data.unpersist()
            logger.info(f"Report {report_name} generated!")

    except Exception as e:
        logger.error("Cannot Generate Reports!")
        logger.error(str(e))
        return False


    return True



