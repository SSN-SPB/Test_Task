from google.cloud import bigquery

client = bigquery.Client()

dataset_id = "your-project.my_dataset"
dataset = bigquery.Dataset(dataset_id)
dataset.location = "US"

dataset = client.create_dataset(dataset, exists_ok=True)

table_id = f"{dataset_id}.my_table"

schema = [
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("age", "INTEGER"),
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table, exists_ok=True)

print("Dataset and table created.")