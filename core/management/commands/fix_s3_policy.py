from django.core.management.base import BaseCommand
import boto3
import json
import os


class Command(BaseCommand):
    help = 'Fix S3 bucket policy for public access'

    def handle(self, *args, **options):
        AWS_ACCESS_KEY_ID = os.getenv('BUCKETEER_AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.getenv('BUCKETEER_AWS_SECRET_ACCESS_KEY')
        AWS_REGION = os.getenv('BUCKETEER_AWS_REGION')
        BUCKET_NAME = os.getenv('BUCKETEER_BUCKET_NAME')

        if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, BUCKET_NAME]):
            self.stdout.write(self.style.ERROR('Missing AWS credentials'))
            return

        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

        try:
            # 1. Check current public access block
            self.stdout.write(self.style.WARNING('=== Current Public Access Block Settings ==='))
            try:
                pab = s3.get_public_access_block(Bucket=BUCKET_NAME)
                self.stdout.write(f"BlockPublicAcls: {pab['PublicAccessBlockConfiguration']['BlockPublicAcls']}")
                self.stdout.write(f"IgnorePublicAcls: {pab['PublicAccessBlockConfiguration']['IgnorePublicAcls']}")
                self.stdout.write(f"BlockPublicPolicy: {pab['PublicAccessBlockConfiguration']['BlockPublicPolicy']}")
                self.stdout.write(f"RestrictPublicBuckets: {pab['PublicAccessBlockConfiguration']['RestrictPublicBuckets']}")
            except Exception as e:
                self.stdout.write(f"Error getting public access block: {str(e)}")

            # 2. Set public access block to allow bucket policies
            self.stdout.write(self.style.WARNING('\n=== Setting Public Access Block (Allow Bucket Policies) ==='))
            s3.put_public_access_block(
                Bucket=BUCKET_NAME,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': True,  # Keep ACLs blocked (Bucketeer requirement)
                    'IgnorePublicAcls': True,
                    'BlockPublicPolicy': False,  # MUST be False to allow bucket policies
                    'RestrictPublicBuckets': False  # MUST be False to allow public access via policies
                }
            )
            self.stdout.write(self.style.SUCCESS('✓ Public access block configured'))

            # 3. Set bucket policy for public read access
            self.stdout.write(self.style.WARNING('\n=== Setting Bucket Policy ==='))
            bucket_policy = {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "PublicReadGetObject",
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
            self.stdout.write(self.style.SUCCESS('✓ Bucket policy set for public read access'))

            # 4. Verify bucket policy
            self.stdout.write(self.style.WARNING('\n=== Verifying Bucket Policy ==='))
            policy = s3.get_bucket_policy(Bucket=BUCKET_NAME)
            self.stdout.write(policy['Policy'])

            # 5. Set CORS
            self.stdout.write(self.style.WARNING('\n=== Setting CORS ==='))
            cors_config = {
                'CORSRules': [
                    {
                        'AllowedHeaders': ['*'],
                        'AllowedMethods': ['GET', 'HEAD', 'PUT', 'POST', 'DELETE'],
                        'AllowedOrigins': ['*'],
                        'ExposeHeaders': ['ETag'],
                        'MaxAgeSeconds': 3000
                    }
                ]
            }
            s3.put_bucket_cors(Bucket=BUCKET_NAME, CORSConfiguration=cors_config)
            self.stdout.write(self.style.SUCCESS('✓ CORS configured'))

            # 6. Test with a file
            self.stdout.write(self.style.WARNING('\n=== Testing File Access ==='))
            response = s3.list_objects_v2(Bucket=BUCKET_NAME, MaxKeys=5)
            if 'Contents' in response:
                for obj in response['Contents']:
                    key = obj['Key']
                    url = f"https://{BUCKET_NAME}.s3-{AWS_REGION}.amazonaws.com/{key}"
                    self.stdout.write(f"\nFile: {key}")
                    self.stdout.write(f"URL: {url}")
                    self.stdout.write(f"Try accessing this URL in browser - it should work now!")
            else:
                self.stdout.write(self.style.WARNING('No files in bucket yet'))

            self.stdout.write(self.style.SUCCESS('\n\n🎉 All configurations completed successfully!'))
            self.stdout.write(self.style.SUCCESS('Files should now be publicly accessible!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'\n❌ Error: {str(e)}'))
            import traceback
            self.stdout.write(traceback.format_exc())
