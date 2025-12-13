from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import FactCard ,Leader


@admin.register(FactCard)
class FactCardAdmin(ModelAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('is_banner',)
        }),
        ('Фото баннера', {
            'fields': ('photo',),
            'classes': ('collapse',),
        }),
        ('Иконка', {
            'fields': ('icon',)
        }),
        ('Заголовок', {
            'fields': ('title_en', 'title_ru', 'title_kg')
        }),
        ('Описание', {
            'fields': ('description_en', 'description_ru', 'description_kg')
        }),
        ('Деталь', {
            'fields': ('detail_en', 'detail_ru', 'detail_kg')
        }),
    )
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj and not obj.is_banner:
            # Если is_banner=False, скрываем поле photo
            fieldsets = [fs 
                         for fs in fieldsets 
                         if fs[0] != 'Фото баннера']
        return fieldsets




@admin.register(Leader)
class LeaderAdmin(ModelAdmin):
    pass
