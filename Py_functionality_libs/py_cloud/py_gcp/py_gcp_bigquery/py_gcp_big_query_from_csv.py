from google.cloud import bigquery

client = bigquery.Client()

table_id = "your-project.your_dataset.your_table"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
)

with open("data.csv", "rb") as source_file:
    load_job = client.load_table_from_file(source_file, table_id, job_config=job_config)

load_job.result()  # Wait for job to complete

print("Loaded data successfully.")
