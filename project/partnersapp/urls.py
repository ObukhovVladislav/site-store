import partnersapp.views as partnersapp
from django.urls import path

app_name = 'partnersapp'

urlpatterns = [
    path('partners/', partnersapp.partners, name='partners'),

]
