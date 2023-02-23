from .models import *
from .filter import *

from .serializers import *
from rest_framework.authentication import TokenAuthentication

from django.shortcuts import get_object_or_404
from requests import request

from django.contrib import messages
from rest_framework.response import Response

from rest_framework.decorators import api_view, authentication_classes
from rest_framework import filters


@api_view(["get"])
def home(request):
    category_list = Category.objects.all().order_by('id')
    #category_list = Category.objects.filter(CATparent=None).order_by('id')
    categoryserializer =  CategorySerializer(category_list,many = True)
    return Response(categoryserializer.data)

@api_view(["get"])
def product(request,slug):
    category = Category.objects.get(slug=slug)
    product_list = Products.objects.filter(category=category).order_by('price')
    serializer_qs = ProductsSerializer(product_list,many=True)
    return Response(serializer_qs.data)

@api_view(['get'])
def product_filter(request,slug):
    category = Category.objects.get(slug=slug)
    product_list = Products.objects.filter(category=category)
    myfilter = ProductFilter(request.GET,queryset=product_list)
    if myfilter.is_valid():
        queryset = myfilter.qs
    serializer_qs = ProductsSerializer(queryset,many=True)
    return Response(serializer_qs.data)

@api_view(["post"])
def add_to_cart(request,slug):
    if request.user.is_authenticated:
        product = get_object_or_404(Products,slug=slug)
        user = request.user
        order_qs = Order.objects.filter(user=user)
        # check the user have any order or not
        if order_qs.exists():
            order_id = order_qs.earliest('-id').pk
            # check if the order item is in the order or not
            try:
                order_item = Cart.objects.get(product_id=product.pk,user=user,order_id=order_id)
                order_item.qunatity += 1
                order_item.save() 
                s = CartSerializer(order_item)
                return Response(s.data)
            except:
                new_item = Cart.objects.create(product_id=product.pk,order_id=order_id,user=user,qunatity=1)
                new_item.save()
                s = CartSerializer(new_item)
                return Response(s.data)
        else:
            order = Order.objects.create(user=user)
            new_item = Cart.objects.create(product_id=product.pk,order_id=order.pk,user=user,qunatity=1)
            new_item.save()
            s = CartSerializer(new_item)
            return Response(s.data)


                

@api_view(["get"])
def user_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user) 
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

@api_view(['get'])
def order(request):
    if request.user.is_authenticated:
        o = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(o, many=True)
        return Response(serializer.data)

@api_view(['post'])
def create_new_order(request):
    if request.user.is_authenticated:
        user = request.user
        order = Order.objects.filter(user=request.user)    
        order = Order.objects.create(user=user)
        order.save() 
        serializer = OrderSerializer(order)
        return Response(serializer.data)
