# define paths to different views

from django.urls import path

from . import views

urlpatterns = [
  path('update/<int:_id>/', views.update, name='update'),
  path('create/', views.create, name='create'),
  # path('delete/<int:id>', None, name='delete'),
  path('', views.home, name='home'),
  path('', views.index, name='index'), # index page
]
