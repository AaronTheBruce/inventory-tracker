# define paths to different views
from django.urls import path

from . import views

urlpatterns = [
  path('<int:id>', views.index, name='index'), # index page
]
