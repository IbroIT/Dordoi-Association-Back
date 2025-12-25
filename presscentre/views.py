from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Category, News, Publication, PublicationCategory
from .serializers import (
    PublicationSerializer,
)


class LocalizationMixin:

    def get_serializer_context(self):
        context = super().get_serializer_context()
        language = (
            self.request.GET.get("lang")
            or getattr(self.request, "LANGUAGE_CODE", None)
            or "ru"
        )
        context.update({"language": language})
        return context


class PublicationViewSet(LocalizationMixin, ReadOnlyModelViewSet):

    queryset = Publication.objects.all().order_by("-created_at")
    serializer_class = PublicationSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "title_en",
        "title_ru",
        "title_kg",
        "link",
    ]
    ordering_fields = ["created_at", "title_ru"]
