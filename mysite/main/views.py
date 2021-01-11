from django.shortcuts import render, redirect
from .models import Employee, Product
from .forms import CreateNewProduct
# Create your views here.
# https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/

def index(_response):
  employee = Employee.objects.get(id=2)
  return render(_response, "main/base.html", {})

def home(_response):
  context = {}  # placeholder
  context["dataset"] = Product.objects.all() # provide product values to the key, dataset.
  return render(_response, "main/home.html", context)

def create(_response, id=None):
  if _response.method == "POST":
    form = CreateNewProduct(_response.POST)
    if(form.is_valid()):
      n = form.cleaned_data["item_name"]
      q = form.cleaned_data["item_quantity"]
      s = form.cleaned_data["status"]
      e = 1 # database currently loaded with a demo user, auth needs work but I cannot spend more time on it w/o having a working product
      product = Product(item_name=n, item_quantity=q, status=s, employee_id=e) # once login has been implemented, we can get the employee id to fill here
      product.save()
    return redirect('/')
  # elif _response.method == "PUT":
  #   data = Product.objects.get(id=id)
  #   form = UpdateProduct(_response.PUT, data)
  #   if(form.is_valid()):
  #     n = form.cleaned_data["item_name"]
  #     q = form.cleaned_data["item_quantity"]
  #     s = form.cleaned_data["status"]
  #     e = 1
  else:
    form = CreateNewProduct()

  return render(_response, "main/create.html", {'form': form})
