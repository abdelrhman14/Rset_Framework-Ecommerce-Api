from .views import *
from django.urls import path


from django.conf.urls import url
from django.urls import path, include


urlpatterns = [

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('registration/',UserRegisterationAPIView.as_view(),name='registration'),

   
]