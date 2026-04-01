from google.cloud import bigquery
import pandas as pd

client = bigquery.Client()

# Example DataFrame
df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "age": [30, 25]
})

table_id = "your-project.your_dataset.your_table"

job = client.load_table_from_dataframe(df, table_id)

job.result()  # Wait for completion

print("Data uploaded successfully.")