# https://www.techwithtim.net/tutorials/django/admin-page/
from django.contrib import admin
from .models import Employee, Product
# Register your models here.
admin.site.register({Employee, Product})
