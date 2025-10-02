import logging
import sys

from pyspark.sql.types import (
        DateType, StringType, StructType, StructField, DoubleType
        )

from helper import get_spark
from etl import extract, transform , analytics


if __name__ == "__main__":

    logger = logging.getLogger("retail_app")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info("Set to log!")
    
    spark = get_spark(logger)
    if spark is None:
        logger.error("Unable to create a spark Session")
        sys.exit(1)

    TABLE = "retail"
    input_schema = StructType()\
                        .add("InvoiceNo", StringType(), False)\
                        .add("StockCode", StringType(), False)\
                        .add("Description", StringType(), False)\
                        .add("Quantity", DoubleType(), False)\
                        .add("InvoiceDate", StringType(), False)\
                        .add("UnitPrice", DoubleType(), False)\
                        .add("CustomerID", StringType(), False)\
                        .add("Country", StringType(), False)

    output_schema = {
           "orders" : ["InvoiceNo", "Quantity",  "CustomerID", "StockCode", "InvoiceDate"],
           "products" : ["StockCode", "Description", "UnitPrice"],
            "customers" : ["CustomerID", "Country"]
            }


    res =  extract(logger,
                   spark,
                   TABLE,
                   input_schema,
                   output_schema)


    if not res:
        logger.error("Counld not run extract!")


    pool_tables = {
            "orders" : ("""
            select InvoiceNo, Quantity,  CustomerID, StockCode, 
            to_date(substring(InvoiceDate,1,10), "dd-LL-yyyy") as InvoiceDate,
            substring(to_date(substring(InvoiceDate,1,10), "dd-LL-yyyy"), 1,7) as YearMonth
            from
            orders
            """, ["YearMonth"]),
            "products" : ( """
                select StockCode, Description, UnitPrice,
                case when UnitPrice < 10 then 'low'
                     when UnitPrice < 100 then 'medium'
                     when UnitPrice >= 100 then 'high'
                end as PriceBucket
                from
                products
            """, ["PriceBucket"]),
            "customers" : ("select CustomerID, Country from customers",
                           ["Country"])
            }

    res = transform(logger,
                    spark,
                    pool_tables
                    )
    
    if not res:
        logger.error("There was some error transforming data")
    

    report_names = ["top_five_customers", "sales_trends", "top_three_selling_products"]
    queries = ["""
          WITH base as (
          Select c.CustomerID, c.Country, sum(o.Quantity * p.UnitPrice) as spending
          from customers c join orders o on c.CustomerID = o.customerID
          join products p on p.StockCode = o.StockCode
          group by c.CustomerID, c.Country
          ),
          window_on_base as (
          select CustomerID, Country, round(spending,2) as spending, 
          dense_rank() over(order by spending desc) as rn
          from base
          )
          select  CustomerID, Country, spending from window_on_base
          where rn <= 5
          """,

          """
          WITH base as (
          Select trunc(InvoiceDate, "month") InvoiceMonth, sum(o.Quantity * p.UnitPrice) as spending
          from orders o 
          join products p on p.StockCode = o.StockCode
          group by  trunc(InvoiceDate, "month")
          )
          select InvoiceMonth, spending
          from base
          order by InvoiceMonth
          
          """,

            """
          WITH base as (
          Select p.StockCode, sum(o.Quantity * p.UnitPrice) as spending
          from orders o 
          join products p on p.StockCode = o.StockCode
          group by p.StockCode
          ),

          window_on_base as 
          (
          Select StockCode, spending, dense_rank() over(order by spending desc ) as rn
          from base 

          )

          select StockCode
          from window_on_base where 
          rn <= 3

            """
        ]
    res = analytics(logger,
                    spark,
                    report_names,
                    queries
                    )
    
    if not res:
        logger.error("There was some error generating reports")


    spark.stop()       

