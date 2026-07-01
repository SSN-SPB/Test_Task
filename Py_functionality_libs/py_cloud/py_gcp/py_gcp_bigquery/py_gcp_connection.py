# This code demonstrates how to connect to Google Cloud Storage using the Google Cloud Client Library for Python.
# It lists all the buckets in your GCP project.
# Make sure you have the appropriate permissions and that your environment
# is set up with the necessary credentials to access GCP services.
# Note: To run this code, you need to have the `google-cloud-storage` library installed
# and properly configured with your GCP credentials. You can install it using pip:
# pip install google-cloud-storage
# export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account.json"from google.cloud import storage


def list_buckets():
    # Create client (this is your "connection" to GCP)
    client = storage.Client()

    # List buckets
    buckets = client.list_buckets()

    print("Buckets in your project:")
    for bucket in buckets:
        print(bucket.name)


if __name__ == "__main__":
    list_buckets()
