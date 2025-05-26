from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('get-comments/<int:route_id>/', views.get_comments, name='get_comments'),
    path('submit-comment/<int:route_id>/', views.submit_comment, name='submit_comment'),
    path('<slug:category_slug>/', views.index, name='index'),
]
