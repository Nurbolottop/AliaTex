from tabnanny import verbose
from django.db import models
from django_resized.forms import ResizedImageField
from ckeditor.fields import RichTextField
# Create your models here.
class About(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
    )    
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    experience = models.IntegerField(
        verbose_name='Опыт работы'
    )

    class Meta:
        verbose_name = '2) О нас'
        verbose_name_plural = '2) О нас'
        
    def __str__(self):
        return self.title

class AboutService(models.Model):
    service = models.ForeignKey(About, related_name='about_service', on_delete=models.CASCADE)
    title = models.CharField(
        max_length = 100,
        verbose_name = "Услуги"
    )
    subtitle = models.CharField(
        max_length = 100,
        verbose_name = "Подзаголовок"
    )
    icon = models.CharField(
        max_length = 100,
        verbose_name = "Иконка"
    )
    class Meta:
        verbose_name = "Почему мы лучше"
        verbose_name_plural = "Почему мы лучше"
        
    def __str__(self):
        return self.title

class Numbers(models.Model):
    ICON_CHOICES = [
        # Одежда
        ('fa-tshirt', 'Футболка'),
        ('fa-hat-cowboy', 'Шляпа'),
        ('fa-socks', 'Носки'),
        ('fa-vest', 'Жилет'),
        ('fa-vest-patches', 'Жилет с заплатками'),
        # Инструменты
        ('fa-scissors', 'Ножницы'),
        ('fa-ruler', 'Линейка'),
        ('fa-ruler-combined', 'Сантиметр'),
        ('fa-tape', 'Сантиметровая лента'),
        ('fa-pen-ruler', 'Лекало'),
        # Оборудование
        ('fa-print', 'Принтер для выкроек'),
        ('fa-box-open', 'Коробка с тканью'),
        ('fa-boxes', 'Упаковки'),
        # Процессы
        ('fa-cut', 'Раскрой'),
        ('fa-vector-square', 'Выкройка'),
        ('fa-th', 'Лекала'),
        # Общие
        ('fa-users', 'Команда'),
        ('fa-star', 'Качество'),
        ('fa-certificate', 'Сертификат'),
        ('fa-award', 'Награда'),
        ('fa-medal', 'Медаль'),
        ('fa-thumbs-up', 'Качество'),
        ('fa-hands-helping', 'Помощь')
    ]

    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='numbers/', 
        verbose_name="Фотография заднего фона"
    )
    icon = models.CharField(
        max_length=100,
        choices=ICON_CHOICES,
        verbose_name='Иконка'
    )
    number = models.IntegerField(
        verbose_name='в числах'
    )
    descriptions = models.CharField(
        max_length=100,
        verbose_name='Описание'
    )
    
    class Meta:
        verbose_name = '3) Мы в числах'
        verbose_name_plural = '3) Мы в числах'
        
    def __str__(self):
        return self.title

from django_resized import ResizedImageField

class Reviews_Image(models.Model):
    image = ResizedImageField(
        size=[300, 300],  # Фиксированный размер 300x300 пикселей
        quality=85,  # Качество изображения
        crop=['middle', 'center'],  # Обрезка по центру
        upload_to='reviews_image/', 
        verbose_name="Фотография"
    )
    
    class Meta:
        verbose_name = '4) Фотографии Отзывы'
        verbose_name_plural = '4) Фотографии Отзывы'
        
    def save(self, *args, **kwargs):
        # Проверяем, что нет более 4 фотографий
        if self.pk is None and Reviews_Image.objects.count() >= 4:
            raise ValueError('Максимальное количество фотографий (4) уже достигнуто')
        super().save(*args, **kwargs)
    
 