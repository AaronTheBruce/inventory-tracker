from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from main.models import Employee

# Create your views here.
def sign_up(_req):
  if _req.method == 'POST':
    sign_up = RegisterForm(_req.POST)
    if sign_up.is_valid():
      # pull in user info to resolve
      sign_up.save()
      email = _req.POST['email']
      password = _req.POST['password1']
      employee = authenticate(_req, email=email, password=password)
      login(_req, employee)
      return redirect('/')
  else:
    sign_up = RegisterForm()
  return render(_req, 'register/register.html', {'form': sign_up})

# def log_in(_req):
#   if _req.method == 'POST'
