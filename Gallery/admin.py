from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Gallery

# Просто добавляем возможность загружать несколько фото к категории
class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 3  # 3 пустые формы для добавления фото

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass

@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    inlines = [GalleryInline]  # Здесь можно добавлять фото к категории
    list_display = ['name', 'image_count']
    