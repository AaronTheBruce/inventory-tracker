# https://www.techwithtim.net/tutorials/django/admin-page/
# https://dev.to/joshwizzy/customizing-django-authentication-using-abstractbaseuser-llg
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from register.forms import UserCreationForm

from main.models import Employee

class UserCreationForm(forms.ModelForm):
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Password', widget=forms.PasswordInput)

  class Meta:
    model = Employee
    fields = ('first_name', 'last_name', 'email')

  def clean_password2(self):
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if(password1 and password2 and password1 != password2):
      raise ValidationError("Passwords don't match")
    return password2

  def save(self, commit=True):
    employee = super().save(commit=False)
    employee.set_password(self.cleaned_data["password1"])
    if commit:
      user.save()
    return user

# Register your models here.

class EmployeeAdmin(BaseUserAdmin):
  add_form = UserCreationForm

  list_display = ('email', 'first_name', 'last_name', 'is_superuser')
  list_filter = ('is_superuser',)
  fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_admin', 'is_superuser',)}),
  )
  add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

  search_fields = ('email', 'first_name', 'last_name')
  ordering=('email',)
  filter_horizontal = ()

admin.site.register(Employee, EmployeeAdmin)
