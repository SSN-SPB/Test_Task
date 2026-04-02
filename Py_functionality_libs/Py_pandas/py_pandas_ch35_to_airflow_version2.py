from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema

import logging

def validate_data():
    schema = DataFrameSchema({
        "name": Column(str, nullable=False),
        "age": Column(int, checks=pa.Check.in_range(0, 120), nullable=False),
        "salary": Column(float, nullable=True)
    })

    df = pd.DataFrame({
        "name": ["Alice", "Bob", None, "David"],
        "age": [25, -5, 30, None],
        "salary": [50000, 60000, None, 70000]
    })

    try:
        schema.validate(df)
        logging.info(df.head())
    except Exception as e:
        logging.error("Validation failed", exc_info=True)
        raise   # 🔥 THIS is the key

if __name__ == "__main__":
    validate_data()