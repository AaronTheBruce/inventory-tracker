from django import forms
from .models import Product

class CreateNewProduct(forms.Form):
  CHOICES = (('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock'), ('Discontinued', 'Discontinued'),)
  item_name = forms.CharField(label="Name", max_length=200, required=True)
  item_quantity = forms.IntegerField(label="Quantity", required=True)
  status = forms.ChoiceField(label="Status", choices=CHOICES, required=True)
