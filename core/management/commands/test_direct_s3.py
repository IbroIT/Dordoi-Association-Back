from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from storages.backends.s3boto3 import S3Boto3Storage
import os


class Command(BaseCommand):
    help = 'Test S3 file upload directly with S3Boto3Storage'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== Testing Direct S3Boto3Storage Upload ==='))
        
        try:
            # Create S3 storage instance directly
            storage = S3Boto3Storage()
            
            self.stdout.write(f'\nStorage class: {storage.__class__.__name__}')
            self.stdout.write(f'Bucket: {storage.bucket_name}')
            
            # Create a test file
            test_content = b'This is a direct S3 test file'
            test_filename = 'test_uploads/direct_test.txt'
            
            self.stdout.write(f'\nAttempting to upload: {test_filename}')
            
            # Save file
            path = storage.save(test_filename, ContentFile(test_content))
            
            self.stdout.write(self.style.SUCCESS(f'✓ File saved to: {path}'))
            
            # Get URL
            url = storage.url(path)
            self.stdout.write(f'URL: {url}')
            
            # Check if file exists
            exists = storage.exists(path)
            self.stdout.write(f'File exists in storage: {exists}')
            
            # Get file size
            size = storage.size(path)
            self.stdout.write(f'File size: {size} bytes')
            
            self.stdout.write(f'\n✓ SUCCESS! Test file uploaded successfully!')
            self.stdout.write(f'\nTry accessing this URL in browser:')
            self.stdout.write(f'{url}')
            
            # Clean up
            self.stdout.write(f'\nDeleting test file...')
            storage.delete(path)
            self.stdout.write(self.style.SUCCESS('✓ Test file deleted'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'\n❌ Error: {str(e)}'))
            import traceback
            self.stdout.write(traceback.format_exc())
