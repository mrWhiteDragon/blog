from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('posts/add', views.post_add, name='post_add')
]
