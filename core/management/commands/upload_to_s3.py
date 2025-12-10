from django.core.management.base import BaseCommand
from django.core.files.storage import default_storage
from about_us.models import FactCard, Leader
from presscentre.models import News
from partners.models import Partner
import boto3
import os
from pathlib import Path


class Command(BaseCommand):
    help = 'Upload local media files to S3 bucket'

    def handle(self, *args, **options):
        # Get AWS credentials
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

        BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
        uploaded_count = 0
        failed_count = 0

        # Upload FactCard icons
        self.stdout.write(self.style.WARNING('\n=== Uploading FACT CARD icons ==='))
        for card in FactCard.objects.all():
            if card.icon:
                local_path = BASE_DIR / card.icon.name
                if local_path.exists():
                    try:
                        with open(local_path, 'rb') as file:
                            s3.upload_fileobj(
                                file,
                                BUCKET_NAME,
                                card.icon.name,
                                ExtraArgs={'ContentType': 'image/png'}
                            )
                        url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{card.icon.name}"
                        self.stdout.write(self.style.SUCCESS(f'✓ Uploaded: {card.icon.name}'))
                        self.stdout.write(f'  URL: {url}')
                        uploaded_count += 1
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'✗ Failed: {card.icon.name} - {str(e)}'))
                        failed_count += 1
                else:
                    self.stdout.write(self.style.WARNING(f'⚠ File not found locally: {local_path}'))

        # Upload Leader photos
        self.stdout.write(self.style.WARNING('\n=== Uploading LEADER photos ==='))
        for leader in Leader.objects.all():
            if leader.photo:
                local_path = BASE_DIR / leader.photo.name
                if local_path.exists():
                    try:
                        with open(local_path, 'rb') as file:
                            s3.upload_fileobj(
                                file,
                                BUCKET_NAME,
                                leader.photo.name,
                                ExtraArgs={'ContentType': 'image/png'}
                            )
                        url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{leader.photo.name}"
                        self.stdout.write(self.style.SUCCESS(f'✓ Uploaded: {leader.photo.name}'))
                        self.stdout.write(f'  URL: {url}')
                        uploaded_count += 1
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'✗ Failed: {leader.photo.name} - {str(e)}'))
                        failed_count += 1
                else:
                    self.stdout.write(self.style.WARNING(f'⚠ File not found locally: {local_path}'))

        # Upload News images
        self.stdout.write(self.style.WARNING('\n=== Uploading NEWS images ==='))
        for news in News.objects.all():
            if news.image:
                local_path = BASE_DIR / news.image.name
                if local_path.exists():
                    try:
                        # Determine content type
                        content_type = 'image/jpeg'
                        if news.image.name.lower().endswith('.png'):
                            content_type = 'image/png'
                        
                        with open(local_path, 'rb') as file:
                            s3.upload_fileobj(
                                file,
                                BUCKET_NAME,
                                news.image.name,
                                ExtraArgs={'ContentType': content_type}
                            )
                        url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{news.image.name}"
                        self.stdout.write(self.style.SUCCESS(f'✓ Uploaded: {news.image.name}'))
                        self.stdout.write(f'  URL: {url}')
                        uploaded_count += 1
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'✗ Failed: {news.image.name} - {str(e)}'))
                        failed_count += 1
                else:
                    self.stdout.write(self.style.WARNING(f'⚠ File not found locally: {local_path}'))

        # Upload Partner logos
        self.stdout.write(self.style.WARNING('\n=== Uploading PARTNER logos ==='))
        for partner in Partner.objects.all():
            if partner.logo:
                local_path = BASE_DIR / partner.logo.name
                if local_path.exists():
                    try:
                        with open(local_path, 'rb') as file:
                            s3.upload_fileobj(
                                file,
                                BUCKET_NAME,
                                partner.logo.name,
                                ExtraArgs={'ContentType': 'image/png'}
                            )
                        url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{partner.logo.name}"
                        self.stdout.write(self.style.SUCCESS(f'✓ Uploaded: {partner.logo.name}'))
                        self.stdout.write(f'  URL: {url}')
                        uploaded_count += 1
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'✗ Failed: {partner.logo.name} - {str(e)}'))
                        failed_count += 1
                else:
                    self.stdout.write(self.style.WARNING(f'⚠ File not found locally: {local_path}'))

        # Summary
        self.stdout.write('\n' + '=' * 80)
        self.stdout.write(self.style.SUCCESS(f'✓ Successfully uploaded: {uploaded_count} files'))
        if failed_count > 0:
            self.stdout.write(self.style.ERROR(f'✗ Failed: {failed_count} files'))
        self.stdout.write('=' * 80)
