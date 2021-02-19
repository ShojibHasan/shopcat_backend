from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=False)
    name = models.CharField(max_length=200,null=True,blank=True)
    # image =
    brand = models.CharField(max_length=200,null=True,blank=True)
    category = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=True)
    number_of_reviews = models.IntegerField(null=True,blank=True,default=0)
    price = models.DecimalField(decimal_places=2,null=True,blank=True)
    count_in_stock =models.IntegerField(null=True,blank=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True,editable=False)