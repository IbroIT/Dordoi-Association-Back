from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    """
    Custom S3 storage backend that ensures all uploaded files are publicly accessible
    """
    location = 'media'
    file_overwrite = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Use public ACL for files
        self.default_acl = 'public-read'
        self.querystring_auth = False  # Disable signed URLs

    def _save(self, name, content):
        """
        Override _save to ensure ACL is set correctly
        """
        self.object_parameters = {
            'ACL': 'public-read',
            'CacheControl': 'max-age=86400',
        }
        return super()._save(name, content)