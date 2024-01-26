import boto3
import os  # Import added for directory operations

# Set default region (optional if already configured elsewhere)
boto3.setup_default_session(region_name='ap-southeast-2')

# Instantiate the S3 resource
s3 = boto3.resource('s3')

bucket_name = 'flask-static12'  # Replace with your desired bucket name

# Create the bucket (only if it doesn't already exist)
if bucket_name not in [bucket.name for bucket in s3.buckets.all()]:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': 'ap-southeast-2'}
    )

local_path = '/home/greg/Aws Projects/cloud-resume/flask_portfolio_site'

# Iterate through files in the directory and upload each one
for root, dirs, files in os.walk(local_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        key = os.path.relpath(file_path, local_path)
        s3.Bucket(bucket_name).upload_file(Filename=file_path, Key=key)