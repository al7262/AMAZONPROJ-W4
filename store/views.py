from django.shortcuts import render
from .models import User, Seller, Product, PaymentMethod, Order, Category, OrderDetail

# Create your views here.

def index(request):
    categories = Category.objects.all()
    productList = []
    for category in categories:
        add = Product.objects.filter(category=category.id).all()
        product.append(add)
    return render(request, 'store/index.html', {
        'categories': categories,
        'listproduct': productList
    })

def slider(request):
    return render(request, 'store/slider-banner.html', {})

def header(request):
    return render(request, 'header.html', {})
