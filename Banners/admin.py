from django.contrib import admin
from .models import Banner
from unfold.admin import ModelAdmin


@admin.register(Banner)
class CategoryAdmin(ModelAdmin):
    pass