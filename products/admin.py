from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['CATname','CATparent']

@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display =['name','price','PRdiscount_price','PRstate','PRnp_available']

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['id','created_at']

@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display =['product','qunatity']
