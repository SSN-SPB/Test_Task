from google.cloud import storage
from google.oauth2 import service_account

# pip install google-auth

credentials = service_account.Credentials.from_service_account_file(
    "path/to/service-account.json"
)

client = storage.Client(credentials=credentials, project=credentials.project_id)

for bucket in client.list_buckets():
    print(bucket.name)
# Verify connection details
print(client.project)
