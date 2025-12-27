from django.urls import path, include
from . import views

urlpatterns = [
    path("banners/", views.BannerListView.as_view(), name="banner-list"),
]

