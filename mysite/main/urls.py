# define paths to different views
from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'), # index page
  path('v1/', views.v1, name='view v1'),
]
