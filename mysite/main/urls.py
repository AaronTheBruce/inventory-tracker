# define paths to different views

from django.urls import path

from . import views

urlpatterns = [
  path('sign-up/', views.sign_up, name='sign-up'),
  path('log-in/', views.log_in, name='log-in'),
  path('create/', views.create, name='create'),
  path('', views.home, name='home'),
  path('', views.index, name='index'), # index page
]
