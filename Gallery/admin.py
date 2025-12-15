from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Gallery, Photos

# Inline для добавления фото к галерее
class PhotosInline(admin.TabularInline):
    model = Photos
    extra = 3  # 3 пустые формы для добавления фото
    fields = ['image']

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name_ru', 'name_en', 'name_kg']

@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    inlines = [PhotosInline]
    list_display = ['id', 'category']
    list_filter = ['category']
    search_fields = ['category__name_ru']
    