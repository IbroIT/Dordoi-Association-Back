from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Gallery, Photos

# Inline для добавления галерей к категории
class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1  # 1 пустая форма для добавления галереи
    fields = ['title_ru', 'title_en', 'title_kg']

# Inline для добавления фото к галерее
class PhotosInline(admin.TabularInline):
    model = Photos
    extra = 3  # 3 пустые формы для добавления фото
    fields = ['image']

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    inlines = [GalleryInline]  # Здесь можно добавлять галереи к категории
    list_display = ['name_ru', 'name_en', 'name_kg']

@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    inlines = [PhotosInline]
    list_display = ['title_ru', 'category', 'photo_count']
    list_filter = ['category']
    search_fields = ['title_ru', 'category__name_ru']
    
    def photo_count(self, obj):
        return obj.photos.count()
    photo_count.short_description = "Количество фото"
    
