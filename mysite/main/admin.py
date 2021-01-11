# https://www.techwithtim.net/tutorials/django/admin-page/
# https://dev.to/joshwizzy/customizing-django-authentication-using-abstractbaseuser-llg
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Employee
from register.forms import UserCreationForm
# Register your models here.

class EmployeeAdmin(BaseUserAdmin):
  form = UserCreationForm

  list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
  list_filter = ('is_superuser',)

  fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
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

# admin.site.register(Employee, EmployeeAdmin)
