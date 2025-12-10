from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    """
    Custom S3 storage backend that stores files with public URLs
    """
    location = 'media'
    file_overwrite = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable signed URLs for direct public access
        self.querystring_auth = False
        self.default_acl = None

    def _save(self, name, content):
        """
        Override _save to ensure proper storage
        """
        self.object_parameters = {
            'CacheControl': 'max-age=86400',
        }
        return super()._save(name, content)