# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact = models.CharField(max_length=15)
    joinedAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    joinedAt = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class PaymentMethod(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = RichTextField()
    photo = models.ImageField(upload_to='store/static/img')
    rate = models.DecimalField(max_digits=2,decimal_places=1)
    brandName = models.CharField(max_length=200)
    stock = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    payment = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    shipAddres = models.TextField()

    def __str__(self):
        return "Order from" + str(self.user)

class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    def __str__(self):
        return "Detail of" + str(self.order)