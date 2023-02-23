import django_filters

from .models import *

class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Products
        exclude =['category','pr_code','PRdescription','PRdiscount_price','PRstate','PRimage','PRnp_available','slug','created_at','updated_at']
