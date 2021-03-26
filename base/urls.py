from django.urls import path

from . import views

urlpatterns = [
    path('users/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api',views.getRoutes,name='routes'),
    path('api/product/all',views.getProducts,name='products'),
    path('api/product/<int:pk>',views.getProduct,name='product'),
    path('',views.home,name='home'),
    path('api/users/profile/',views.getUserProfile, name="user_profile")
]
