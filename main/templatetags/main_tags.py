# pylint: disable=no-member
from django import template


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