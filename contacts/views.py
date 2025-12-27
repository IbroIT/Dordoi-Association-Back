from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import generics

# Create your views here.
class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        language = self.request.query_params.get('language', 'ru')
        context['language'] = language
        return context