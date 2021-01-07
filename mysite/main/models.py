# https://docs.djangoproject.com/en/2.1/ref/models/fields/
# https://doc.oroinc.com/user/concept-guides/inventory/ ideas for how to classify inventory status
# https://www.techwithtim.net/tutorials/django/sqlite3-database/
from django.db import models

# Create your models here.
class Employee(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=254, unique=True)
  hashed_password = models.CharField(max_length=65)

  def to_dictionary(self):
    return {
      "id": self.id,
      "first_name": self.first_name,
      "last_name": self.last_name,
      "email": self.email,
      "hashed_password": self.hashed_password,
    }

class Product(models.Model):
  # InStock, OutOfStock, Discontinued
  INVENTORY_STATUS = (  # By default, products should be Out of Stock
    ('IS', 'In Stock'),
    ('OS', 'Out of Stock'),
    ('DC', 'Discontinued'),
  )
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default="") # default set to "" to bypass makemigrations error
  item_name = models.CharField(max_length=100)
  item_quantity = models.IntegerField(default=0)
  status = models.CharField(max_length=2, choices=INVENTORY_STATUS, default='OS')

  def to_dictionary(self):
    return {
      "id": self.id,
      "item_name": self.item_name,
      "item_quantity": self.item_quantity,
      "status": self.status,
      "employee": self.employee,
    }
