from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название сайта'
    )
    slogan = models.CharField(
        max_length=100,
        verbose_name='Слоган'
    )
    slogan_description = models.TextField(
        verbose_name='Описание слогана'
    )
    description = models.TextField(
        verbose_name='Описание сайта'
    )
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/', 
        verbose_name="Логотип"
    )
    icon = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/', 
        verbose_name="Иконка"
    )
    locate = models.CharField(
        max_length=100,
        verbose_name='Адрес'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    phone = models.CharField(
        max_length=100,
        verbose_name='Телефон'
    )
    work_schedule = models.CharField(
        max_length=100,
        verbose_name='Режим работы'
    )
    whatsapp = models.URLField(
        verbose_name='Whatsapp'
    )
    telegram = models.URLField(
        verbose_name='Telegram'
    )
    instagram = models.URLField(
        verbose_name='Instagram'
    )  
    facebook = models.URLField(
        verbose_name='Facebook'
    )
    class Meta:
        verbose_name = '1) Настройки'
        verbose_name_plural = '1) Настройки'
    def __str__(self):
        return self.title

class Service(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='service/', 
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length = 100,
        verbose_name='Название услуги'
    )
    category = models.CharField(
        max_length = 100,
        verbose_name='Категория'
    )
    descriptions = models.TextField(
        verbose_name='Описание',
        max_length=100
    )
    class Meta:
        verbose_name = '2) Услуга'
        verbose_name_plural = '2) Услуги'
    def __str__(self):
        return self.title

class OurService(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='service/', 
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length = 100,
        verbose_name='Название услуги'
    )
    class Meta:
        verbose_name = '3) Мы шьем'
        verbose_name_plural = '3) Мы шьем'
    def __str__(self):
        return self.title

class Partners(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='partners/', 
        verbose_name="Фотография"
    )
    url = models.URLField(
        verbose_name='Ссылка'
    )
    class Meta:
        verbose_name = '4) Партнеры'
        verbose_name_plural = '4) Партнеры'
