from django.core.management.base import BaseCommand
from django.conf import settings
import os


class Command(BaseCommand):
    help = 'Check AWS S3 configuration'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== Environment Variables ==='))
        self.stdout.write(f"BUCKETEER_AWS_ACCESS_KEY_ID: {os.getenv('BUCKETEER_AWS_ACCESS_KEY_ID', 'NOT SET')[:20]}...")
        self.stdout.write(f"BUCKETEER_AWS_SECRET_ACCESS_KEY: {os.getenv('BUCKETEER_AWS_SECRET_ACCESS_KEY', 'NOT SET')[:20]}...")
        self.stdout.write(f"BUCKETEER_BUCKET_NAME: {os.getenv('BUCKETEER_BUCKET_NAME', 'NOT SET')}")
        self.stdout.write(f"BUCKETEER_AWS_REGION: {os.getenv('BUCKETEER_AWS_REGION', 'NOT SET')}")
        
        self.stdout.write(self.style.WARNING('\n=== Django Settings ==='))
        self.stdout.write(f"AWS_ACCESS_KEY_ID: {settings.AWS_ACCESS_KEY_ID[:20] if settings.AWS_ACCESS_KEY_ID else 'NOT SET'}...")
        self.stdout.write(f"AWS_SECRET_ACCESS_KEY: {settings.AWS_SECRET_ACCESS_KEY[:20] if settings.AWS_SECRET_ACCESS_KEY else 'NOT SET'}...")
        self.stdout.write(f"AWS_STORAGE_BUCKET_NAME: {settings.AWS_STORAGE_BUCKET_NAME}")
        self.stdout.write(f"AWS_S3_REGION_NAME: {settings.AWS_S3_REGION_NAME}")
        self.stdout.write(f"AWS_S3_CUSTOM_DOMAIN: {settings.AWS_S3_CUSTOM_DOMAIN}")
        
        self.stdout.write(self.style.WARNING('\n=== Storage Configuration ==='))
        if hasattr(settings, 'STORAGES'):
            self.stdout.write(f"STORAGES (default backend): {settings.STORAGES.get('default', {}).get('BACKEND', 'NOT SET')}")
        elif hasattr(settings, 'DEFAULT_FILE_STORAGE'):
            self.stdout.write(f"DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}")
        self.stdout.write(f"MEDIA_URL: {settings.MEDIA_URL}")
        
        from django.core.files.storage import default_storage
        self.stdout.write(f"Actual storage backend: {default_storage.__class__.__name__}")
        self.stdout.write(f"Storage module: {default_storage.__class__.__module__}")
