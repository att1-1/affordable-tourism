# pylint: disable=no-member
from django.shortcuts import render

from main.models import Route


def index(request):

    routes = Route.objects.all().prefetch_related('age_groups', 'seasons', 'skills')

    # === ФИЛЬТРАЦИЯ ===
    age_group = request.GET.get('age_group')
    min_distance = request.GET.get('min_distance')
    max_distance = request.GET.get('max_distance')
    min_duration = request.GET.get('min_duration')
    max_duration = request.GET.get('max_duration')

    if age_group:
        routes = routes.filter(age_groups__code=age_group)
    if min_distance:
        routes = routes.filter(distance__gte=min_distance)
    if max_distance:
        routes = routes.filter(distance__lte=max_distance)
    if min_duration:
        routes = routes.filter(duration__gte=min_duration)
    if max_duration:
        routes = routes.filter(duration__lte=max_duration)

    # === СОРТИРОВКА ===
    sort_by = request.GET.get('sort_by', 'id')
    if sort_by in ['distance', 'duration', 'cost']:
        routes = routes.order_by(sort_by)

    context = {
        'routes': routes
    }
    return render(request, 'main/index.html', context)
