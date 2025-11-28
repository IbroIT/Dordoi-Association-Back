# serializers.py
from rest_framework import serializers
from .models import Partner

class PartnerSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    otrasl = serializers.SerializerMethodField()
    shtab_kvartira = serializers.SerializerMethodField()
    about_company = serializers.SerializerMethodField()
    about_corporation = serializers.SerializerMethodField()
    partnership_status = serializers.SerializerMethodField()
    ulugi = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = [
            'id',
            'logo',
            'name',
            'description',
            'otrasl',
            'founded_year',
            'shtab_kvartira',
            'about_company',
            'ulugi',
            'achievements',
            'about_corporation',
            'website',
            'partnership_status',
            'features'
        ]

    def get_name(self, obj):
        return obj.get_name(self.context.get("language", "ru"))

    def get_description(self, obj):
        return obj.get_description(self.context.get("language", "ru"))

    def get_otrasl(self, obj):
        return obj.get_otrasl(self.context.get("language", "ru"))

    def get_shtab_kvartira(self, obj):
        return obj.get_shtab_kvartira(self.context.get("language", "ru"))

    def get_about_company(self, obj):
        return obj.get_about_company(self.context.get("language", "ru"))

    def get_about_corporation(self, obj):
        return obj.get_about_corporation(self.context.get("language", "ru"))

    def get_partnership_status(self, obj):
        return obj.get_partnership_status(self.context.get("language", "ru"))

    def get_ulugi(self, obj):
        return obj.get_ulugi(self.context.get("language", "ru"))

    def get_achievements(self, obj):
        return obj.get_achievements(self.context.get("language", "ru"))

    def get_features(self, obj):
        return obj.get_features(self.context.get("language", "ru"))