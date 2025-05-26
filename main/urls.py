from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:category_slug>/', views.index, name='index'),
    path("route/<int:route_id>/", views.route_detail, name="route_detail"),
]