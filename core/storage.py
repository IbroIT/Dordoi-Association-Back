from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    """
    Custom S3 storage backend that ensures all uploaded files are publicly accessible
    """
    location = 'media'
    file_overwrite = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure ACL is set to public-read
        if not hasattr(self, 'default_acl'):
            self.default_acl = 'public-read'

    def _save(self, name, content):
        """
        Override _save to ensure ACL is set correctly
        """
        # Set ACL explicitly for each file
        self.object_parameters = {
            'ACL': 'public-read',
            'CacheControl': 'max-age=86400',
        }
        return super()._save(name, content)