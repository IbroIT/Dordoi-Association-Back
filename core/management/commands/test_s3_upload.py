from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os


class Command(BaseCommand):
    help = 'Test S3 file upload'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=== Testing S3 Upload ==='))
        
        # Check configuration
        self.stdout.write(f'\nStorage backend: {default_storage.__class__.__name__}')
        self.stdout.write(f'Bucket: {os.getenv("BUCKETEER_BUCKET_NAME")}')
        self.stdout.write(f'Region: {os.getenv("BUCKETEER_AWS_REGION")}')
        
        try:
            # Create a test file
            test_content = b'This is a test file for S3 upload'
            test_filename = 'test_uploads/test_file.txt'
            
            self.stdout.write(f'\nAttempting to upload: {test_filename}')
            
            # Save file
            path = default_storage.save(test_filename, ContentFile(test_content))
            
            self.stdout.write(self.style.SUCCESS(f'✓ File saved to: {path}'))
            
            # Get URL
            url = default_storage.url(path)
            self.stdout.write(f'URL: {url}')
            
            # Check if file exists
            exists = default_storage.exists(path)
            self.stdout.write(f'File exists in storage: {exists}')
            
            # Get file size
            size = default_storage.size(path)
            self.stdout.write(f'File size: {size} bytes')
            
            # Try to access the URL
            self.stdout.write(f'\n✓ SUCCESS! Test file uploaded successfully!')
            self.stdout.write(f'\nTry accessing this URL in browser:')
            self.stdout.write(f'{url}')
            
            # Clean up
            self.stdout.write(f'\nDeleting test file...')
            default_storage.delete(path)
            self.stdout.write(self.style.SUCCESS('✓ Test file deleted'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'\n❌ Error: {str(e)}'))
            import traceback
            self.stdout.write(traceback.format_exc())
