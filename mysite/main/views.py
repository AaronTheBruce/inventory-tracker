from django.shortcuts import render
from .models import Employee, Product
from .forms import CreateNewProduct
# Create your views here.

def index(_response):
  employee = Employee.objects.get(id=2)
  return render(_response, "main/base.html", {})

def home(_response):
  return render(_response, "main/home.html", {})

def sign_up(_response):
  return render(_response, "main/sign-up.html", {})

def log_in(_response):
  return render(_response, "main/log-in.html", {})

def create(_response):
  if _response.method == "POST":
    form = CreateNewProduct(_response.POST)
    if(form.is_valid()):
      n = form.cleaned_data["item_name"]
      q = form.cleaned_data["item_quantity"]
      s = form.cleaned_data["status"]
      # e = employee_id
      product = Product(item_name=n, item_quantity=q, status=s, employee_id=2) # once login has been implemented, we can get the employee id to fill here
      product.save()
  else:
    form = CreateNewProduct()
  return render(_response, "main/create.html", {'form': form})
