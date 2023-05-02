import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1682954081001 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://the-sole-plate/Womens_Shoes.csv"]},
    transformation_ctx="AmazonS3_node1682954081001",
)

# Script generated for node Custom Transform
SqlQuery140 = """
SELECT `brand` AS brand,
       to_date(`dateUpdated`) AS updatedate,
       to_date(`dateAdded`) AS createdate,
       `categories` AS category,
       cast(`prices.amountMin` as decimal(19, 4)) AS price,
       'w' AS sex
FROM myDataSource
"""
CustomTransform_node1682954517080 = sparkSqlQuery(
    glueContext,
    query=SqlQuery140,
    mapping={"myDataSource": AmazonS3_node1682954081001},
    transformation_ctx="CustomTransform_node1682954517080",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1682954632453 = glueContext.write_dynamic_frame.from_catalog(
    frame=CustomTransform_node1682954517080,
    database="gluedb_the_sole_plate",
    table_name="thesoleplate_dbo_statisticsvalues",
    transformation_ctx="AWSGlueDataCatalog_node1682954632453",
)

job.commit()
