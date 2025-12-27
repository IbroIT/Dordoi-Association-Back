from rest_framework.routers import DefaultRouter
from .views import (
    PublicationViewSet,
    CategoryViewSet,
    NewsViewSet,
)
from django.urls import path, include

app_name = "presscentre"

router = DefaultRouter()
router.register(r"publications", PublicationViewSet, basename="publication")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"news", NewsViewSet, basename="news")

urlpatterns = [
    path("", include(router.urls)),
    path("news-banners/", NewsViewSet.as_view({'get': 'banners'}), name="news-banners"),
]
