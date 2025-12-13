from django.db import models

# Create your models here.
class Banner(models.Model):
    image = models.ImageField(upload_to="partners/banners/", verbose_name="баннер")
    title_en = models.CharField(max_length=255, verbose_name="Главный текст баннера (en)")
    title_kg = models.CharField(max_length=255, verbose_name="Главный текст баннера (kg)")
    title_ru = models.CharField(max_length=255, verbose_name="Главный текст баннерали (ru)")

    idea_en = models.CharField(max_length=255, verbose_name="Идея баннера (en)")
    idea_kg = models.CharField(max_length=255, verbose_name="Идея  баннера (kg)")
    idea_ru = models.CharField(max_length=255, verbose_name="Идея  баннера (ru)")

    desctip_en = models.CharField(max_length=255, verbose_name="Описание баннера (en)")
    desctip_kg = models.CharField(max_length=255, verbose_name="Описание баннера (kg)")
    desctip_ru = models.CharField(max_length=255, verbose_name="Описание баннера (ru)")

    link_url = models.URLField(max_length=500, verbose_name="Ссылка для кнопки(необязательно)", blank=True, null=True)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

    def __str__(self):
        return self.title_ru
    
    def get_title(self, language="ru"):
        return getattr(self, f"title_{language}", self.title_ru)
    
    def get_idea(self, language="ru"):
        return getattr(self, f"idea_{language}", self.idea_ru)

    def get_desctip(self, language="ru"):
        return getattr(self, f"desctip_{language}", self.desctip_ru)