from django.db import models


class Partners(models.Model):
    name = models.CharField(verbose_name='Партнёры', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнёры'
        verbose_name_plural = 'Партнёры'
