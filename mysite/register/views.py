from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from main.models import Employee

# Create your views here.
def sign_up(_res):
  if _res.method == 'POST':
    sign_up = RegisterForm(_res.POST)
    if sign_up.is_valid():
      # pull in user info to resolve
      sign_up.save()
      return redirect('/')
  else:
    sign_up = RegisterForm()
  return render(_res, 'register/register.html', {'form': sign_up})
