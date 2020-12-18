from django.shortcuts import render

from mainapp.models import GamesCategory


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
