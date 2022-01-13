from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from django.db.models.deletion import CASCADE
# Create your models here.
class Todo(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   completed = models.BooleanField(default=False)

   def _str_(self):
     return self.title


class Feature(models.Model):
      # auto created ID
      name=models.CharField(max_length=20)
      details=models.CharField(max_length=100)
      is_true=models.BooleanField(default=True)

class islamicarticle(models.Model):
      article_ID = models.AutoField(primary_key=True)
      title=models.CharField(max_length=100)
      article_slug=models.CharField(max_length=100)
      article_meta=models.TextField(max_length=100)
      bcontent = models.TextField(max_length=5000)
      created_at=models.DateTimeField(default=datetime.now,blank=True)

class Quiz(models.Model):
      questionID=models.AutoField(primary_key=True)
      question=models.CharField(max_length=250)
      op1=models.CharField(max_length=200)
      op2=models.CharField(max_length=200)
      op3=models.CharField(max_length=200)
      op4=models.CharField(max_length=200)
      correctop=models.CharField(max_length=200)

class Hadith(models.Model):
      Hadith_ID=models.AutoField(primary_key=True)
      ArabicText=models.CharField(max_length=2500)
      HAdith_Trans=models.CharField(max_length=1000)
      Hadith_Topic=models.CharField(max_length=300)
      Hadith_referenece=models.CharField(max_length=250)

class QuranicVerse(models.Model):
      QuranicVerse_ID=models.AutoField(primary_key=True)
      ArabicText=models.CharField(max_length=2500)
      Quranic_Trans=models.CharField(max_length=1000)
      Quranic_Topic=models.CharField(max_length=300)
      Quranic_reference=models.CharField(max_length=250)
class Products(models.Model):
      productID=models.AutoField(primary_key=True)
      productName=models.CharField(max_length=200)
      productQuantity=models.IntegerField()
      productPrice=models.IntegerField() # not sure 
      InStock=models.BooleanField()
      ImagePath=models.CharField(max_length=200)

      # in stock TRUE FALSE

class PurchaseHistory(models.Model):
      # address ,foreign key userID/product ID, delivery date , Totalprice,Total Item 
      username= models.ForeignKey(User, default=None, on_delete=CASCADE)
      TransactionID=models.AutoField(primary_key=True)
      productID=models.ForeignKey(Products, on_delete=CASCADE)
      created_at=models.DateTimeField(default=datetime.now,blank=True)
      priceOneUnit=models.IntegerField()
      Quantity=models.IntegerField()

    

