# pylint: disable=no-member
from django.shortcuts import render

from main.models import Routes


def index(request):

    routes = Routes.objects.all()
    
    level = request.GET.get('level', None)
    distance = request.GET.get('distance', None)
    duration = request.GET.get('duration', None)

    if level and level != "default":
        routes = routes.order_by(level)
    
    if distance and distance != "default":
        routes = routes.order_by(distance)
    
    if duration and duration != "default":
        routes = routes.order_by(duration)


    context = {
        'routes': routes,
    }

    return render(request, 'main/index.html', context)
