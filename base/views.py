from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


def getRoutes(request):
    return JsonResponse('Hello',safe=False)