from django.db import models

# Create your models here.
class Category(models.Model):
    name_en = models.CharField(max_length=255, verbose_name="Категория Name(en)")
    name_kg = models.CharField(max_length=255, verbose_name="Категория (kg)")
    name_ru = models.CharField(max_length=255, verbose_name="Категория (ru)")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name_ru"]

    def __str__(self):
        return self.name_ru
    def get_name(self, language="ru"):
        return getattr(self, f"name_{language}", self.name_ru)

class Gallery(models.Model):   
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="galleries", verbose_name="Категория")
    title_en = models.CharField(max_length=255, blank=True, verbose_name="Заголовок (en)")
    title_kg = models.CharField(max_length=255, blank=True, verbose_name="Заголовок (kg)")
    title_ru = models.CharField(max_length=255, blank=True, verbose_name="Заголовок (ru)")

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"
        ordering = ["id"]

    def __str__(self):
        return self.get_title() or f"Gallery {self.id}"
    
    def get_title(self, language="ru"):
        return getattr(self, f"title_{language}", self.title_ru) or f"Gallery {self.id}"

class Photos(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="photos", verbose_name="Галерея")
    image = models.ImageField(upload_to="gallery/photos/", verbose_name="Фото")

    class Meta:
        verbose_name = "Изображение галереи"
        verbose_name_plural = "Изображения галереи"
        ordering = ["id"]

    def __str__(self):
        return f"Image {self.id} in gallery {self.gallery}"