from unfold.admin import ModelAdmin
from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Category, News, Publication, PublicationCategory


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(PublicationCategory)
class PublicationCategoryAdmin(ModelAdmin):
    list_display = ["id", "title_ru", "title_en", "title_kg"]
    search_fields = ["title_ru", "title_en", "title_kg"]


@admin.register(News)
class NewsAdmin(ImageCroppingMixin, ModelAdmin):
    list_display = ["id", "get_title", "category", "is_recommended", "published_at", "created_at"]
    list_filter = ["category", "is_recommended", "published_at", "is_banner"]
    search_fields = ["title_ru", "title_en", "title_kg", "short_description_ru", "short_description_en", "short_description_kg"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Основная информация", {
            "fields": ("is_banner", "category", "is_recommended")
        }),
        ("Заголовок", {
            "fields": ("title_ru", "title_en", "title_kg")
        }),
        ("Краткое описание", {
            "fields": ("short_description_ru", "short_description_en", "short_description_kg")
        }),
        ("Полное описание", {
            "fields": ("description_ru", "description_en", "description_kg"),
            "classes": ("collapse",)
        }),
        ("Изображение", {
            "fields": ("image", "cropping")
        }),
        ("Даты", {
            "fields": ("published_at", "created_at", "updated_at")
        }),
    )

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'image_cropping/cropping.js',
            'presscentre/cropping_admin.js',
        )
        css = {
            'all': ('image_cropping/cropping.css',)
        }

    def get_title(self, obj):
        return obj.get_title()
    get_title.short_description = "Заголовок"


@admin.register(Publication)
class PublicationAdmin(ModelAdmin):
    list_display = ["id", "get_title_ru", "author", "published_at", "category"]
    list_filter = ["published_at", "category"]
    search_fields = ["title_ru", "title_en", "title_kg", "author"]

    fieldsets = (
        ("Категория", {"fields": ("category",)}),
        ("Заголовок", {"fields": ("title_ru", "title_en", "title_kg")}),
        (
            "Краткое описание",
            {
                "fields": (
                    "short_description_ru",
                    "short_description_en",
                    "short_description_kg",
                )
            },
        ),
        (
            "Полное описание",
            {
                "fields": ("description_ru", "description_en", "description_kg"),
                "classes": ("collapse",),
            },
        ),
        ("Автор и файл", {"fields": ("author", "pdf_file")}),
        ("Даты", {"fields": ("published_at",)}),
    )

    def get_title_ru(self, obj):
        return obj.title_ru

    get_title_ru.short_description = "Заголовок (RU)"
