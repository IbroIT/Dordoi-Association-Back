#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.db.migrations.recorder import MigrationRecorder

# Добавляем записи о миграциях вручную
recorder = MigrationRecorder(connection=django.db.connection)
recorder.record_applied('presscentre', '0011_newsphoto')
recorder.record_applied('presscentre', '0012_publication_gallery_alter_news_image')

print("Migrations marked as applied successfully!")
