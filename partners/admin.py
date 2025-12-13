from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Partner


@admin.register(Partner)
class PartnerAdmin(ModelAdmin):
    pass

