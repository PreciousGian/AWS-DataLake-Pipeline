import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource = glueContext.create_dynamic_frame.from_catalog(database="default", table_name="raw_data")
transformed = datasource.drop_fields(['unnecessary_column'])
glueContext.write_dynamic_frame.from_options(
    frame=transformed, connection_type="s3",
    connection_options={"path": "s3://processed-bucket/"},
    format="json"
)
job.commit()
