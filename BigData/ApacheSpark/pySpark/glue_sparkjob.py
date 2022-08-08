import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# https: // docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-samples-legislators.html


glueContext = GlueContext(SparkContext.getOrCreate())

# Read Data from crawled database
persons = glueContext.create_dynamic_frame.from_catalog(
    database="legislators",
    table_name="persons_json")
print("Count: ", persons.count())
persons.printSchema()


# Joined Table
Joinedtable = Join.apply(persons, orders, "Order ID", "Order ID")

# Droping a Table

Joined.drop_fields(["Order ID"])


# Writing the data back to s3 bucket or any other datastore


glueContext.write_dynamic_frame.from_options(persons, connection_type="s3",
                                             connection_options={"path": "s3://etldata01/person"}, format="parquet")
