from django.db import models
from django.contrib.auth.models import User


       
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    tags = models.CharField(max_length=20)
    category_photo = models.ImageField(upload_to='./static/images')

   

    def __str__(self):
        return self.category_name
    
    
# Create your models here.
class Products(models.Model):
    product_name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='./static/images')
    details = models.TextField(max_length=500)
    stock = models.IntegerField()
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)

    price=models.CharField(max_length=50)

    def __str__(self):
        return self.product_name
    
    
    
class Cart(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)

    no = models.IntegerField()

    new_price = models.IntegerField(default=0)

    def __str__(self):
        return self.product.product_name
    
class Your_Order(models.Model):
     
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     product = models.ForeignKey(Products,on_delete=models.CASCADE)
     cart = models.ForeignKey(Cart,on_delete=models.CASCADE)