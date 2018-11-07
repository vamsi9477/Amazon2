from django.db import models

# Create your models here.

class amazonwebsite(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10,primary_key=True)
    email=models.EmailField()
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=8)
    address=models.CharField(max_length=500)

class paymentprocesses(models.Model):
    watchestypes=models.CharField(max_length=10)
    watchesname=models.CharField(max_length=100)
    Money=models.IntegerField(default=10)
    customercno = models.IntegerField(default=10, primary_key=True)
    customeradd = models.CharField(max_length=500)
    cardtype=models.CharField(max_length=50)
    bankname=models.CharField(max_length=50)
    cardnumber=models.IntegerField(default=11)
    cardname=models.CharField(max_length=10)
    cvvno=models.IntegerField(default=3)

class comments(models.Model):
    comment=models.CharField(max_length=10000)

