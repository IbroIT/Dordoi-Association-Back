from django.shortcuts import render
from .models import Banner
from .serializers import BannerSerializer
from rest_framework import generics

# Create your views here.
class LanguageContextMixin:
    """Миксин для добавления языка в context сериализатора"""
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class BannerListView(LanguageContextMixin, generics.ListAPIView):
    """View для получения списка всех баннеров"""
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer