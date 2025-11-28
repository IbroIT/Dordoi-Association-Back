# urls.py
from django.urls import path
from . import views

app_name = 'partners'

urlpatterns = [
    path('partners/', views.PartnerListView.as_view(), name='partner-list'),
    path('partners/<int:id>/', views.PartnerDetailView.as_view(), name='partner-detail'),
]