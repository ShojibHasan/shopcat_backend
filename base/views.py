from django.http import JsonResponse, response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


def getRoutes(request):
    return JsonResponse('Hello',safe=False)


def home(request):
    return render(request,'index.html')
