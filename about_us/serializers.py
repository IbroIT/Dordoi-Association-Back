from rest_framework import serializers
from .models import FactCard, Leader, History, Structure


class LeaderSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()

    class Meta:
        model = Leader
        fields = ["id", "photo", "name", "position", "bio", "achievements", "education"]

    def get_name(self, obj):
        return obj.get_name(self.context.get("language", "ru"))

    def get_position(self, obj):
        return obj.get_position(self.context.get("language", "ru"))

    def get_bio(self, obj):
        return obj.get_bio(self.context.get("language", "ru"))

    def get_achievements(self, obj):
        return obj.get_achievements(self.context.get("language", "ru"))

    def get_education(self, obj):
        return obj.get_education(self.context.get("language", "ru"))


class LocalizationSerializerMixin:
    """Миксин для локализации сериализаторов"""

    def _get_language(self):
        lang = self.context.get("language")
        if lang:
            return lang
        request = self.context.get("request")
        if request:
            return (
                request.GET.get("lang")
                or getattr(request, "LANGUAGE_CODE", None)
                or "ru"
            )
        return "ru"


class FactCardSerializer(LocalizationSerializerMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    details = serializers.SerializerMethodField()

    class Meta:
        model = FactCard
        fields = ["id", "icon", "title", "description", "details", "is_banner"]
        read_only_fields = ["id"]

    def get_title(self, obj):
        language = self._get_language()
        return obj.get_title(language=language)

    def get_description(self, obj):
        language = self._get_language()
        field_name = f"description_{language}"
        value = getattr(obj, field_name, None)

        if value and value.strip():
            return value.strip()

        if language != "ru" and obj.description_ru and obj.description_ru.strip():
            return obj.description_ru.strip()

        if language != "en" and obj.description_en and obj.description_en.strip():
            return obj.description_en.strip()

        return ""

    def get_details(self, obj):
        language = self._get_language()
        return obj.get_detail(language=language)


class HistorySerializer(LocalizationSerializerMixin, serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = History
        fields = ["id", "description", "image", "order"]
        read_only_fields = ["id"]

    def get_description(self, obj):
        language = self._get_language()
        field_name = f"description_{language}"
        return getattr(obj, field_name, obj.description_ru)


class StructureSerializer(LocalizationSerializerMixin, serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()

    class Meta:
        model = Structure
        fields = [
            "id",
            "slug",
            "logo",
            "name",
            "short_description",
            "description",
            "founded_year",
            "achievements",
            "address",
            "email",
            "phone",
            "website",
            "order",
        ]
        read_only_fields = ["id"]
        lookup_field = "slug"

    def get_name(self, obj):
        return obj.get_name(language=self._get_language())

    def get_short_description(self, obj):
        return obj.get_short_description(language=self._get_language())

    def get_description(self, obj):
        return obj.get_description(language=self._get_language())

    def get_achievements(self, obj):
        return obj.get_achievements(language=self._get_language())
