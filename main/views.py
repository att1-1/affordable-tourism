# pylint: disable=no-member
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.db.models import Min

from .models import Route, Comment
from main.models import Skill, AgeGroup, Season

def index(request):
    routes = Route.objects.all().prefetch_related('age_groups', 'seasons', 'skills')

    # === ФИЛЬТРАЦИЯ по сезонам ===
    selected_seasons = request.GET.getlist('season')
    if selected_seasons:
        routes = routes.filter(seasons__id__in=selected_seasons).distinct()

    # === СОРТИРОВКИ ===
    if 'level' in request.GET:
        sort_level = request.GET['level']
        if sort_level == 'level':
            routes = routes.annotate(min_age_code=Min('age_groups__code')).order_by('min_age_code')
        elif sort_level == '-level':
            routes = routes.annotate(min_age_code=Min('age_groups__code')).order_by('-min_age_code')

    if 'distance' in request.GET:
        sort_distance = request.GET['distance']
        if sort_distance == 'distance':
            routes = routes.order_by('distance')
        elif sort_distance == '-distance':
            routes = routes.order_by('-distance')

    if 'duration' in request.GET:
        sort_duration = request.GET['duration']
        if sort_duration == 'duration':
            routes = routes.order_by('duration')
        elif sort_duration == '-duration':
            routes = routes.order_by('-duration')

    context = {
        'routes': routes,
        'all_seasons': Season.objects.all()
    }
    return render(request, 'main/index.html', context)


def get_comments(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    comments = route.comments.filter(is_approved=True)

    html = render_to_string('main/modal_content.html', {
        'route': route,
        'comments': comments
    }, request=request) # Из за этого тоже походу ничего не работало
    return HttpResponse(html)


def submit_comment(request, route_id):
    route = get_object_or_404(Route, id=route_id)

    if request.method == 'POST':
        author_name = request.POST.get('author_name', 'Аноним')
        text = request.POST.get('text', '')

        if not text:
            return JsonResponse({'success': False, 'error': 'Текст комментария обязателен'})

        Comment.objects.create(
            route=route,
            author_name=author_name,
            text=text,
            is_approved=True
        )

        comments = route.comments.filter(is_approved=True)
        html = render_to_string(
            'main/comments_list.html',
            {'comments': comments},
            request=request # Походу из за этого не работали комментарии
        )

        return JsonResponse({
            'success': True,
            'html': html,
            'count': comments.count()
        })

    return JsonResponse({'success': False})
