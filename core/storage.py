from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings
from datetime import timedelta


class PublicMediaStorage(S3Boto3Storage):
    """
    Custom S3 storage backend that generates signed URLs for secure access
    """
    location = 'media'
    file_overwrite = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Use signed URLs instead of public ACL
        self.querystring_auth = True
        self.default_acl = None  # Don't set public ACL

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
        Generate signed URL for the file
        """
        if expire is None:
            expire = 3600 * 24 * 7  # 7 days

        return super().url(name, parameters, expire)