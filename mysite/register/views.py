from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from main.models import Employee

# Create your views here.
def sign_up(_res):
  if _res.method == 'POST':
    form = RegisterForm(_res.POST)
    if form.is_valid():
      form.save()
    return redirect('/')
  else:
    form = RegisterForm()
  return render(_res, 'register/register.html', {'form': form})
