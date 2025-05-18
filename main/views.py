# pylint: disable=no-member
from django.shortcuts import render

from main.models import Route


def index(request):

    routes = Route.objects.all()

    # === ФИЛЬТРАЦИЯ ===
    level = request.GET.get('level')  # Уровень сложности (например, "I", "II")
    min_distance = request.GET.get('min_distance')  # Минимальная протяженность
    max_distance = request.GET.get('max_distance')  # Максимальная протяженность
    min_duration = request.GET.get('min_duration')  # Минимальная продолжительность
    max_duration = request.GET.get('max_duration')  # Максимальная продолжительность

    if level and level != "default":
        routes = routes.filter(level=level)
    if min_distance:
        routes = routes.filter(distance__gte=min_distance)
    if max_distance:
        routes = routes.filter(distance__lte=max_distance)
    if min_duration:
        routes = routes.filter(duration__gte=min_duration)
    if max_duration:
        routes = routes.filter(duration__lte=max_duration)

    # === СОРТИРОВКА === (ваш текущий код)
    sort_by = request.GET.get('sort_by')  # Параметр сортировки (например, "distance", "-duration")
    if sort_by and sort_by != "default":
        routes = routes.order_by(sort_by)

    context = {
        'routes': routes,
    }
    return render(request, 'main/index.html', context)
