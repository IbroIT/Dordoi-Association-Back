from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Gallery

# Просто добавляем возможность загружать несколько фото к категории
class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 3  # 3 пустые формы для добавления фото

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    inlines = [GalleryInline]  # Здесь можно добавлять фото к категории
    list_display = ['name', 'image_count']
    
    def image_count(self, obj):
        return obj.images.count()

@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    list_display = ['id', 'category', 'image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 50px;" />'
        return "Нет изображения"
    image_preview.allow_tags = True