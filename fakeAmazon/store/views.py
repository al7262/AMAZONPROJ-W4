from django.shortcuts import render

# Create your views here.

def slider(request):
    return render(request, 'store/slider-banner.html', {})