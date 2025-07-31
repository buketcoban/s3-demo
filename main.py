import boto3
from botocore.client import Config
import uuid

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
    config=Config(signature_version="s3v4"),
)

bucket_name = "demo-bucket"
file_name = f"{uuid.uuid4()}.txt"
file_content = "Merhaba S3, bu dosya localstack içindir."

s3.create_bucket(Bucket=bucket_name)

with open(file_name, "w") as f:
    f.write(file_content)

s3.upload_file(file_name, bucket_name, file_name)
print(f"Yüklendi: {file_name}")

print("Bucket içeriği:")
objects = s3.list_objects_v2(Bucket=bucket_name)
for obj in objects.get("Contents", []):
    print(f" - {obj['Key']}")

# s3.delete_object(Bucket=bucket_name, Key=file_name)
# print(f"Silindi: {file_name}")

