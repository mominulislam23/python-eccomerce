from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

class Product(models.Model):    
    product_id = models.AutoField
    product_name = models.CharField(max_length=350)
    product_desc = models.CharField(max_length=50)
    pub_date = models.DateField()
    category = models.CharField(default=0, max_length=50)
    subcategory = models.CharField(default=0, max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")

def __st__(self):
    return self.product_name
