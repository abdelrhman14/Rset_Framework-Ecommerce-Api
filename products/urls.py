from django.urls import path
from . import views
urlpatterns = [
    path('category',views.home,name='home'),
    path('category_type/<slug:slug>/',views.product,name='category'),
    path('product_filter/<slug:slug>/',views.product_filter,name='category'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('user_cart/',views.user_cart,name='user_cart'),
    path('order/',views.order,name='user_cart'),
    path('create_new_order/',views.create_new_order,name='create_new_order'),



]
