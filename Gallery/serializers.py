from rest_framework import serializers
from .models import Category, Gallery, Photos


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_en', 'name_kg', 'name_ru']


class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ['id', 'image']


class GallerySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    photos = PhotosSerializer(many=True, read_only=True)
    
    class Meta:
        model = Gallery
        fields = ['id', 'category', 'title_en', 'title_kg', 'title_ru', 'photos']


class GalleryListByCategorySerializer(serializers.ModelSerializer):
    photos = PhotosSerializer(many=True, read_only=True)
    
    class Meta:
        model = Gallery
        fields = ['id', 'photos']
