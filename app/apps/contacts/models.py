from django.db import models
from django_resized import ResizedImageField

class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    review_text = models.TextField(verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.name} - {self.created_at.strftime("%d.%m.%Y")}'
    
    class Meta:
        verbose_name = '1) Отзыв'
        verbose_name_plural = '1) Отзывы'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.name} - {self.created_at.strftime("%d.%m.%Y")}'
