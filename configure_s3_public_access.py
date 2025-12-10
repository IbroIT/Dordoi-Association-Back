#!/usr/bin/env python3
import boto3
import json
import os

# AWS credentials from Bucketeer environment variables
AWS_ACCESS_KEY_ID = os.environ.get('BUCKETEER_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('BUCKETEER_AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.environ.get('BUCKETEER_AWS_REGION')
BUCKET_NAME = os.environ.get('BUCKETEER_BUCKET_NAME')

if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, BUCKET_NAME]):
    print("❌ Error: Missing required environment variables:")
    print("BUCKETEER_AWS_ACCESS_KEY_ID")
    print("BUCKETEER_AWS_SECRET_ACCESS_KEY")
    print("BUCKETEER_AWS_REGION")
    print("BUCKETEER_BUCKET_NAME")
    exit(1)

# Initialize S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

try:
    # 1. Disable public access block
    print("Disabling public access block...")
    s3.put_public_access_block(
        Bucket=BUCKET_NAME,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': False,
            'IgnorePublicAcls': False,
            'BlockPublicPolicy': False,
            'RestrictPublicBuckets': False
        }
    )
    print("✓ Public access block disabled")

    # 2. Set bucket policy for public access to media/ folder
    print("Setting bucket policy for public access...")
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{BUCKET_NAME}/media/*"
            }
        ]
    }

    s3.put_bucket_policy(
        Bucket=BUCKET_NAME,
        Policy=json.dumps(bucket_policy)
    )
    print("✓ Bucket policy set")

    # 3. Set CORS configuration
    print("Setting CORS configuration...")
    cors_config = {
        'CORSRules': [
            {
                'AllowedHeaders': ['*'],
                'ExposeHeaders': ['ETag', 'x-amz-meta-custom-header'],
                'AllowedMethods': ['HEAD', 'GET', 'PUT', 'POST', 'DELETE'],
                'AllowedOrigins': ['*']
            }
        ]
    }

    s3.put_bucket_cors(
        Bucket=BUCKET_NAME,
        CORSConfiguration=cors_config
    )
    print("✓ CORS configuration set")

    # 4. Update ACL for existing media files
    print("Updating ACL for existing media files...")
    paginator = s3.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=BUCKET_NAME, Prefix='media/')

    updated_count = 0
    for page in page_iterator:
        if 'Contents' in page:
            for obj in page['Contents']:
                key = obj['Key']
                try:
                    s3.put_object_acl(
                        Bucket=BUCKET_NAME,
                        Key=key,
                        ACL='public-read'
                    )
                    updated_count += 1
                    print(f"✓ Updated ACL for: {key}")
                except Exception as e:
                    print(f"✗ Failed to update {key}: {e}")

    print(f"✓ Successfully updated ACL for {updated_count} files")

    print("\n🎉 All S3 configurations completed successfully!")
    print(f"Media files should now be publicly accessible at:")
    print(f"https://{BUCKET_NAME}.s3.amazonaws.com/media/...")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()