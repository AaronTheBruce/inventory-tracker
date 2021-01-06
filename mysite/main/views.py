from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(_response):
  return HttpResponse("<h1>Yeet from views.py</h1>")

def v1(_response):
  return HttpResponse("<h1>View 1</h1>")
