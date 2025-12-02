from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import FactCard, FactDetail, Leader


@admin.register(FactCard)
class FactCardAdmin(ModelAdmin):
    pass


@admin.register(FactDetail)
class FactDetailAdmin(ModelAdmin):
    pass


@admin.register(Leader)
class LeaderAdmin(ModelAdmin):
    pass
