from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.slider),
    path('header', views.header, name = 'header'),
    path('cart0', views.cart0, name = 'cart0'),
]
