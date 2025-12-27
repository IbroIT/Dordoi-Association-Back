#!/usr/bin/env python
"""
Heroku release script to run migrations and collect static files
"""
import os
import sys
import django
from pathlib import Path

# Add the project directory to the path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Run migrations
from django.core.management import execute_from_command_line
print("Running migrations...")
execute_from_command_line(['manage.py', 'migrate', '--noinput'])

# Collect static files
print("Collecting static files...")
execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--clear'])

print("Release tasks completed!")