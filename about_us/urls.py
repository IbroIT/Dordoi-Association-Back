from rest_framework.routers import DefaultRouter
from .views import FactCardViewSet, FactDetailViewSet

app_name = "about_us"

router = DefaultRouter()
router.register(r"facts", FactCardViewSet, basename="fact-card")
router.register(r"details", FactDetailViewSet, basename="fact-detail")

urlpatterns = router.urls
