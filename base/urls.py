from django.urls import path

from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
   
)
urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api',views.getRoutes,name='routes'),
    path('api/product/all',views.getProducts,name='products'),
    path('api/product/<int:pk>',views.getProduct,name='product'),
    path('',views.home,name='home'),
]
