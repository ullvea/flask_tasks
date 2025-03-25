from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    image = models.ImageField