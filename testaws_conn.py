import boto3
import time
from botocore.exceptions import ClientError

# Initialize a session using Amazon S3
s3 = boto3.client('s3')

def create_s3_bucket(bucket_name):
    try:
        # Create the S3 bucket
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint':'ap-south-1'
            }


        )
        print(f"Bucket '{bucket_name}' created successfully!")
        return response
    except ClientError as e:
        print(f"Error creating bucket {bucket_name}: {e}")
        return None

if __name__ == "__main__":
    # Create a unique bucket name using a timestamp
    bucket_name = f"json-bucket-{int(time.time())}"

    # Create the bucket
    create_s3_bucket(bucket_name)
