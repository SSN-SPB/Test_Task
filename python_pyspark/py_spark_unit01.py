from pyspark.sql import SparkSession
import os
# PySpark is library for working with big data using Apache Spark.
# It provides an interface for programming Spark with Python.
# PySpark allows you to leverage the power of Spark's distributed computing capabilities while writing code in Python.


# Set environment variables for PySpark
# Note: Adjust the paths to your Python installation if necessary
# PySpark doesn't support 3.12 and 3.13 yet, so make sure to use a compatible version of Python (e.g., 3.11)
os.environ["PYSPARK_PYTHON"] = "C:\\Users\\SergeiSmirnov6\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:\\Users\\SergeiSmirnov6\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"

def basic_spark_example():
    # Create a Spark session
    spark = SparkSession.builder.appName("BasicSparkExample").getOrCreate()

    # Create sample data
    data = [
        ("Alice", 25),
        ("Bob", 30),
        ("Charlie", 35)
    ]

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

    # Stop Spark session
    spark.stop()



if __name__ == "__main__":
    basic_spark_example()
