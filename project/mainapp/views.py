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


def basket(request):
    return render(request, 'mainapp/basket.html')


def catalog_page(request, pk):
    games = Games.objects.filter(category_id=pk)
    context = {
        'games': games,
        'page_title': 'Страница каталога'
    }
    return render(request, 'mainapp/catalog_page.html', context)
