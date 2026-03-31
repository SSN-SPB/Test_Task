from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema

def validate_data():
    # ✅ Define schema INSIDE the task
    schema = DataFrameSchema({
        "name": Column(str, nullable=False),
        "age": Column(int, checks=pa.Check.in_range(0, 120), nullable=False),
        "salary": Column(float, nullable=True)
    })

    # Example dataset (in real case, you'd load from DB / file)
    data = {
        "name": ["Alice", "Bob", None, "David"],
        "age": [25, -5, 30, None],
        "salary": [50000, 60000, None, 70000]
    }

    df = pd.DataFrame(data)

    # ✅ This will raise error if validation fails
    try:
        schema.validate(df)
        print("Dataframe first 5 values:")
        print(df.head())
    except Exception as e:
        print(f"Validation error: {e}")

# Define DAG
dag = DAG(
    "data_validation_example",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
)

task = PythonOperator(
    task_id="validate_data",
    python_callable=validate_data,
    dag=dag
)

if __name__ == "__main__":
    validate_data()
    print(task.show_return_value_in_logs)
