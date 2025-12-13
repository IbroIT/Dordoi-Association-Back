from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, NewsViewSet, BannerNewsViewSet
from django.urls import path, include

app_name = "presscentre"

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"news", NewsViewSet, basename="news")

urlpatterns = [
            path('', include(router.urls)),
            path("news-banners/", BannerNewsViewSet.as_view(), name="banner-news"),
]
