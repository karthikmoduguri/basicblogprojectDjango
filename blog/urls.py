
from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog, name='blog'),
    path('create/', views.create_post, name='create_post'),
    path('post/', views.post_list, name='post_list'),
]