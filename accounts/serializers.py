from django.db.models import Q
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_auth.registration.serializers import RegisterSerializer

from .models import *

class RegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(Q(email__iexact=email)).exists():
            raise serializers.ValidationError('Email is already exist')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(Q(username__iexact=username)).exists():
            raise serializers.ValidationError('Username is already exist please try again')
        return username
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise serializers.ValidationError("Password don't match")

        return password2



