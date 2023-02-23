from rest_framework import status
from django.conf import settings
from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_auth.registration.views import RegisterView

class UserRegisterationAPIView(RegisterView):
    serializer_class = RegistrationSerializer


    