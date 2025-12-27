from django.db import models

# Create your models here.
class Contact(models.Model):
    logo = models.ImageField(upload_to='contacts/logos/')
    name_en = models.CharField(max_length=255, verbose_name='название(en)')
    name_kg = models.CharField(max_length=255, verbose_name='название(kg)')
    name_ru = models.CharField(max_length=255, verbose_name='название(ru)')
    email = models.EmailField(verbose_name='электронная почта')
    phone = models.CharField(max_length=20, verbose_name='телефон')
    work_time_en = models.CharField(max_length=255, verbose_name='рабочее время(en)')
    work_time_kg = models.CharField(max_length=255, verbose_name='рабочее время(kg)')
    work_time_ru = models.CharField(max_length=255, verbose_name='рабочее время(ru)')
    tg_link = models.URLField(verbose_name='ссылка на телеграм' ,blank=True, null=True)
    wb_link = models.URLField(verbose_name='ссылка на whatsapp', blank=True, null=True)
    ins_link = models.URLField(verbose_name='ссылка на instagram', blank=True, null=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
    
    def __str__(self):
        return self.name_ru
    
    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)
    
    def get_work_time(self, language='ru'):
        return getattr(self, f'work_time_{language}', self.work_time_ru)