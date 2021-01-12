from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import Employee

class RegisterForm(UserCreationForm):
  first_name = forms.CharField(label="First Name", required=True)
  last_name = forms.CharField(label="Last Name", required=True)
  email = forms.EmailField(required=True)
  class Meta:
    model = Employee
    fields = ("first_name", "last_name", "email", "password1", "password2")
