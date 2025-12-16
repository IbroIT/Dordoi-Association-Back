from django.contrib import admin
from .models import Banner
from unfold.admin import ModelAdmin


@admin.register(Banner)
class CategoryAdmin(ModelAdmin):
    list_display = ["order", "title_ru", "link_url"]
    list_display_links = ["title_ru"]
    list_editable = ["order"]
    ordering = ["order"]