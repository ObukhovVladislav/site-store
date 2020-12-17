from django.contrib import admin

# Register your models here.
from mainapp.models import GamesCategory, Games

admin.site.register(GamesCategory)
admin.site.register(Games)
