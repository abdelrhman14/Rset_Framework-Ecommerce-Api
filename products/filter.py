from random import choice, choices
from unittest import result
from django import forms
import django_filters
from matplotlib import widgets

from .models import *

class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Products
        exclude =['category','pr_code','PRdescription','PRdiscount_price','PRstate','PRimage','PRnp_available','slug','created_at','updated_at']
