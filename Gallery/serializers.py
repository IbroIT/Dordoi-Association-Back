from rest_framework import serializers
from .models import Category, Gallery


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_en', 'name_kg', 'name_ru']


class GallerySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Gallery
        fields = ['id', 'image', 'category']


class GalleryListByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'image']
