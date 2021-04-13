from django.contrib.auth.models import update_last_login
from django.core.checks import messages
from django.http import JsonResponse, response
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from ..models import *
from ..serializers import *



from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status



#Product API


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def getProduct(request,pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

