from rest_framework import serializers
from main.models import Product


class ProductSerializer(serializers.ModelSerializer):

  class Meta:
    model = Product
    fields = ('id',
              'item_name',
              'item_quantity',
              'status',
              'employee_id')
