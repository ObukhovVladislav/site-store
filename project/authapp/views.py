from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render


def login(request):
    form = AuthenticationForm()
    context = {
        'page_title': 'Авторизация',
        'form': form,

    }
    return render(request, 'authapp/login.html', context)
