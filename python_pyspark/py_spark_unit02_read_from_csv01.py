from pyspark.sql import SparkSession
import os
import pandas as pd

# Read the existing Excel file
dfp = pd.read_excel("py_columns_init.xlsx", engine="openpyxl")

# Add a new column (e.g., 'New Column') with some values
dfp["Day7"] = [
    "Value1",
    "Value2",
    "Value3",
    "Value31",
    "Value32",
    "Value4",
    "Value5",
    "Value6",
    "Value7",
]  # Adjust according to the length of your data

# Save the dataframe back to an Excel file
dfp.to_csv("py_columns_01_new_column.csv", index=False)
os.environ["PYSPARK_PYTHON"] = (
    "C:\\Users\\SergeiSmirnov6\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
)
os.environ["PYSPARK_DRIVER_PYTHON"] = (
    "C:\\Users\\SergeiSmirnov6\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
)
os.environ["HADOOP_HOME"] = "C:\\Program Files\\hardoop"


def basic_spark_example():
    # Create a Spark session
    spark = SparkSession.builder.appName("test").getOrCreate()
    df = spark.read.csv("py_columns_01_new_column.csv", header=True, inferSchema=True)

    # Show first rows
    df.show()

    # Select specific columns
    df.select("Subject", "Day3", "Day5").show()

    # Group by and aggregate
    df.groupBy("Subject").max("Day5").show()

    # Stop Spark session
    spark.stop()


if __name__ == "__main__":
    basic_spark_example()
