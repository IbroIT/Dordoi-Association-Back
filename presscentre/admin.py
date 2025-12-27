from django.contrib import admin
from .models import Category, News, NewsPhoto


class NewsPhotoInline(admin.TabularInline):
    model = NewsPhoto
    extra = 0
    fields = ['image', 'alt_text_ru', 'alt_text_en', 'alt_text_kg', 'order']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsPhotoInline]


# Register your models here.
admin.site.register(Category)
admin.site.register(NewsPhoto)