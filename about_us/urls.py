from rest_framework.routers import DefaultRouter
from .views import FactCardViewSet, BannerFact, HistoryViewSet, StructureViewSet
from django.urls import path, include
from . import views

app_name = "about_us"

router = DefaultRouter()
router.register(r"facts", FactCardViewSet, basename="fact-card")
router.register(r"history", HistoryViewSet, basename="history")
router.register(r"structure", StructureViewSet, basename="structure")


urlpatterns = [
    path("", include(router.urls)),
    path("fact_banners/", BannerFact.as_view(), name="banner-facts"),
    path("leaders/", views.LeaderListView.as_view(), name="leader-list"),
    path("leaders/<int:id>/", views.LeaderDetailView.as_view(), name="leader-detail"),
]
