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