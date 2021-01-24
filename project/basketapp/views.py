from django.http import HttpResponseRedirect
from django.shortcuts import render

from basketapp.models import GamesBasket


def index(request):
    return render(request, 'basketapp/basket.html')


def add(request, games_id):
    GamesBasket.objects.get_or_create(
        user=request.user,
        games_id=games_id
    )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
