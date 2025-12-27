from django.urls import path, include
from . import views

urlpatterns = [
	path("contacts/", views.ContactListView.as_view(), name="contacts")
]

