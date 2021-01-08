from django.shortcuts import render
from .models import Employee, Product
# Create your views here.

def index(_response):
  employee = Employee.objects.get(id=2)
  return render(_response, "main/base.html", {})

def home(_response):
  return render(_response, "main/home.html", {})

def sign_up(_response):
  return render(_response, "main/sign-up.html", {})

def log_in(_response):
  return render(_response, "main/login.html", {})
