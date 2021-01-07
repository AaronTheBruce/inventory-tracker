# https://docs.djangoproject.com/en/2.1/ref/models/fields/
# https://doc.oroinc.com/user/concept-guides/inventory/ ideas for how to classify inventory status
from django.db import models

# Create your models here.
class Employee(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=254, unique=True)
  hashed_password = models.CharField(max_length=65)

  def __str__(self):
    return self.email

class Product(models.Model):
  # InStock, OutOfStock, Discontinued
  INVENTORY_STATUS = (  # By default, products should be Out of Stock
    ('IS', 'In Stock'),
    ('OS', 'Out of Stock'),
    ('DC', 'Discontinued'),
  )
  item_name = models.CharField(max_length=100)
  itemQuantity = models.IntegerField()
  status = models.CharField(max_length=2, choices=INVENTORY_STATUS, default='OS')

  def __self__(self):
    return self.item_name
