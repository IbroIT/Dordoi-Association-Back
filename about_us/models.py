from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class FactCard(models.Model):
    icon = models.ImageField(upload_to="fact_cards/", verbose_name="Иконка")
    
    title_en = models.CharField(max_length=255, verbose_name="Заголовок (EN)")
    title_ru = models.CharField(max_length=255, verbose_name="Заголовок (RU)")
    title_kg = models.CharField(max_length=255, verbose_name="Заголовок (KG)")

    description_en = models.TextField(verbose_name="Описание (EN)")
    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_kg = models.TextField(verbose_name="Описание (KG)")


    class Meta:
        verbose_name = "Факт-карта"
        verbose_name_plural = "Факт-карты"
        ordering = ["id"]

    def __str__(self):
        return self.get_title()

    def get_title(self, language="ru"):
        field_name = f"title_{language}"
        value = getattr(self, field_name, None)

        if value and value.strip():
            return value.strip()

        if language != "ru" and self.title_ru and self.title_ru.strip():
            return self.title_ru.strip()

        if language != "en" and self.title_en and self.title_en.strip():
            return self.title_en.strip()

        return f"FactCard #{self.id}"

    @property
    def title(self):
        return self.get_title(language="ru") or ""

    def clean(self):
        super().clean()
        if not any([self.title_ru, self.title_en, self.title_kg]):
            raise ValidationError("Необходимо заполнить хотя бы одно название")
        
class FactDetail(models.Model):
    card = models.ForeignKey(FactCard, on_delete=models.CASCADE, related_name="details", verbose_name="Факт-карта")
    
    detail_en = models.CharField(max_length=255, verbose_name="Деталь (EN)")
    detail_ru = models.CharField(max_length=255, verbose_name="Деталь (RU)")
    detail_kg = models.CharField(max_length=255, verbose_name="Деталь (KG)")
    
    class Meta:
        verbose_name = "Деталь факта"
        verbose_name_plural = "Детали фактов"
        ordering = ["id"]
        
    def __str__(self):
        return self.get_detail()
    
    def get_detail(self, language="ru"):
        field_name = f"detail_{language}"
        value = getattr(self, field_name, None)

        if value and value.strip():
            return value.strip()

        if language != "ru" and self.detail_ru and self.detail_ru.strip():
            return self.detail_ru.strip()

        if language != "en" and self.detail_en and self.detail_en.strip():
            return self.detail_en.strip()

        return f"FactDetail #{self.id}"
    

class Leader(models.Model):
    photo = models.ImageField(upload_to="leaders/", verbose_name="Фото")
    name_ru = models.CharField(max_length=255, verbose_name="ФИО (RU)")
    name_en = models.CharField(max_length=255, verbose_name="ФИО (EN)")
    name_kg = models.CharField(max_length=255, verbose_name="ФИО (KG)")
    position_ru = models.CharField(max_length=255, verbose_name="Должность (RU)")
    position_en = models.CharField(max_length=255, verbose_name="Должность (EN)")
    position_kg = models.CharField(max_length=255, verbose_name="Должность (KG)")  
    bio_kg = models.TextField(verbose_name="Биография (KG)")
    bio_ru = models.TextField(verbose_name="Биография (RU)")
    bio_en = models.TextField(verbose_name="Биография (EN)")
    achievements_kg = models.JSONField(verbose_name="Достижения (KG)")
    achievements_ru = models.JSONField(verbose_name="Достижения (RU)")
    achievements_en = models.JSONField(verbose_name="Достижения (EN)")
    education_kg = models.JSONField(verbose_name="Образование (KG)")
    education_ru = models.JSONField(verbose_name="Образование (RU)")
    education_en = models.JSONField(verbose_name="Образование (EN)")

    class Meta:
        verbose_name = "Лидер"
        verbose_name_plural = "Лидеры"
        ordering = ["id"]

    def __str__(self):
        return self.get_name()
    def get_name(self, language="ru"):
        return getattr(self, f"name_{language}", self.name_ru)
    def get_position(self, language="ru"):
        return getattr(self, f"position_{language}", self.position_ru)
    def get_bio(self, language="ru"):
        return getattr(self, f"bio_{language}", self.bio_ru)
    def get_achievements(self, language="ru"):
        return getattr(self, f"achievements_{language}", self.achievements_ru)
    def get_education(self, language="ru"):
        return getattr(self, f"education_{language}", self.education_ru)
    
