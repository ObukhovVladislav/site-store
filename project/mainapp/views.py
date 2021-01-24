from django.shortcuts import render

from mainapp.models import GamesCategory, Games


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    categories = GamesCategory.objects.all()
    context = {
        'categories': categories,
        'page_title': 'Каталог'
    }
    return render(request, 'mainapp/catalog.html', context)


def catalog_section(request, category_pk):
    games = Games.objects.filter(category_id=category_pk)
    context = {
        'games': games,
        'page_title': 'Страница каталога'
    }
    return render(request, 'mainapp/catalog_section.html', context)


def game_page(request, game_pk):
    game = Games.objects.get(pk=game_pk)
    context = {
        'game': game,
        'page_title': 'Страница игры'
    }
    return render(request, 'mainapp/game_page.html', context)
