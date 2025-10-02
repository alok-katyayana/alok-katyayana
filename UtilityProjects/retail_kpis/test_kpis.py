import os
import pytest
from helper import get_spark, get_s3_filelist 
from etl import extract, transform, analytics

from pyspark.sql.types import StructType, StringType

@pytest.fixture(scope="session")
def test_get_spark():
    spark = get_spark()

    assert spark is not None
    return (spark,)

def test_extract(test_get_spark):
    file_cols = ["testc", "testc1"]
    output_schema = {"ptest": file_cols}
    
    input_schema = StructType().add(file_cols[0], StringType(), False)\
                               .add(file_cols[1], StringType(), False)

    res = extract(
            logger = None,
            spark= test_get_spark[0],
            table="test",
            input_schema=input_schema,
            output_schema=output_schema
            )
    assert res

def test_stage_file_creation():
    prefix = "retail-kpi/stage/ptest.parquet/_SUCCESS"
    res =  get_s3_filelist(prefix)
    
    assert prefix in res

def test_transform(test_get_spark):
    tables = {
            "ptest" : ("select testc as id, testc1 as word, 'lol' as random_part from ptest",
                      ["word", "random_part"]
                       )
            }

    res = transform(logger = None,
                    spark= test_get_spark[0],
                    pool_tables = tables
                    )

    assert res

def test_pool_file_creation():
    prefix = "retail-kpi/pool/ptest.parquet/_SUCCESS"
    res = get_s3_filelist(prefix)
    assert prefix in res

def test_analytics(test_get_spark):
    report_names = ["test_total_count"]
    queries = ["select count(id) as total_count from ptest"]

    analytics(logger = None,
              spark = test_get_spark[0],
              report_names = report_names,
              queries = queries
    )

def test_report_file_creation():
    res = os.path.exists("")
    prefix = "retail-kpi/analytics/test_total_count.csv/_SUCCESS"
    res = get_s3_filelist(prefix)

    assert res
