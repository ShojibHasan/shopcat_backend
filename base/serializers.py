from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id','username','email']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
