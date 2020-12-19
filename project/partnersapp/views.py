from django.shortcuts import render

# Create your views here.
from partnersapp.models import Partners


def partners(request):
    partner = Partners.objects.all()
    context = {
        'partner': partner,
    }
    return render(request, 'partnersapp/index.html', context)
