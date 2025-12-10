#!/bin/bash
# Script to test Heroku deployment locally

echo "Testing Heroku deployment locally..."

# Check if gunicorn is installed
if ! command -v gunicorn &> /dev/null; then
    echo "❌ Gunicorn not found. Install with: pip install gunicorn"
    exit 1
fi

# Check if required packages are installed
python -c "import whitenoise, dj_database_url, psycopg2" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Missing required packages. Install with: pip install -r requirements.txt"
    exit 1
fi

# Test Django settings
echo "Testing Django settings..."
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
import django
django.setup()
from django.conf import settings
print(f'✅ DEBUG: {settings.DEBUG}')
print(f'✅ SECRET_KEY: {\"Set\" if settings.SECRET_KEY else \"Not set\"}')
print(f'✅ ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}')
print(f'✅ DATABASES: {list(settings.DATABASES.keys())}')
print(f'✅ INSTALLED_APPS count: {len(settings.INSTALLED_APPS)}')
"

# Test gunicorn startup
echo "Testing Gunicorn startup..."
timeout 5 gunicorn core.wsgi --bind 0.0.0.0:8001 --workers 1 --log-level info &
GUNICORN_PID=$!

sleep 3

if kill -0 $GUNICORN_PID 2>/dev/null; then
    echo "✅ Gunicorn started successfully"
    kill $GUNICORN_PID
else
    echo "❌ Gunicorn failed to start"
    exit 1
fi

echo "🎉 All tests passed! Ready for Heroku deployment."