from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    """
    Custom S3 storage backend that generates long-term signed URLs for public access
    """
    location = 'media'
    file_overwrite = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Use long-term signed URLs instead of public ACL
        self.querystring_auth = True
        self.default_acl = None

    def _save(self, name, content):
        """
        Override _save to ensure proper storage
        """
        self.object_parameters = {
            'CacheControl': 'max-age=86400',
        }
        return super()._save(name, content)

    def url(self, name, parameters=None, expire=None):
        """
        Generate long-term signed URL for the file (1 year)
        """
        if expire is None:
            expire = 3600 * 24 * 365  # 1 year

        return super().url(name, parameters, expire)