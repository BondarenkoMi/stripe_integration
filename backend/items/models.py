from django.db import models

class Item(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

