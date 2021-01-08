# define paths to different views

from django.urls import path

from . import views

urlpatterns = [
  path('sign-up/', views.sign_up, name='sign-up'),
  path('login/', views.log_in, name='login'),
  path('', views.home, name='home'),
  path('', views.index, name='index'), # index page
]
