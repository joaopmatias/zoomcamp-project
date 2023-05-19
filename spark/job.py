import re

from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

conf = (
    SparkConf()
    .setAppName('test')
    #.set("spark.jars","gcs-connector-hadoop3-2.2.12-shaded.jar,spark-3.3-bigquery-0.30.0.jar")
    .set("spark.hadoop.google.cloud.auth.service.account.enable","true")
    .set("spark.hadoop.fs.AbstractFileSystem.gs.impl","com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
    .set("spark.hadoop.fs.gs.impl","com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
    .set("spark.hadoop.fs.gs.project.id","taxi-rides-ny-373121")
)

spark = (
    SparkSession
    .builder
    .config(conf=conf)
    .getOrCreate()
)

spark.conf.set("temporaryGcsBucket", "zoomcamp_project_bucket")

df = spark.read.csv("gs://zoomcamp_project_bucket/flights2022/*.csv", header=True)

for a in df.inputFiles():
    (
        spark
        .read
        .csv(a, header=True)
        .write
        .format("bigquery")
        .option("table", "zoomcamp_project_bq." + re.search(r"/(\w+)\.csv$", a).group(1))
        .save()
    )

