# pylint: disable=no-member
from django.shortcuts import render

from main.models import Routes


def index(request):
    routes = Routes.objects.all()
    
    context = {
        'routes': routes,
    }

    return render(request, 'main/index.html', context)
