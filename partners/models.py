from django.db import models

# Create your models here.
class Partner(models.Model):
    logo = models.ImageField(upload_to="partners/logos/", verbose_name="Логотип")
    name_en = models.CharField(max_length=255, verbose_name="Название (EN)")
    name_ru = models.CharField(max_length=255, verbose_name="Название (RU)")
    name_kg = models.CharField(max_length=255, verbose_name="Название (KG)")
    description_en = models.TextField(verbose_name="Описание (EN)")
    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_kg = models.TextField(verbose_name="Описание (KG)")
    otrasl_kg = models.CharField(max_length=255, verbose_name="Отрасль (KG)")
    otrasl_ru = models.CharField(max_length=255, verbose_name="Отрасль (RU)")
    otrasl_en = models.CharField(max_length=255, verbose_name="Отрасль (EN)")
    founded_year = models.PositiveIntegerField(verbose_name="Год основания")
    shtab_kvartira_ru = models.CharField(max_length=255, verbose_name="Штаб-квартира(RU)")
    shtab_kvartira_en = models.CharField(max_length=255, verbose_name="Штаб-квартира(EN)")
    shtab_kvartira_kg = models.CharField(max_length=255, verbose_name="Штаб-квартира(KG)")
    about_company_en = models.TextField(verbose_name="О компании (EN)")
    about_company_ru = models.TextField(verbose_name="О компании (RU)")
    about_company_kg = models.TextField(verbose_name="О компании (KG)")
    ulugi_en = models.JSONField(verbose_name="Услуги (EN)")
    ulugi_ru = models.JSONField(verbose_name="Услуги (RU)")
    ulugi_kg = models.JSONField(verbose_name="Услуги (KG)")
    achievements_en = models.JSONField(verbose_name="Достижения (EN)")
    achievements_ru = models.JSONField(verbose_name="Достижения (RU)")
    achievements_kg = models.JSONField(verbose_name="Достижения (KG)")
    about_corporation_en = models.TextField(verbose_name="О сотрдуничестве (EN)")
    about_corporation_ru = models.TextField(verbose_name="О сотрдуничестве (RU)")
    about_corporation_kg = models.TextField(verbose_name="О сотрдуничестве (KG)")
    website = models.URLField(verbose_name="Вебсайт")
    partnership_status_ru = models.CharField(max_length=50, verbose_name="Статус партнерства(RU)")
    partnership_status_en = models.CharField(max_length=50, verbose_name="Статус партнерства(EN)")
    partnership_status_kg = models.CharField(max_length=50, verbose_name="Статус партнерства(KG)")
    features_en = models.JSONField(verbose_name="Преимущества сотрудничества(EN)")
    features_ru = models.JSONField(verbose_name="Преимущества сотрудничества(RU)")
    features_kg = models.JSONField(verbose_name="Преимущества сотрудничества(KG)")


    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"
        ordering = ["id"]   
    def __str__(self):
        return self.get_name()
    def get_name(self, language="ru"):
        return getattr(self, f"name_{language}", self.name_ru)
    def get_description(self, language="ru"):
        return getattr(self, f"description_{language}", self.description_ru)
    def get_otrasl(self, language="ru"):
        return getattr(self, f"otrasl_{language}", self.otrasl_ru)
    def get_shtab_kvartira(self, language="ru"):
        return getattr(self, f"shtab_kvartira_{language}", self.shtab_kvartira_ru)
    def get_about_company(self, language="ru"):
        return getattr(self, f"about_company_{language}", self.about_company_ru)
    def get_about_corporation(self, language="ru"):
        return getattr(self, f"about_corporation_{language}", self.about_corporation_ru)    
    def get_partnership_status(self, language="ru"):
        return getattr(self, f"partnership_status_{language}", self.partnership_status_ru)
    def get_features(self, language="ru"):
        return getattr(self, f"features_{language}", self.features_ru)
    def get_ulugi(self, language="ru"):
        return getattr(self, f"ulugi_{language}", self.ulugi_ru)
    def get_achievements(self, language="ru"):
        return getattr(self, f"achievements_{language}", self.achievements_ru)  