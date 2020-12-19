from django.shortcuts import render

# Create your views here.
from partnersapp.models import Partners


def partners(request):
    partners = Partners.objects.all()
    context = {
        'partners': partners,
    }
    return render(request, 'partnersapp/index.html', context)
