from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import FactCard, FactDetail,Leader
from .serializers import FactCardSerializer, FactDetailSerializer,LeaderSerializer
from rest_framework import generics


class LeaderListView(generics.ListAPIView):
    """
    View для получения списка всех лидеров
    Поддерживает параметр lang для выбора языка (ru, en, kg)
    """
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context

class LeaderDetailView(generics.RetrieveAPIView):
    """
    View для получения детальной информации о лидере
    Поддерживает параметр lang для выбора языка (ru, en, kg)
    """
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer
    lookup_field = 'id'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context

class LocalizationMixin:
    """Миксин для передачи языка в контекст сериализатора"""

    def get_serializer_context(self):
        context = super().get_serializer_context()
        language = (
            self.request.GET.get("lang")
            or getattr(self.request, "LANGUAGE_CODE", None)
            or "ru"
        )
        context.update({"language": language})
        return context


class FactCardViewSet(LocalizationMixin, ReadOnlyModelViewSet):
    """
    ViewSet для получения факт-карт с деталями.

    Query Parameters:
    - lang: ru, en, kg (язык ответа)
    - ordering: id, title_ru, title_en, title_kg
    - search: поиск по названию и описанию
    """

    queryset = FactCard.objects.prefetch_related("details").all().order_by("id")
    serializer_class = FactCardSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "title_en",
        "title_ru",
        "title_kg",
        "description_en",
        "description_ru",
        "description_kg",
    ]
    ordering_fields = ["id", "title_ru", "title_en", "title_kg"]


class FactDetailViewSet(LocalizationMixin, ReadOnlyModelViewSet):
    """
    ViewSet для получения деталей фактов.

    Query Parameters:
    - lang: ru, en, kg (язык ответа)
    - card: ID факт-карты (фильтр)
    """

    queryset = FactDetail.objects.select_related("card").all().order_by("id")
    serializer_class = FactDetailSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["card"]
    ordering_fields = ["id", "card"]
