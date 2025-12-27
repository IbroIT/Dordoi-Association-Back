from django.core.management.base import BaseCommand
import boto3
from django.conf import settings


class Command(BaseCommand):
    help = 'Update ACL for existing S3 media files to make them publicly accessible'

    def handle(self, *args, **options):
        if not hasattr(settings, 'AWS_STORAGE_BUCKET_NAME'):
            self.stdout.write(self.style.ERROR('S3 not configured'))
            return

        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )

        try:
            # List all objects in media folder
            paginator = s3.get_paginator('list_objects_v2')
            page_iterator = paginator.paginate(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Prefix='media/')

            updated_count = 0
            for page in page_iterator:
                if 'Contents' in page:
                    for obj in page['Contents']:
                        key = obj['Key']
                        try:
                            # Update ACL to public-read
                            s3.put_object_acl(
                                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                                Key=key,
                                ACL='public-read'
                            )
                            updated_count += 1
                            self.stdout.write(f'Updated ACL for: {key}')
                        except Exception as e:
                            self.stdout.write(self.style.WARNING(f'Failed to update {key}: {e}'))

            self.stdout.write(self.style.SUCCESS(f'Successfully updated ACL for {updated_count} files'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error accessing S3: {e}'))