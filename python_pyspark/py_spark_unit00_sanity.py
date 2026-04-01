# This is a simple sanity check to ensure that PySpark is working correctly.
# PySpark is a powerful tool for big data processing, and this code
# will create a Spark session, generate a range of numbers,
# and display them to confirm that everything is set up properly.
# If you see the output of the range and the message "Spark is working!",
# then your PySpark environment is ready to use.
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
spark.range(10).show()

print("Spark is working!")

spark.stop()
