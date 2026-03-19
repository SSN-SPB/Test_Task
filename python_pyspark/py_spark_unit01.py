from pyspark.sql import SparkSession
import os
# PySpark is library for working with big data using Apache Spark.
# It provides an interface for programming Spark with Python.
# PySpark allows you to leverage the power of Spark's distributed computing capabilities while writing code in Python.


# Set environment variables for PySpark
# Note: Adjust the paths to your Python installation if necessary
# PySpark doesn't support 3.12 and 3.13 yet, so make sure to use a compatible version of Python (e.g., 3.11)
os.environ["PYSPARK_PYTHON"] = (
    "C:\\Users\\SergeiSmirnov6\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
)
os.environ["PYSPARK_DRIVER_PYTHON"] = (
    "C:\\Users\\SergeiSmirnov6\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
)
os.environ["HADOOP_HOME"] = "C:\\Program Files\\hardoop"


def basic_spark_example():
    # Create a Spark session
    spark = SparkSession.builder.appName("BasicSparkExample").getOrCreate()

    # Create sample data
    data = [("Alice", 25), ("Bob", 30), ("Bob21", 21), ("Bob43", 43), ("Charlie", 35)]

    # Define columns
    columns = ["Name", "Age"]

    # Create DataFrame
    df = spark.createDataFrame(data, columns)

    # Show data
    df.show()

    # Filter data
    df_filtered = df.filter(df.Age > 28)

    # Show filtered data
    df_filtered.show()

    # Need to save the filtered DataFrame to a CSV files within output directory named "df_filtered".
    # The CSV file should include a header row with column names.
    # the winutils.exe is required for Hadoop to work properly on Windows.
    # It provides necessary utilities for Hadoop to function correctly,
    # such as handling file permissions and other operations
    # that are essential for Hadoop's operation on Windows.
    # Without winutils.exe, you may encounter errors when trying to run Hadoop or Spark on a Windows system.
    # Make sure to download the appropriate version of winutils.exe
    # and place it in the specified HADOOP_HOME directory for your setup.
    # ✅ Save to CSV
    df_filtered.write.mode("overwrite").option("header", True).csv("df_filtered")

    # Stop Spark session
    spark.stop()


if __name__ == "__main__":
    basic_spark_example()
