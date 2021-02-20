from django.urls import path

from . import views

urlpatterns = [
    path('api',views.getRoutes,name='routes'),
    path('api/product/all',views.getProducts,name='products'),
    path('api/product/<int:pk>',views.getProduct,name='product'),
    path('',views.home,name='home'),
]
