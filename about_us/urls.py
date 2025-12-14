from rest_framework.routers import DefaultRouter
from .views import FactCardViewSet, BannerFact,HistoryListView
from django.urls import path, include
from . import views

app_name = "about_us"

router = DefaultRouter()
router.register(r"facts", FactCardViewSet, basename="fact-card")

urlpatterns = [
    path('', include(router.urls)),
    path('fact_banners/', BannerFact.as_view(), name='banner-facts'),
    path('leaders/', views.LeaderListView.as_view(), name='leader-list'),
    path('leaders/<int:id>/', views.LeaderDetailView.as_view(), name='leader-detail'),
    path('history/',HistoryListView.as_view(),name='history-list')
]
