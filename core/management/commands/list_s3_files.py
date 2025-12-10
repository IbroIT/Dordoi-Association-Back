from django.core.management.base import BaseCommand
import boto3
import os


class Command(BaseCommand):
    help = 'List all files in S3 bucket'

    def handle(self, *args, **options):
        # Get AWS credentials from environment
        AWS_ACCESS_KEY_ID = os.getenv('BUCKETEER_AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.getenv('BUCKETEER_AWS_SECRET_ACCESS_KEY')
        AWS_REGION = os.getenv('BUCKETEER_AWS_REGION')
        BUCKET_NAME = os.getenv('BUCKETEER_BUCKET_NAME')

        if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, BUCKET_NAME]):
            self.stdout.write(
                self.style.ERROR('Missing required environment variables')
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
            self.stdout.write(f'Files in bucket: {BUCKET_NAME}')
            self.stdout.write('-' * 80)
            
            paginator = s3.get_paginator('list_objects_v2')
            page_iterator = paginator.paginate(Bucket=BUCKET_NAME)
            
            file_count = 0
            for page in page_iterator:
                if 'Contents' in page:
                    for obj in page['Contents']:
                        file_count += 1
                        key = obj['Key']
                        size = obj['Size']
                        url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{key}"
                        self.stdout.write(f"{file_count}. {key} ({size} bytes)")
                        self.stdout.write(f"   URL: {url}")
            
            if file_count == 0:
                self.stdout.write(self.style.WARNING('No files found in bucket'))
            else:
                self.stdout.write(self.style.SUCCESS(f'\nTotal files: {file_count}'))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
