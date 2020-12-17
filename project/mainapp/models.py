from django.db import models


class GamesCategory(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=128)
    desc = models.TextField(verbose_name='Описание ', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории игр'
        verbose_name_plural = 'Категория игр'


class Games(models.Model):
    category = models.ForeignKey(GamesCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название игры', max_length=128)
    desc = models.TextField(verbose_name='Описание игры', blank=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игры'
