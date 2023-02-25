from pyspark.sql import SparkSession
import os

spark_cluster_uri = "local[4]"
csv_path = "data/betaTest.csv"
# os.environ['PYARROW_IGNORE_TIMEZONE'] = "1"

spark = SparkSession.builder().master(spark_cluster_uri
    ).appName("Beta_test").getOrCreate()

df = spark.read.csv("/tmp/resources/zipcodes.csv")
df.printSchema()
