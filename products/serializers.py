from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude =['id','PRnew','PRbestseller','category','pr_code','PRdescription','PRdiscount_price','PRstate','PRimage','PRnp_available','slug','created_at','updated_at','PRinformation']

class CartSerializer(serializers.ModelSerializer):
    product = ProductsSerializer(many=False)
    class Meta:
        model = Cart
        exclude =['id','created_at','user']

class OrderSerializer(serializers.ModelSerializer):
    items = CartSerializer(many=True)
    class Meta:
        model = Order
        fields = ['items']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude =['CATdescription','image','slug']


