# pylint: disable=no-member
from django import template
from django.utils.http import urlencode


register = template.Library()

@register.simple_tag
def get_level_and_age(level):
    """
    Возвращает строку с уровнем и возрастом, если ключ существует в словаре.
    """
    getting_age = {
        '3': '11-12 лет',
        '4': '13-15 лет',
        '5': '16-17 лет',
        '6': '18-29 лет',
        '7': '30-39 лет',
        '8': '40-49 лет',
        '9': '50-59 лет',
    }

    age = getting_age.get(str(level))
    if age:
        return f"{level}: {age}"
    return f"{level}: Возраст не указан"


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)


@register.filter
def hours_format(value):
    try:
        hours = float(value)
        if hours == 1:
            return "час"
        elif 2 <= hours <= 4:
            return "часа"
        else:
            return "часов"
    except:
        return "часов"
