# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render

from authapp.forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            authenticate(request, username=username, password=password)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm

    context = {
        'page_title': 'Авторизация',
        'form': form,

    }
    return render(request, 'authapp/login.html', context)
