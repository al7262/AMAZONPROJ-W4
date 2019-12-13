from django.shortcuts import render
from .models import User, Seller, Product, PaymentMethod, Order, Category, OrderDetail

# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'store/index.html', {
        'categories': categories,
        'products': products
    })

def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'store/product.html', {
        'product': product
    })

def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, 'store/category.html', {
        'category': category
    })

def slider(request):
    return render(request, 'store/slider-banner.html', {})

def header(request):
    return render(request, 'store/header.html', {})

def cart0(request):
    return render(request, 'store/cart0.html', {})

def cart1(request):
    return render(request, 'store/cart1.html', {})
