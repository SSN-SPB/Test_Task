from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
spark.range(10).show()

print("Spark is working!")

spark.stop()
