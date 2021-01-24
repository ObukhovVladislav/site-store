# from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from authapp.forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            pass
    else:
        form = LoginForm

    context = {
        'page_title': 'Авторизация',
        'form': form,

    }
    return render(request, 'authapp/login.html', context)
