from django.db import models


class GamesCategory(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
