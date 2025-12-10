from django.core.management.base import BaseCommand
import boto3
import json
import os


class Command(BaseCommand):
    help = 'Configure S3 bucket for public access'

    def handle(self, *args, **options):
        # Get AWS credentials from environment
        AWS_ACCESS_KEY_ID = os.getenv('BUCKETEER_AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.getenv('BUCKETEER_AWS_SECRET_ACCESS_KEY')
        AWS_REGION = os.getenv('BUCKETEER_AWS_REGION')
        BUCKET_NAME = os.getenv('BUCKETEER_BUCKET_NAME')

        if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, BUCKET_NAME]):
            self.stdout.write(
                self.style.ERROR('Missing required environment variables: BUCKETEER_AWS_ACCESS_KEY_ID, BUCKETEER_AWS_SECRET_ACCESS_KEY, BUCKETEER_AWS_REGION, BUCKETEER_BUCKET_NAME')
            )
            return

        # Initialize S3 client
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

        try:
            # 1. Disable public access block
            self.stdout.write('Disabling public access block...')
            s3.put_public_access_block(
                Bucket=BUCKET_NAME,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': False,
                    'IgnorePublicAcls': False,
                    'BlockPublicPolicy': False,
                    'RestrictPublicBuckets': False
                }
            )
            self.stdout.write(self.style.SUCCESS('✓ Public access block disabled'))

            # 2. Set bucket policy for public access to all files
            self.stdout.write('Setting bucket policy for public access...')
            bucket_policy = {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": "s3:GetObject",
                        "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*"
                    }
                ]
            }

            s3.put_bucket_policy(
                Bucket=BUCKET_NAME,
                Policy=json.dumps(bucket_policy)
            )
            self.stdout.write(self.style.SUCCESS('✓ Bucket policy set'))

            # 3. Set CORS configuration
            self.stdout.write('Setting CORS configuration...')
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
            self.stdout.write(self.style.SUCCESS('✓ CORS configuration set'))

            # 4. Update ACL for existing media files
            self.stdout.write('Updating ACL for existing media files...')
            paginator = s3.get_paginator('list_objects_v2')
            page_iterator = paginator.paginate(Bucket=BUCKET_NAME)

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
                            self.stdout.write(f"✓ Updated ACL for: {key}")
                        except Exception as e:
                            self.stdout.write(self.style.WARNING(f"✗ Failed to update {key}: {e}"))

            self.stdout.write(self.style.SUCCESS(f'✓ Successfully updated ACL for {updated_count} files'))

            self.stdout.write(
                self.style.SUCCESS(
                    f'\n🎉 All S3 configurations completed successfully!\n'
                    f'Media files should now be publicly accessible at:\n'
                    f'https://{BUCKET_NAME}.s3.amazonaws.com/...'
                )
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Error: {e}'))
            import traceback
            traceback.print_exc()