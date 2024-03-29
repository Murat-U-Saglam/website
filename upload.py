from google.cloud import storage
import os

local_directory = os.getcwd()
local_directory = os.path.join(local_directory, "public")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "env.json"
# Initialize a client
client = storage.Client()

bucket_name = "www.hacimuro.com"
bucket = client.get_bucket(bucket_name)

# List objects in the bucket
blobs = bucket.list_blobs()
white_list = ["public"]
# Specify the local directory you want to upload

# Rebuild the site
os.system(command="rm -rf public")
os.system(command="hugo")


def delete_files_in_bucket():
    for blob in blobs:
        blob.delete()
        print(f"Deleted {blob.name} from {bucket_name}")


delete_files_in_bucket()
for root, dirs, files in os.walk(top=local_directory):
    for file in files:
        local_path = os.path.join(root, file)
        # Calculate the relative path within the local directory
        relative_path = os.path.relpath(local_path, local_directory)
        # Replace backslashes with forward slashes for GCS paths
        cloud_path = relative_path.replace("\\", "/")
        # Create a blob object in the bucket
        blob = bucket.blob(cloud_path)
        # Upload the file to GCS
        blob.upload_from_filename(local_path)
        print(f"Uploaded {local_path} to gs://{bucket_name}/{cloud_path}")