# define paths to different views

from django.urls import path

from . import views

urlpatterns = [
  path('create/', views.create, name='create'),
  path('', views.home, name='home'),
  path('', views.index, name='index'), # index page
]
