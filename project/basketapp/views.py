from django.shortcuts import render

from basketapp.models import GamesBasket


def index(request):
    return render(request, 'basketapp/basket.html')


def add(request, games_id):
    basket_item = GamesBasket.objects.get_or_create(
        user=request.user,
        games=games_id
    )
