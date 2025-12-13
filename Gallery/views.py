from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Category, Gallery
from .serializers import (
    CategorySerializer, 
    GallerySerializer, 
    GalleryListByCategorySerializer
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    
    @action(detail=False, methods=['get'], url_path='by-category/(?P<category_id>[^/.]+)')
    def by_category(self, request, category_id=None):
        """Получить все изображения по категории"""
        category = get_object_or_404(Category, id=category_id)
        galleries = Gallery.objects.filter(category=category)
        serializer = GalleryListByCategorySerializer(galleries, many=True)
        return Response({
            'category': CategorySerializer(category).data,
            'images': serializer.data
        })
