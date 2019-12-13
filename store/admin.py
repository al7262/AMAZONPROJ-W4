# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User, Seller, Product, PaymentMethod, Order, Category, OrderDetail

# Register your models here.

admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(PaymentMethod)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(OrderDetail)