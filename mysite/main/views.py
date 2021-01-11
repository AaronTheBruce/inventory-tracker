from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee, Product
from .forms import CreateNewProduct
# Create your views here.
# https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/
# https://projectsplaza.com/add-and-update-data-with-modelform-in-django-3/

def index(_req):
  employee = Employee.objects.get(id=2)
  return render(_req, "main/base.html", {})

def home(_req):
  context = {}  # placeholder
  context["dataset"] = Product.objects.all() # provide product values to the key, dataset.
  return render(_req, "main/home.html", context)

def create(_req):
  if _req.method == "POST":
    form = CreateNewProduct(_req.POST)
    if(form.is_valid()):
      n = form.cleaned_data["item_name"]
      q = form.cleaned_data["item_quantity"]
      s = form.cleaned_data["status"]
      e = 1 # database currently loaded with a demo user, auth needs work but I cannot spend more time on it w/o having a working product
      product = Product(item_name=n, item_quantity=q, status=s, employee_id=e) # once login has been implemented, we can get the employee id to fill here
      product.save()
    return redirect('/')
  else:
    form = CreateNewProduct()

  return render(_req, "main/create.html", {'form': form})

def update(_req, _id):
  item=Product.objects.get(id=_id)
  updateForm=CreateNewProduct(instance=item)
  if _req.method == "POST":
    productAdd=CreateNewProduct(_req.POST, instance=item)
    if productAdd.is_valid():
      productAdd.save()
      messages.success(_req, 'Data has been updated')
      return redirect('/')
  return render(_req, 'main/update.html', {'form':updateForm, 'item': item})
