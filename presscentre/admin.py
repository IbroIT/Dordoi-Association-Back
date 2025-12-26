from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Category, News, Publication, NewsPhoto


@admin.register(Publication)
class PublicationAdmin(ModelAdmin):
    list_display = ["id", "get_title_ru", "link", "created_at"]
    search_fields = ["title_ru", "title_en", "title_kg", "link"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Заголовок", {"fields": ("title_ru", "title_en", "title_kg")}),
        ("Ссылка", {"fields": ("link",)}),
        ("Даты", {"fields": ("created_at", "updated_at")}),
    )

    def get_title_ru(self, obj):
        return obj.title_ru

    get_title_ru.short_description = "Заголовок (RU)"
