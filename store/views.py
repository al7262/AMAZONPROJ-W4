from django.shortcuts import render

# Create your views here.

def slider(request):
    return render(request, 'store/slider-banner.html', {})

def header(request):
    return render(request, 'store/header.html', {})

def cart0(request):
    return render(request, 'store/cart0.html', {})
