from django.contrib import admin
from .models import Route, AgeGroup, Season

# Удалите все @admin.register декораторы, если они есть
admin.site.register(Route)
admin.site.register(AgeGroup)
admin.site.register(Season)