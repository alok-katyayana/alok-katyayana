from helper import get_spark, convert_to_parquet
from pyspark.sql.functions import sum, col

def test_conversion():
    spark = get_spark()
    input_file = "input/test.csv"
    output_file = "output/test.parquet"
    group_col = "country"
    agg_col = "age"
    convert_to_parquet(spark,
                      input_file, 
                      output_file,
                      group_col
                       )

    input_df = spark.read.option("header", True)\
                         .option("inferSchema", True)\
                         .csv(input_file)

    output_df = spark.read.parquet(output_file)

    input_group = input_df.groupBy(group_col).agg(sum(col(agg_col)).alias("value")).collect()
    output_group = output_df.groupBy(group_col).agg(sum(col(agg_col)).alias("value")).collect()

    assert len(input_group) == len(output_group)
    idict = {}
    odict = {}
    for elm1, elm2 in zip(input_group, output_group):
        idict[elm1[group_col]] = elm1.value
        odict[elm2[group_col]] = elm2.value

    for k,v in idict.items():
        assert odict[k] == v


