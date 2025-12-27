from django.http import JsonResponse
from django.db import connection
from django.conf import settings
import os


def health_check(request):
    """
    Health check endpoint for Heroku
    """
    # Check database connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        db_status = "ok"
    except Exception as e:
        db_status = f"error: {str(e)}"

    # Get basic info
    data = {
        "status": "ok" if db_status == "ok" else "error",
        "database": db_status,
        "environment": os.environ.get('ENVIRONMENT', 'development'),
        "debug": settings.DEBUG,
        "version": "1.0.0"
    }

    status_code = 200 if data["status"] == "ok" else 500
    return JsonResponse(data, status=status_code)


def serve_media(request, path):
    """
    Proxy media files from S3 to avoid CORS issues
    """
    if not settings.AWS_ACCESS_KEY_ID:
        # Fallback to local media serving in development
        from django.views.static import serve
        return serve(request, path, document_root=settings.MEDIA_ROOT)

    # Build S3 URL
    s3_url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.{settings.AWS_S3_REGION_NAME}.amazonaws.com/media/{path}"

    try:
        # Fetch file from S3
        import requests
        response = requests.get(s3_url, stream=True, timeout=10)

        if response.status_code == 200:
            # Create Django response with S3 content
            from django.http import HttpResponse
            django_response = HttpResponse(
                response.content,
                content_type=response.headers.get('content-type', 'application/octet-stream')
            )

            # Copy relevant headers
            for header in ['content-type', 'content-length', 'etag', 'last-modified']:
                if header in response.headers:
                    django_response[header] = response.headers[header]

            # Add CORS headers
            django_response['Access-Control-Allow-Origin'] = '*'
            django_response['Access-Control-Allow-Methods'] = 'GET, HEAD, OPTIONS'
            django_response['Access-Control-Allow-Headers'] = '*'

            return django_response
        else:
            from django.http import Http404
            raise Http404("File not found")

    except requests.RequestException:
        from django.http import Http404
        raise Http404("File not accessible")