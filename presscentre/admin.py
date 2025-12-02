from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Category, News


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(ModelAdmin):
    pass
