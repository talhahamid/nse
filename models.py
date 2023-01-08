from django.db import models

class Users(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=50)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    pincode=models.CharField(max_length=100)

class Plan(models.Model):
    uid =models.IntegerField()
    price = models.CharField(max_length=100) 
    plan_name = models.CharField(max_length=100)
    start_date = models.DateField() 
    end_date = models.DateField()
    status = models.BooleanField(default=False)

class Plantype(models.Model): 
    name = models.CharField(max_length=100)
    img = models.ImageField() 
    duration =models.CharField(max_length=100)
    price =models.CharField(max_length=100)
    description=models.CharField(max_length=300)