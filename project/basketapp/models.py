from django.contrib.auth.models import User
from django.db import models

from mainapp.models import Games


class GamesBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
