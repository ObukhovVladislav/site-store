import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.catalog, name='catalog'),
    path('catalog/category/<int:category_pk>/', mainapp.catalog_section, name='catalog_section'),
    path('catalog/game/<int:game_pk>/', mainapp.game_page, name='game_page'),
]
