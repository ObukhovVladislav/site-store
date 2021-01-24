from django.shortcuts import render


def login(request):
    context = {
        'page_title': 'Авторизация'
    }
    return render(request, 'authapp/login.html', context)
