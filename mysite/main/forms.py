from django import forms
from .models import Product

class CreateNewProduct(forms.Form):
  item_name = forms.CharField(label="Name", max_length=200, required=True)
  item_quantity = forms.IntegerField(label="Quantity", required=True)
  status = forms.CharField(label="Status", max_length=2, required=True)
