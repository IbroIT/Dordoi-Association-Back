from rest_framework.routers import DefaultRouter
from .views import (
    PublicationViewSet,
)
from django.urls import path, include

app_name = "presscentre"

router = DefaultRouter()
router.register(r"publications", PublicationViewSet, basename="publication")

urlpatterns = [
    path("", include(router.urls)),
]
