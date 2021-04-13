from django.urls import path

from base.views import product_views as views

urlpatterns = [
    

    #Product URL
    path('',views.getProducts,name='products'),
    path('<int:pk>',views.getProduct,name='product'),
]
