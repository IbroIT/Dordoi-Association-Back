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
    image = models.ImageField(upload_to="gallery/", verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="images", verbose_name="Категория")

    class Meta:
        verbose_name = "Изображение галереи"
        verbose_name_plural = "Изображения галереи"
        ordering = ["id"]

    def __str__(self):
        return f"Image {self.id} in category {self.category.get_name()}"