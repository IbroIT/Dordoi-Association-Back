from django.contrib import admin
from .models import Category, Gallery
from unfold.admin import ModelAdmin


@admin.register(Category)
class CustomAdminClass(ModelAdmin):
    pass
@admin.register(Gallery)
class CustomAdminClass(ModelAdmin):
    pass
