from rest_framework.routers import DefaultRouter
from .views import FactCardViewSet, FactDetailViewSet
from django.urls import path, include
from . import views

app_name = "about_us"

router = DefaultRouter()
router.register(r"facts", FactCardViewSet, basename="fact-card")
router.register(r"details", FactDetailViewSet, basename="fact-detail")

urlpatterns = [
    path('', include(router.urls)),
    path('leaders/', views.LeaderListView.as_view(), name='leader-list'),
    path('leaders/<int:id>/', views.LeaderDetailView.as_view(), name='leader-detail'),
]
