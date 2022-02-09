from django.urls import path, include
from . import views

app_name='blog'  # to specify the app name for accuracy to avoid duplication in name

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
]