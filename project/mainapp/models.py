from django.db import models


class GamesCategory(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=128)
    desc = models.TextField(verbose_name='Описание ', blank=True)


class Games(models.Model):
    category = models.ForeignKey(GamesCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название игры', max_length=128)
    desc = models.TextField(verbose_name='Описание игры', blank=True)
    is_active = models.BooleanField(verbose_name='Активен',  default=True)
