from rest_framework import serializers
from .models import FactCard, FactDetail


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


class FactDetailSerializer(LocalizationSerializerMixin, serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()

    class Meta:
        model = FactDetail
        fields = ["id", "detail"]
        read_only_fields = ["id"]

    def get_detail(self, obj):
        language = self._get_language()
        return obj.get_detail(language=language)


class FactCardSerializer(LocalizationSerializerMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    details = FactDetailSerializer(many=True, read_only=True)

    class Meta:
        model = FactCard
        fields = ["id", "icon", "title", "description", "details"]
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
