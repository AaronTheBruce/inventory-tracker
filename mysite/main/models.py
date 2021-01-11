# https://docs.djangoproject.com/en/2.1/ref/models/fields/
# https://doc.oroinc.com/user/concept-guides/inventory/ ideas for how to classify inventory status
# https://www.techwithtim.net/tutorials/django/
# https://github.com/arsentieva/campy-backend/blob/master/app/models/models.py | referring to an old project I worked on
# https://dev.to/joshwizzy/customizing-django-authentication-using-abstractbaseuser-llg
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.utils.translation import ugettext_lazy as _

class EmployeeManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password, **extra_fields):
        values = [email, first_name, last_name]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, phone, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, password, **extra_fields)

# Create your models here.
class Employee(AbstractBaseUser, PermissionsMixin):

  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  objects = EmployeeManager()

  def get_username(self):
    return self.email

  def to_dictionary(self):
    return {
      "id": self.id,
      "first_name": self.first_name,
      "last_name": self.last_name,
      "email": self.email,
      "password": self.password
    }

# Employee._meta.get_field_by_name('email')[0]._unique=True

class Product(models.Model):
  # InStock, OutOfStock, Discontinued
  INVENTORY_STATUS = (  # By default, products should be Out of Stock
    ('In Stock', 'In Stock'),
    ('Out of Stock', 'Out of Stock'),
    ('Discontinued', 'Discontinued'),
  )
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default="") # default set to "" to bypass makemigrations error
  item_name = models.CharField(max_length=100)
  item_quantity = models.IntegerField(default=0)
  status = models.CharField(max_length=12, choices=INVENTORY_STATUS, default='Out of Stock')

  def to_dictionary(self):
    return {
      "id": self.id,
      "item_name": self.item_name,
      "item_quantity": self.item_quantity,
      "status": self.status,
      "employee_id": self.employee_id,
    }
