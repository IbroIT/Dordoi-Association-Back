from django.core.management.base import BaseCommand
from about_us.models import FactCard, Leader
from presscentre.models import News
from partners.models import Partner
import boto3
import os


class Command(BaseCommand):
    help = 'Check and display all media files from database'

    def handle(self, *args, **options):
        # Get AWS credentials
        AWS_ACCESS_KEY_ID = os.getenv('BUCKETEER_AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.getenv('BUCKETEER_AWS_SECRET_ACCESS_KEY')
        AWS_REGION = os.getenv('BUCKETEER_AWS_REGION')
        BUCKET_NAME = os.getenv('BUCKETEER_BUCKET_NAME')

        if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, BUCKET_NAME]):
            self.stdout.write(self.style.ERROR('Missing AWS credentials'))
            return

        # Check FactCards
        self.stdout.write(self.style.WARNING('\n=== FACT CARDS ==='))
        for card in FactCard.objects.all():
            if card.icon:
                self.stdout.write(f"ID: {card.id}")
                self.stdout.write(f"Icon path: {card.icon.name}")
                self.stdout.write(f"Icon URL: {card.icon.url}")
                self.stdout.write('-' * 80)

        # Check Leaders
        self.stdout.write(self.style.WARNING('\n=== LEADERS ==='))
        for leader in Leader.objects.all():
            if leader.photo:
                self.stdout.write(f"ID: {leader.id}, Name: {leader.name_ru}")
                self.stdout.write(f"Photo path: {leader.photo.name}")
                self.stdout.write(f"Photo URL: {leader.photo.url}")
                self.stdout.write('-' * 80)

        # Check News
        self.stdout.write(self.style.WARNING('\n=== NEWS ==='))
        for news in News.objects.all():
            if news.image:
                self.stdout.write(f"ID: {news.id}, Title: {news.title_ru[:50]}")
                self.stdout.write(f"Image path: {news.image.name}")
                self.stdout.write(f"Image URL: {news.image.url}")
                self.stdout.write('-' * 80)

        # Check Partners
        self.stdout.write(self.style.WARNING('\n=== PARTNERS ==='))
        for partner in Partner.objects.all():
            if partner.logo:
                self.stdout.write(f"ID: {partner.id}, Name: {partner.name_ru}")
                self.stdout.write(f"Logo path: {partner.logo.name}")
                self.stdout.write(f"Logo URL: {partner.logo.url}")
                self.stdout.write('-' * 80)

        # Now check what's actually in S3
        self.stdout.write(self.style.WARNING('\n=== FILES IN S3 BUCKET ==='))
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

        try:
            response = s3.list_objects_v2(Bucket=BUCKET_NAME)
            if 'Contents' in response:
                for obj in response['Contents']:
                    self.stdout.write(f"S3 File: {obj['Key']}")
                    self.stdout.write(f"Size: {obj['Size']} bytes")
                    self.stdout.write(f"Public URL: https://{BUCKET_NAME}.s3.amazonaws.com/{obj['Key']}")
                    self.stdout.write('-' * 80)
            else:
                self.stdout.write(self.style.WARNING('No files in S3 bucket'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error accessing S3: {str(e)}'))
